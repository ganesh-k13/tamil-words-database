#!/bin/bash/python3

'''
Author: Ganesh Kathiresan
Github: ganesh-k13

ganesh-k13/tamil-words-database
Copyright (C) 2020  Ganesh Kathiresan

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''


import xml.etree.ElementTree as etree
import argparse
import re
from tqdm import tqdm

NAMESPACES = {'wiki': 'http://www.mediawiki.org/xml/export-0.10/'}
TEXT_XPATH = 'wiki:page/wiki:revision/wiki:text'
TAMIL_REGEX = '([\u0B80-\u0BFF]+)'  # This witchcraft: https://stackoverflow.com/a/22075070/5671364

class TamilParser:
    def __init__(self, filepath):
        self.filepath = filepath
        self.result = set()

    # Utility, use if needed
    @staticmethod
    def is_tamil(word):
        return ord(word[0]) >= 2944 and ord(word[0]) <= 3071

    def yield_text_from_file(self):
        print(f'Parsing {self.filepath}. This may take 10 to 30 seconds depending on your machine...')
        root = etree.parse(self.filepath).getroot()
        for textnode in tqdm(root.findall(TEXT_XPATH, NAMESPACES), desc='Parsing'):
            yield(textnode.text)

    def parse_and_dump(self, outfile):
        for text in self.yield_text_from_file():
            try:
                self.result.update(re.findall(TAMIL_REGEX, text))
            except TypeError:
                pass # [TODO]
        print('Parsing done!')
        with open(outfile, 'w') as f:
            for word in tqdm(self.result, desc='dumping'):
                print(word, file=f)
        print(f'Dump successful! Around {len(self.result)} unique words found!')

if __name__ == '__main__':

    # print(TamilParser.is_tamil("தமிழ்"))

    parser = argparse.ArgumentParser(description='Script to find unique tamil words in wikipedia corpus')
    parser.add_argument('-f', '--filepath', dest='filepath', action='store', help='Path to wiki pages xml dump')
    parser.add_argument('-o', '--outfile', dest='outfile', action='store', help='Path output')


    options = parser.parse_args()
    # import pdb; pdb.set_trace()

    tp = TamilParser(options.filepath)
    tp.parse_and_dump(options.outfile)
