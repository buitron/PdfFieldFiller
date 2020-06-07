from configparser import ConfigParser
from os import path

class ConfigRetriever():
    def __init__(self, filePath):
        self.config = ConfigParser()
        self.config.read(filePath)

    def getSourceFilePath(self):
        return self.config['File'].get('source_path') + self.config['File'].get('source_name')

    def getTargetFilePath(self):
        return self.config['File'].get('target_path') + self.config['File'].get('target_name')

    def getFieldDict(self):
        return dict(self.config['Fillable Fields'])

    def getMetaDataDict(self):
        return dict(self.config['PDF Information'])

if __name__ == '__main__':
    print('\nTesting')
    config = ConfigRetriever(path.join('..', 'etc', 'sample_pdf.ini'))
    print(config.getMetaDataDict())