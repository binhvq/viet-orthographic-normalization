#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from vietprepro import is_viet_alpha

def main():
    for line in sys.stdin:
        line = line.rstrip().decode('utf-8')
        if line == '':
            print ''
        else:
            syllable, pos = line.split(u'\t')
            print u"{}\t{}".format(generize(syllable), pos).encode('utf-8')

def generize(syllable):
    if syllable.isdigit():
        return u"__NUMBER__"
    # elif is_viet_alpha(syllable):
    #     return syllable
    # return u"__SYMBOL__"
    return syllable

if __name__ == "__main__":
    main()
