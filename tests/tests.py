import os
import sys
import unittest

from PdfFieldFiller import PdfFilePrinter, PdfFieldFiller

# Configure path environment
TESTS_ROOT = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.dirname(TESTS_ROOT)
CONFIG_ROOT = os.path.join(PROJECT_ROOT, 'tests', 'etc')
PDF_ROOT = os.path.join(PROJECT_ROOT, 'tests', 'pdfs')

sys.path.append(PROJECT_ROOT)

class PdfFieldFillerTestCase(unittest.TestCase):
    
    def test_PdfFieldFillerFileLoad(self):
        """
        Testing filling out a templated pdf form file
        """

        # Instantiate Filler Object
        pdf = PdfFieldFiller(os.path.join(CONFIG_ROOT, 'sample_pdf.ini'))
        pdf.post()

        with open(os.path.join(PDF_ROOT, 'sample_filled_test.pdf'), 'rb') as tf:
            pdfTest = tf.read()

        with open(os.path.join(PDF_ROOT, 'sample_filled.pdf'), 'rb') as ff:
            pdfFilled = ff.read()

        self.assertEqual(pdfTest, pdfFilled, msg="Simple test")