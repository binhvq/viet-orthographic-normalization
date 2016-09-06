#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from vietprepro import BoDau, is_viet_alpha

def main():
    for line in sys.stdin:
        sentence = line.rstrip().decode('utf-8')

        words = []
        for w in sentence.split(u' '):
            words.append(splitter(w))

        s = u' '.join(words).encode('utf-8')
        s = s.replace('  ', ' ').replace('  ', ' ')
        print s

def splitter(syllable):
    splited_syllable = []
    for c in syllable:
        if is_viet_alpha(c) or c.isdigit():
            splited_syllable.append(c)
        else:
            splited_syllable.append(u' ' + c + u' ')
    return u''.join(splited_syllable).rstrip()


if __name__ == "__main__":
    main()
