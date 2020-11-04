"""
youtube music downloader
"""

import numpy as np
import argparse
import os
from pydub import AudioSegment, effects

parser = argparse.ArgumentParser(description='download youtube music.')
parser.add_argument('link_path', type=str, help='file path of links')

args = parser.parse_args()

try:
    links = np.loadtxt(args.link_path, delimiter=',', dtype=np.unicode)
except IOError:
    print("no such {}".format(args.link_path))
    exit(-1)


def download_music(infos):
    errors = []
    for i, (singer, song, link) in enumerate(infos):
        command = "youtube-dl -x --audio-format mp3 --audio-quality 0 {}".format(link)
        return_value = os.system(command)
        if return_value != 0:
            errors.append((singer, song, link))
            continue

        for filename in os.listdir('./'):
            if filename.endswith('.mp3'):
                raw = AudioSegment.from_mp3(filename)
                raw_normalized = effects.normalize(raw)
                raw_normalized.export(filename, format="mp3")
                os.rename('./' + filename, './output/{} - {}.mp3'.format(singer, song))
        print("{} {} - {} complete".format(i + 1, singer, song))
    if errors:
        download_music(errors)


download_music(links[1:])
