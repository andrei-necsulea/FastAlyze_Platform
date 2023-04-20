import zipfile
from lxml import etree
import pandas as pd



def read_docx(docx_file, **kwargs):
    """Read tables as DataFrames from a Word document
    """
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    with zipfile.ZipFile(docx_file).open('word/document.xml') as f:
        root = etree.parse(f)
    for el in root.xpath('//w:tbl', namespaces=ns):
        el.tag = 'table'
    for el in root.xpath('//w:tr', namespaces=ns):
        el.tag = 'tr'
    for el in root.xpath('//w:tc', namespaces=ns):
        el.tag = 'td'
    return pd.read_html(etree.tostring(root), **kwargs)