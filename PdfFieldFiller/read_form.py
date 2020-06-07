from PyPDF2 import PdfFileReader
from sys import argv

def main(filePath):
    pdf = PdfFilePrinter(filePath)
    pdf.peak()

class PdfFilePrinter(PdfFileReader):
    def __init__(self, filePath):
        super().__init__(filePath)
        stream = open(filePath, 'rb')
        self.read(stream)
        self.stream = stream

    def peak(self):
        # pdf = open(self.filePath, 'rb')
            # pdf = self(f)
        info = self.getDocumentInfo()
        fields = self.getFields()
        metadata = self.getXmpMetadata()
        self.stream.close()
        
        if not fields:
            preformatFields = ['NA']
        else:
            preformatFields = [f'\n\t\t\t{list(fields.keys())[i]}' if i % 5 == 0 and i != 0  else list(fields.keys())[i] for i in range(len(fields))]
        
        stdout = f"""
        title:      {info.title}
        subject:    {info.subject}
        author:     {info.author}
        creator:    {info.creator}
        producer:   {info.producer}

        metadata:   {metadata}
        fields:     {','.join(preformatFields)}
        """ 
        print(stdout)


if __name__ == '__main__':
    main(argv[1])