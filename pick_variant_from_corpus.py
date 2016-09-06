#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This script picks up Vietnamese syllable variation from corpus that on standard input.
"""

import sys
import unicodedata
from viet_spliter import splitter
from collections import defaultdict

# Diacritics list
tone_list = (
    u'\u0300', # Huyền, à
    u'\u0301', # Sắc, á
    u'\u0303', # Ngã, ã
    u'\u0309', # Hỏi, ả
    u'\u0323', # Nặng, ạ
)

def main():
    # Create dictionary
    sy_dic = defaultdict(lambda:defaultdict(int))

    # Read line from standard input
    for line in sys.stdin:
        # Get a syllables list
        lower_syllables = splitter(line.rstrip().lower().decode('utf-8')).split()
        for syllable in lower_syllables:
            if not is_correct_syllable(syllable):
                continue

            splitted_syllable, tone_mark = split_tone(syllable)
            if tone_mark == u'':
                continue

            sy_dic[(splitted_syllable, tone_mark)][syllable] += 1

    for syllable_tone, syllable_dic in sy_dic.iteritems():
        base_syllable = syllable_tone[0]
        variant_syllable = u'\t'.join([u'{}\t{}'.format(s, f) for s, f in sorted(syllable_dic.items(), key=lambda x:x[1], reverse=True)])

        if len(syllable_dic) > 1:
            print variant_syllable.encode('utf-8')

def is_correct_syllable(syllable):
    """
    If a syllable contains more than two diacritics marks, then it's wrong.
    """
    splited_syllable = unicodedata.normalize('NFD', syllable)
    return len([s for s in splited_syllable if s in tone_list]) < 2

def split_tone(input_syllable):
    syllable = []
    tones = u''
    for c in input_syllable:
       for c_n in unicodedata.normalize('NFD', c):
           if c_n in tone_list:
               tones = c_n
               continue
           else:
               syllable.append(c_n)
    return unicodedata.normalize('NFC', u''.join(syllable)), tones


if __name__ == "__main__":
    main()
