# pip install pdfminer

import pdfminer
import pandas as pd

# from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine

def extract_text_from_pdf(path):
    '''
    extract text from pdf
    the function works for asian language

    path `str` to pdf file e.g. './folder_name/text.pdf'
    extracted_text `str`

    source: stackoverflow
    '''
    fp = open(path, 'rb')

    parser = PDFParser(fp)
    doc = PDFDocument(parser)
    # parser.set_document(doc)
    # doc.set_parser(parser)
    # doc.initialize('')
    rsrcmgr = PDFResourceManager()
    laparams = LAParams()
    laparams.char_margin = 1.0
    laparams.word_margin = 1.0
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    extracted_text = ''
    for page in PDFPage.create_pages(doc):
    # for page in doc.get_pages():
        interpreter.process_page(page)
        layout = device.get_result()
        for lt_obj in layout:
            if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
                extracted_text += lt_obj.get_text()

    return extracted_text


def cleanse_df(df):
    '''
    clean the dataframe

    df: `pd.DataFrame`
    '''
    # strip the space out when the datatype is string
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    # we can add more cleansing here is needed
    # blah blah blah

    return df
