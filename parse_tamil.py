import xml.etree.ElementTree as etree
import lxml.etree
# p root.findall('m:page/m:revision/m:text', namespaces)[1].text

NAMESPACES = {'m': 'http://www.mediawiki.org/xml/export-0.10/'}

class TamilParser:
    def __init__(self):
        pass

    @staticmethod
    def is_tamil(word):
        return ord(word[0]) >= 2944 and ord(word[0]) <= 3071

    def yield_text_from_file(filename):
        root = etree.parse(filename).getroot()
        for textnode in root.findall('m:page/m:revision/m:text', NAMESPACES):
            yield(textnode.text)
        #for event, elem in etree.iterparse(filename, events=('start', 'end')):
        #    if event == 'start':
        #        import pdb; pdb.set_trace()

if __name__ == '__main__':
    print(TamilParser.is_tamil("112i"))
    print(TamilParser.is_tamil("தமிழ்"))

    TamilParser.yield_text_from_file('tawiki-20200701-pages-meta-current.xml')
