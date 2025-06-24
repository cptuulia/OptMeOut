########################################################################
#
# A class to export translations json to cvs files
#
########################################################################
import json
from pprint import pprint
from pathlib import Path


class CvsExport:
  
  #
  # Constructor
  # 
  def __init__(self, languagesDir, csvDir):
    self.languagesDir = languagesDir
    self.csvDir = csvDir
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

