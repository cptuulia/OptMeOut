import json
import os
import time

from pathlib import Path
from http.server import SimpleHTTPRequestHandler, HTTPServer
# enable var_dump as pprint
from pprint import pprint
import multiprocessing
from lib.translate import Translate
from lib.translationsExport import TranslationsExport
from lib.cvsImport import CvsImport

# Paths
TEMPLATE_PATH ="src/template.html"
STEPS_PATH = "src/steps.json"
LANGUAGES_DIR = "src/languages"
DIST_DIR = "dist"
CSV_DIR = "dist/csv"
JS_DIR = "dist/js"



def initialize_folders():
    Path(DIST_DIR).mkdir(exist_ok=True)
    Path(CSV_DIR).mkdir(exist_ok=True)
    Path(JS_DIR).mkdir(exist_ok=True)

# Generate HTML files
def generate_html():
    initialize_folders()
    

    translateObj = Translate()
    # Load steps
    with open(Path(STEPS_PATH), "r") as f:
        steps = json.load(f)

    # Load languages
    languages = {}
    for lang_file in Path(LANGUAGES_DIR).glob("*.json"):
        with open(lang_file, "r") as f:
            languages[lang_file.stem] = json.load(f)
  
    with open( Path(TEMPLATE_PATH), "r") as f:
        template = f.read()
        templateName = f.name
    for lang, overrides in languages.items():
        html = translateObj.translate(template, templateName, overrides)
        javascriptFile = 'js/' + lang +'.js'
        html = html.replace('{{translations_javascript}}', javascriptFile)

        output_path = Path(DIST_DIR) / f"{lang}.html"
        with open(output_path, "w") as f:
            f.write(html)
        print(f"Generated {output_path}")
        

if __name__ == "__main__":
    initialize_folders()
    CvsImport = CvsImport(LANGUAGES_DIR, CSV_DIR)
    CvsImport.importAll()
    generate_html()
    translationsExport = TranslationsExport(Path(LANGUAGES_DIR), CSV_DIR, JS_DIR)
    translationsExport.exportAll();

   
  