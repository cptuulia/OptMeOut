import json
import config

from pathlib import Path
# enable var_dump as pprint
from pprint import pprint
from lib.cvsImport import CvsImport
from lib.translationsExport import TranslationsExport
from lib.htmlGenerator import HtmlGenerator


def initialize_folders():
    # make the folders if they dont exist
    Path(config.DIST_DIR).mkdir(exist_ok=True)
    Path(config.CSV_DIR).mkdir(exist_ok=True)
    Path(config.CSV_DIR + '/export').mkdir(exist_ok=True)
    Path(config.CSV_DIR + '/import').mkdir(exist_ok=True)
    Path(config.JS_DIR).mkdir(exist_ok=True)
   

if __name__ == "__main__":
    initialize_folders()
    cvsImport = CvsImport()
    cvsImport.importAll()
    htmlGenerator = HtmlGenerator()
    htmlGenerator.generate()
    translationsExport = TranslationsExport()
    translationsExport.exportAll()

   
  