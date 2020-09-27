"""
youtube music downloader
"""

import numpy as np
import argparse
import os

parser = argparse.ArgumentParser(description='download youtube music.')
parser.add_argument('link_path', type=str, help='file path of links')

args = parser.parse_args()

try:
    links = np.loadtxt(args.link_path, delimiter=',', dtype=np.unicode)
except IOError:
    print("no such {}".format(args.link_path))
    exit(-1)

for i, (singer, song, link) in enumerate(links[142:]):
    command = "youtube-dl -x --audio-format mp3 --audio-quality 0 {}".format(link)
    try:
        os.system(command)
    except:
        continue
    for filename in os.listdir('./'):
        if filename.endswith('.mp3'):
            os.rename('./'+filename, './output/{} - {}.mp3'.format(singer, song))
    print("{} {} - {} complete".format(i+1, singer, song))
