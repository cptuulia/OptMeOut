########################################################################
#
# A class to generate html from templates and fill the translations
#
########################################################################
import json
import config
import shutil   
from pprint import pprint
from pathlib import Path
from lib.translate import Translate
from lib.languageCodes import LanguageCodes

class HtmlGenerator:
  
  
    #
    # Constructor
    # 
    def __init__(self):
        self.languages = self.__get_configured_languages()

    # Generate HTML files
    def generate(self):
      
      self.__generateLanguageTemplates(config.SRC_TEMPLATE_PATH + '/index.html')
      path = config.SRC_TEMPLATE_PATH + '/src'
      self.__crawl(path)
      self.__copy_react_root_files()
      self.__set_default_index()
      return    

    #
    # Get the the configured languages 
    #
    def __get_configured_languages(self):
        
        languages = {}
        for lang_file in Path(config.LANGUAGES_DIR).glob("*.json"):
          with open(lang_file, "r") as f:
              languages[lang_file.stem] = json.load(f)
        return languages

    #
    # Copy the react files in the root folder
    #
    # read all of the files in the root folder and copy them
    # Like all config files
    #
    def __copy_react_root_files(self):
        
        for rootFile in Path(config.SRC_TEMPLATE_PATH).glob("*.*"):
            source =  str(rootFile)
            target = config.DIST_DIR  + source.replace(config.SRC_TEMPLATE_PATH ,'')
            shutil.copy(source, target)

    #
    # Generate the language templates for the given language
    #  
    def __generateLanguageTemplates(self, srcFile):
        translateObj = Translate()
        languageCodes = LanguageCodes()
        try:                                        
            with open( Path(srcFile), "r") as f:
                template = f.read()
                templateName = f.name
            for lang, overrides in self.languages.items():
                html = translateObj.translate(template, templateName, overrides)
                # update language codes
                html = html.replace('{{LANGUAGE_CODE}}', lang)
                # update language select options
                languageHtmlOptions = languageCodes.get_language_options_html(lang,self.languages)
                html = html.replace('{{LANGUAGE_HTML_OPTIONS}}', languageHtmlOptions)
                # write file
                distFile = self.__distFileName(srcFile, lang)
                output_path = Path(config.DIST_DIR) / f"{distFile}"
                with open(output_path, "w") as f:
                    f.write(html)
                print(f"Generated {output_path}")
        except UnicodeDecodeError:
            pass # Found non-text data
    #
    # Make file index.html from the default language index file
    #
    def __set_default_index(self):
        source = config.DIST_DIR + '/index_' + config.DEFAULT_LANGUAGE +'.html'
        target = config.DIST_DIR + '/index.html'
        shutil.copy(source, target)      


    #
    # Get file name for the given template and language
    #
    def __distFileName(self, srcFile, lang) :
        srcFile = srcFile.replace(config.SRC_TEMPLATE_PATH + '/' ,'')
        parts = srcFile.split('.')
        file = parts[0]
        extension =  parts[1]
        return file +'_' + lang + '.' + extension

    #
    # Crawl all of the files and folder in the give folder and make translations
    #
    def __crawl(self, path):
        self.__makeDistFolder(path)
        for file in Path(path).glob("*"):
            if (file.is_dir()):
                # crawl a sub folder
                self.__crawl(str(file))
            else:
                self.__generateLanguageTemplates(str(file))
    #
    # make the given source folder in the dist folder
    # if it does not exist
    #
    def __makeDistFolder(self,srcPath):
        srcPath = srcPath.replace(config.SRC_TEMPLATE_PATH + '/' ,'')
        distPath = config.DIST_DIR + '/' + srcPath
        Path(distPath).mkdir(exist_ok=True)
