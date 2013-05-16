import xml.etree.ElementTree as ET

from lojban_grammar import text
from ReduceXML import *

xml = ET.fromstring(text.parseString('mi besto').asXML())
d = convertToDict(xml)

print(reduceDict(d))
