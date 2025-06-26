import json
import os
import time
import config

from pathlib import Path
from http.server import SimpleHTTPRequestHandler, HTTPServer
# enable var_dump as pprint
from pprint import pprint
import multiprocessing
from lib.translate import Translate
from lib.translationsExport import TranslationsExport
from lib.cvsImport import CvsImport


def initialize_folders():
    Path(config.DIST_DIR).mkdir(exist_ok=True)
    Path(config.CSV_DIR).mkdir(exist_ok=True)
    Path(config.JS_DIR).mkdir(exist_ok=True)
   

# Generate HTML files
def generate_html():
    initialize_folders()
    

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
        

if __name__ == "__main__":
    initialize_folders()
    CvsImport = CvsImport()
    CvsImport.importAll()
    generate_html()
    translationsExport = TranslationsExport()
    translationsExport.exportAll();

   
  