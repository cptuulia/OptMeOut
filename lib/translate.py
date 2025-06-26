import json
from pprint import pprint
class Translate:
  
  #
  # Translate the current template
  #
  def translate(self,template, templateFileName, overrides):
    html = template
    templateName = self.__getTemplateName(templateFileName)
    translations = json.dumps(overrides.get(templateName));
    json_object = json.loads(translations)
    html = self.__translateSet(html, '', json_object)
    return html
  
  #
  # Translate 
  #  
  def __translateSet(self, html, baseKey, json_object):
    for key in json_object.keys():
        placeHolder = "{{" + baseKey + key +"}}"
        translation = json_object[key]
        if ( isinstance(translation, str)):
            html = html.replace(placeHolder, translation)
        else:
            if (baseKey != ""):
                subKey = baseKey  + key + "."
            else:
                  subKey = key + "."
            html = self.__translateSet(html, subKey, translation)
    return html

  #
  # return the template name, so that it can be recognized by translations
  #
  def __getTemplateName(self, templateFileName):
    template = templateFileName
    template = template.replace('.html', '');
    template = template.replace ("src/", '');
    return template