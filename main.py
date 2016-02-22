# -*- coding: utf-8 -*-
import sys

import sound


def open_file(file_name):
    ''' return a sound object for the given file name'''
    return sound.load_sound(file_name)


if __name__ == '__main__':
    file_name = sys.argv[1]
    sound_obj = open_file(file_name)



