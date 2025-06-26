########################################################################
#
# A class to export translations json to cvs and javascript files
#
########################################################################
import json
import config
from pprint import pprint
from pathlib import Path


class TranslationsExport:
  
  #
  # Constructor
  # 
  def __init__(self):
    self.englishArr = self.__setEnglishArr()
    self.currentLanguageToExport = ''
    
  #
  # Export all languages
  #  
  def exportAll(self):
    languages = {}
    for langFile in Path(config.LANGUAGES_DIR).glob("*.json"):
        with open(langFile, "r") as f:
          languages[langFile.stem] = json.load(f)
    for lang, translations in languages.items():
      self.currentLanguageToExport = lang
      self._exportLanguage(translations)

  #
  # Set the array of english translations
  # This will be as a source translation in csv files
  #  
  def __setEnglishArr(self):
    self.englishArr = {}
    languagesDirStr = str(config.LANGUAGES_DIR)
    langFile = languagesDirStr + "/en_GB.json"
    with open(langFile, "r") as f:
      translationsJson = json.load(f)
    templateKey = list(translationsJson)[0]
    return self.__getTranslationsArray(self.englishArr, '', translationsJson[templateKey])

  #
  # Export the json of one language
  # 
  def _exportLanguage(self, translationsJson):
    valuesArr = {};
    templateKey = list(translationsJson)[0]
    itemsJson = translationsJson[templateKey]
    valuesArr = self.__getTranslationsArray(valuesArr, '', itemsJson)
    
    csvStr = self.__makeCsvContent(valuesArr)
    self.__makeCsvFile(csvStr)
    self.__makeJsFile(valuesArr)
    
  #
  # Make csv content from translation arrays
  # 
  def __makeCsvContent(self, valuesArr):
    csv = "Key,English,Translation (" + self.currentLanguageToExport.upper() + ")\n"
    for key in self.englishArr:
      csv = csv +  key + config.CSV_FIELD_SEPARATOR
      csv = csv + self.englishArr[key] + config.CSV_FIELD_SEPARATOR
      value = valuesArr.get(key)
      if ( isinstance(value, str)):
        csv = csv + value + "\n"
      else:   
        csv = csv + "\n"
    return csv

  #
  # Make csv file from translation arrays
  # 
  def __makeCsvFile(self, csvStr):
    lang = self.currentLanguageToExport
    csvDir = config.CSV_DIR + '/'
    csvFileName = csvDir + lang + '.csv'
    with open(csvFileName, "w") as f:
      f.write(csvStr)
  
  #
  # Make javascript file from translation arrays
  # 
  def __makeJsFile(self, translationsArr):
    
    jsonStr = json.dumps(translationsArr)
    lang = self.currentLanguageToExport
    script =  "let translationsJson='" + jsonStr + "';"
    script = script + " let  globalTranslationsObj = JSON.parse(translationsJson);"
    script = script + " function _trns(translation){return(globalTranslationsObj[translation]);}"
    jsDir = config.JS_DIR + '/'
    jsFileName = jsDir + lang + '.js'
    with open(jsFileName, "w") as f:
      f.write(script)

   
  #
  # Get translations array from the json
  # 
  def __getTranslationsArray(self, translationsJson,  baseKey, itemsJson):
    for key in itemsJson.keys():
      arrayKey =  baseKey + key 
      value = itemsJson[key]
      if ( isinstance(value, str)):
        translationsJson[arrayKey] = value
      else:
          if (baseKey != ""):
              subKey = baseKey  + key + "."
          else:
            subKey = key + "."
          translationsJson = self.__getTranslationsArray(translationsJson, subKey, value)
    return translationsJson

