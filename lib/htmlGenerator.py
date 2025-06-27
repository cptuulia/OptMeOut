########################################################################
#
# A class to generate html from templates and fill the translations
#
########################################################################
import json
import config
from pprint import pprint
from pathlib import Path
from lib.translate import Translate

class HtmlGenerator:
  
  
    # Generate HTML files
    def generate(self):
      
      path = config.TEMPLATE_PATH + '/app'
      self.__loadLanguages(config.TEMPLATE_PATH + '/index.html')
      self.__crawl(path)
      return    
      
    def __loadLanguages(self, srcFile):
        translateObj = Translate()
                                                                      
        # Load languages
        languages = {}
        for lang_file in Path(config.LANGUAGES_DIR).glob("*.json"):
          with open(lang_file, "r") as f:
              languages[lang_file.stem] = json.load(f)
    
        with open( Path(srcFile), "r") as f:
          template = f.read()
          templateName = f.name
        for lang, overrides in languages.items():
          html = translateObj.translate(template, templateName, overrides)
          javascriptFile = 'js/' + lang +'.js'
          html = html.replace('{{translations_javascript}}', javascriptFile)
          distFile = self.__distFileName(srcFile, lang)
          output_path = Path(config.DIST_DIR) / f"{distFile}"
          with open(output_path, "w") as f:
              f.write(html)
          print(f"Generated {output_path}")

    def __distFileName(self, srcFile, lang) :
        srcFile = srcFile.replace('src/' ,'')
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
                self.__loadLanguages(str(file))
    #
    # make the given source folder in the dist folder
    # if it does not exist
    #
    def __makeDistFolder(self,srcPath):
        srcPath = srcPath.replace('src/' ,'')
        distPath = config.DIST_DIR + '/' + srcPath
        Path(distPath).mkdir(exist_ok=True)
        #pprint(srcPath)
        #pprint(distPath)   