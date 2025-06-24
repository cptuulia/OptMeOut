########################################################################
#
# A class to export translations json to cvsand javascript files
#
########################################################################
import json
from pprint import pprint
from pathlib import Path


class TranslationsExport:
  
  #
  # Constructor
  # 
  def __init__(self, languagesDir, csvDir, jsDir):
    self.languagesDir = languagesDir
    self.csvDir = csvDir
    self.jsDir = jsDir
    self.englishArr = self.setEnglishArr()
    self.currentLanguageToExport = ''
    
  #
  # Export all languages
  #  
  def exportAll(self):
    languages = {}
    for langFile in self.languagesDir.glob("*.json"):
        with open(langFile, "r") as f:
          languages[langFile.stem] = json.load(f)
    for lang, translations in languages.items():
      self.currentLanguageToExport = lang
      self.exportLanguage(translations)

  #
  # Set the array of english translations
  # This will be as a source translation in csv files
  #  
  def setEnglishArr(self):
    self.englishArr = {}
    languagesDirStr = str(self.languagesDir.as_posix())
    langFile = languagesDirStr + "/en.json"
    with open(langFile, "r") as f:
      translationsJson = json.load(f)
    templateKey = list(translationsJson)[0]
    return self.getTranslationsArray(self.englishArr, '', translationsJson[templateKey])

  #
  # Export the json of one language
  # 
  def exportLanguage(self, translationsJson):
    valuesArr = {};
    templateKey = list(translationsJson)[0]
    itemsJson = translationsJson[templateKey]
    valuesArr = self.getTranslationsArray(valuesArr, '', itemsJson)
    
    csvStr = self.makeCsvContent(valuesArr)
    self.makeCsvFile(csvStr)
    self.makeJsFile(valuesArr)
    
  #
  # Make csv content from translation arrays
  # 
  def makeCsvContent(self, valuesArr):
    csv = "Key,English,Translation (" + self.currentLanguageToExport.upper() + ")\n"
    for key in self.englishArr:
      csv = csv +  key + ','
      csv = csv + self.englishArr[key] + ','
      value = valuesArr.get(key)
      if ( isinstance(value, str)):
        csv = csv + value + "\n"
      else:   
        csv = csv + "\n"
    return csv

  #
  # Make csv file from translation arrays
  # 
  def makeCsvFile(self, csvStr):
    lang = self.currentLanguageToExport
    csvDir = self.csvDir.as_posix() + '/'
    csvFileName = csvDir + lang + '.csv'
    with open(csvFileName, "w") as f:
      f.write(csvStr)
  
  #
  # Make javascript file from translation arrays
  # 
  def makeJsFile(self, translationsArr):
    
    jsonStr = json.dumps(translationsArr)
    lang = self.currentLanguageToExport
    script =  "let translationsJson='" + jsonStr + "';"
    script = script + " let  globalTranslationsObj = JSON.parse(translationsJson);"
    script = script + " function _trns(translation){return(globalTranslationsObj[translation]);}"
    jsDir = self.jsDir.as_posix() + '/'
    jsFileName = jsDir + lang + '.js'
    with open(jsFileName, "w") as f:
      f.write(script)

   
  #
  # Get translations array from the json
  # 
  def getTranslationsArray(self, translationsJson,  baseKey, itemsJson):
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
          translationsJson = self.getTranslationsArray(translationsJson, subKey, value)
    return translationsJson

