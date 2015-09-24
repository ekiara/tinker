#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""removing-duplite-words.py: Removing duplicate words from a string"""

__author__ = 'Eric Kiara'
__copyright__ = 'Copyright 2009, Eric Kiara'
__license__ = 'GPLv3.0'
__version__ = '0.0.1'
__maintainer__ = 'Eric Kiara'
__email__ = 'ekiara@gmail.com'
__status__ = 'Alpha'
__resources__ = ['http://stackoverflow.com/questions/9841303/removing-duplicate-characters-from-a-string',]

# Sample Words
nm0 = 'JAMIMAH WANGOI WANJIRU JAMIMAH WANGOI WANJIRU'
nm1 = 'JAMIMAH WANGOI WANJIRU'
nm2 = 'SHIVO ELIZABETH  IMONYANGWA SHIVO ELIZABETH IMONYANGWA'
nm3 = 'GITHINJI GEOFFREY GITHUI GITHINJI.GEOFFREY.GITHUI'
nm4 = 'WAMUKOTA MOSES WANYAMA WAMUKOTA'


def remove_duplicate_words(word):
    """remove_duplicate_words"""
    word_as_list = word.replace(',',' ').replace('.',' ').split()
    return ' '.join(sorted(set(word_as_list), key=word_as_list.index))
