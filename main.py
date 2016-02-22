# -*- coding: utf-8 -*-
import sys

import sound


def open_file(file_path):
    ''' return a sound object for the given file name'''
    return sound.load_sound(file_path)

def remove_vocals(sound_obj):
    num_samples = len(sound_obj)
    new_sound = sound.create_sound(num_samples)

    for i in range(num_samples):
        orig_samp = sound.get_sample(sound_obj,i)
        new_samp = sound.get_sample(new_sound,i)
        left_ch = sound.get_left(orig_samp)
        right_ch = sound.get_right(orig_samp)
        result = int( (left_ch - right_ch) / 2.0 )
        sound.set_left(new_samp,result)
        sound.set_right(new_samp,result)

    return new_sound

if __name__ == '__main__':
    file_path = sys.argv[1]
    file_name = file_path.split('/')[-1]
    file_name_split = file_name.split('.')
    sound_obj = open_file(file_path)
    new_sound = remove_vocals(sound_obj)
    new_file_name = file_name_split[0] + '_novoice' + '.wav' 
    new_sound.save_as(new_file_name)

    print "Success.. Exiting.."


