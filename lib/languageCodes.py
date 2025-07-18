########################################################################
#
# A class to handle language codes
#
########################################################################
from pprint import pprint

class LanguageCodes:
   
    #
    # Constructor
    # 
    def __init__(self, languages):
        self.codes = self.__set_codes(languages)
        
   
    #
    # Get html options for the selected language
    #
    def get_language_options_html(self, currentLang, languages):
        options = ""
        for lang, overrides in languages.items():
            options = options + '<option value="' + lang + '"'
            if currentLang == lang:
                options = options + ' selected={true}'
            options = options + ' >'
            options = options + self.codes[lang] 
            options = options + '</option>'
        return options 

    #
    # Get all language codes
    #
    def __set_codes(self,languages):
        codes = {}
        for lang, overrides in languages.items():
            codes[lang] = overrides["menu"]['locale']
            pprint(lang)
            pprint(overrides["menu"]['locale'])
        return codes
        

