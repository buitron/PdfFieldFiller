from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.generic import BooleanObject, NameObject, IndirectObject
from sys import argv

from . import utils

from .utils import ConfigRetriever


class PdfFieldFiller(PdfFileWriter):
    
    def __init__(self, configFile):
        super().__init__()
        config = ConfigRetriever(configFile)
        self.sourceFile = config.getSourceFilePath()
        self.targetFile = config.getTargetFilePath()
        self.fields = config.getFieldDict()
        self.metadata = config.getMetaDataDict()

    def _setMetaData(self, **info):
        self.metadata = info
    
    def _setFields(self, **fields):
        # If you need to set specific logic for certain fields, override this function
        self.fields = fields

    def _setNeedAppearanceWriter(self):
        # See 12.7.2 and 7.7.2 for more information: http://www.adobe.com/content/dam/acom/en/devnet/acrobat/pdfs/PDF32000_2008.pdf
        try:
            catalog = self._root_object
            # get the AcroForm tree
            if "/AcroForm" not in catalog:
                self._root_object.update({NameObject("/AcroForm"): IndirectObject(len(self._objects), 0, self)})

            need_appearances = NameObject("/NeedAppearances")
            self._root_object["/AcroForm"][need_appearances] = BooleanObject(True)
        except Exception as e:
            print('setNeedAppearanceWriter() catch : ', repr(e))
        finally:
            return self

    def post(self):
        with open(self.sourceFile, 'rb') as f:
            sourcePDF = PdfFileReader(f, strict=False)
            if "/AcroForm" in sourcePDF.trailer["/Root"]:
                sourcePDF.trailer["/Root"]["/AcroForm"].update({NameObject("/NeedAppearances"): BooleanObject(True)})
        
            self._setNeedAppearanceWriter()
            if "/AcroForm" in self._root_object:
                self._root_object["/AcroForm"].update({NameObject("/NeedAppearances"): BooleanObject(True)})
            
            self.appendPagesFromReader(sourcePDF)
            
            if self.metadata:
                metadata = dict(map(lambda x: (f'/{x[0].title()}', x[1]), self.metadata.items()))
                self.addMetadata(metadata)
            
            self.updatePageFormFieldValues(self.getPage(0), self.fields)
            
            with open(self.targetFile, 'wb') as f:
                self.write(f)

if __name__ == '__main__':
    main(argv[1])