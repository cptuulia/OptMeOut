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
      
      translateObj = Translate()
      # Load steps
      with open(Path(config.STEPS_PATH), "r") as f:
          steps = json.load(f)

      # Load languages
      languages = {}
      for lang_file in Path(config.LANGUAGES_DIR).glob("*.json"):
          with open(lang_file, "r") as f:
              languages[lang_file.stem] = json.load(f)
    
      with open( Path(config.TEMPLATE_PATH), "r") as f:
          template = f.read()
          templateName = f.name
      for lang, overrides in languages.items():
          html = translateObj.translate(template, templateName, overrides)
          javascriptFile = 'js/' + lang +'.js'
          html = html.replace('{{translations_javascript}}', javascriptFile)

          output_path = Path(config.DIST_DIR) / f"{lang}.html"
          with open(output_path, "w") as f:
              f.write(html)
          print(f"Generated {output_path}")
          