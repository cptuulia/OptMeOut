import json
from pprint import pprint
class Translate:
  
  #
  # Translate the current template
  #
  def translate(self,template, templateFileName, overrides):
    html = template
    templateName = self.__getTemplateName(templateFileName)
    translations = json.dumps(overrides);
    json_object = json.loads(translations)
    html = self.__translateSet(html, '', json_object)
    return html
  
  #
  # Translate 
  #
  #
  # Translates from a json string, which might have child objects
  # like 
  # {
  #   'step1':
  #     { 
  #       'title': 'titel',
  #       'properties':{
  #         'name' : 'Naam', 
  #         'address': 'Adres
  #     }
  # }
  # 
  #  This fills the replacements: 
  #  {{step1.title}}
  #  {{step1.properties.name}}
  #  {{step1.properties.address}}
  #  
  def __translateSet(self, html, baseKey, json_object):
    for key in json_object.keys():
        placeHolder = "[[" + baseKey + key +"]]"
        translation = json_object[key]
        if ( isinstance(translation, str)):
            # We hav have value to replace
            html = html.replace(placeHolder, translation)
        else:
            # The translation is not yet value, but part of
            # json object, like properties.name
            if (baseKey != ""):
                subKey = baseKey  + key + "."
            else:
                  subKey = key + "."
            html = self.__translateSet(html, subKey, translation)
    html = self.__formatHtml(html)        
    return html

  #
  # Format html with special rules
  #
  def __formatHtml(self, html):
    # ‘opt-out’ must be red
    html = html.replace("‘opt-out’",'<span style={{color: "red"}}>' + "'" + 'opt-out' + "'" + '</span>' )

    # Text beteen <red> and  </red> to red
    # 
    # <red>Tell  me more</red>  => <span style={{color: "red"}}>Tell  me more</span>
    #
    html = html.replace("<red>",'<span style={{color: "red"}}>' )
    html = html.replace("</red>", '</span>' )
    return html

  #
  # return the template name, so that it can be recognized by translations
  #
  def __getTemplateName(self, templateFileName):
    template = templateFileName
    template = template.replace('.html', '');
    template = template.replace ("src/", '');
    return template