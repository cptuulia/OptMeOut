import json
import config

from pathlib import Path
# enable var_dump as pprint
from pprint import pprint
from lib.cvsImport import CvsImport
from lib.translationsExport import TranslationsExport
from lib.htmlGenerator import HtmlGenerator



if __name__ == "__main__":
    #initialize_folders()
    cvsImport = CvsImport()
    cvsImport.importAll()
    htmlGenerator = HtmlGenerator()
    htmlGenerator.generate()
    translationsExport = TranslationsExport()
    translationsExport.exportAll()

   
  