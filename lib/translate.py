import json
from pprint import pprint
class Translate:
  
  # Translate the current template
  def translate(self,template, templateFileName, overrides):
    html = template
    templateName = self.getTemplateName(templateFileName)
    translations = json.dumps(overrides.get(templateName));
    json_object = json.loads(translations)
    html = self.test(html, '', json_object)
    return html
    return ""
    
  def test(self, html, baseKey, json_object):
    for key in json_object.keys():
        replacementKey = "{{" + baseKey + key +"}}"
        replacement = json_object[key]
        if ( isinstance(replacement, str)):
            html = html.replace(replacementKey, replacement)
        else:
            if (baseKey != ""):
                subKey = baseKey  + key + "."
            else:
                  subKey = key + "."
            html = self.test(html, subKey, replacement)
    return html

  # return the template name, so that it can be recognized by translations
  def getTemplateName(self, templateFileName):
    template = templateFileName
    template = template.replace('.html', '');
    template = template.replace ("src/", '');
    return template