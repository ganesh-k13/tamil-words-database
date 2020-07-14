import xml.etree.ElementTree as etree
import argparse
import re
from tqdm import tqdm

NAMESPACES = {'wiki': 'http://www.mediawiki.org/xml/export-0.10/'}
TEXT_XPATH = 'wiki:page/wiki:revision/wiki:text'
TAMIL_REGEX = '([\u0B80-\u0BFF]+)'  # This witchcraft: https://stackoverflow.com/a/22075070/5671364 | @Rahul-RB likes this

class TamilParser:
    def __init__(self, filepath):
        self.filepath = filepath

    # Utility, use if needed
    @staticmethod
    def is_tamil(word):
        return ord(word[0]) >= 2944 and ord(word[0]) <= 3071

    def yield_text_from_file(self):
        print('Parsing dump file. This may take 10 to 30 seconds depending on your machine...')
        root = etree.parse(self.filepath).getroot()
        for textnode in tqdm(root.findall(TEXT_XPATH, NAMESPACES), desc='Progess'):
            yield(textnode.text)

    def parse_text(self):
        for text in self.yield_text_from_file():
            print(re.findall(TAMIL_REGEX, text))
            break

if __name__ == '__main__':

    # print(TamilParser.is_tamil("தமிழ்"))

    parser = argparse.ArgumentParser(description='Script to find unique tamil words in wikipedia corpus')
    parser.add_argument('-f', '--filepath', dest='filepath', action='store', help='Path to wiki pages xml dump')

    options = parser.parse_args()
    # import pdb; pdb.set_trace()

    tp = TamilParser(options.filepath)
    tp.parse_text()
