# -*- coding: utf-8 -*-
"""
Created on Wed May 15 2020

Written by EJ_Chang

Web clawer
"""

import os
from youtube_transcript_api import YouTubeTranscriptApi
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

video_id = ['sNoI-ovrAGs','sNoI-ovrAGs']

# video_id = [
#     'cT-Xj05v4T0',
#     'FadfT_UCzKY',
#     'jpy0Y3ILWMw',
#     'NOLI-Kp0ay4',
#     'bx7aFlrsG_8',
#     'HJfdLq-y6rI',
#     '1Z8z7x-4AJI',
#     'tHaFNXJ95Y8',
#     'gkPUHsTqB50',
#     'hqwXPk4ZpmU',
#     '7XjfBs88wAI',
#     'EGIcXdKU4KE',
#     'Ov98ME59_Jk',
#     '_CFnhQTYDXc',
#     'Y5YL5Szst-Q'
#     ]

full_text = []
print(len(video_id))
for video in range(len(video_id)):

    # Load script
    boring = YouTubeTranscriptApi.get_transcript(video_id[video], 
                                                 languages=['en'])
    # full_text = []
    print(len(boring))
    for textline in range(len(boring)):
        full_text.append(boring[textline]['text'])

    # # Experiment record file
    # os.chdir('/Users/YJC/Dropbox/BoringTask')
    # filename = ('YTscript_%s.txt' % (video_id[video]))
    # filecount = 0

    # while os.path.isfile(filename):
    #     filecount += 1
    #     filename = ('YTscript_%s_%d.txt' % (video_id[video], filecount))


    # with open(filename, 'w') as filehandle: # File auto closed
    #     filehandle.writelines("%s\n" % key for key in full_text)

# Experiment record file
os.chdir('/Users/YJC/Dropbox/BoringTask')

filename = ('YTscript_test.txt')

with open(filename, 'w') as filehandle: # File auto closed
    filehandle.writelines("%s\n" % key for key in full_text)


'''
word cloud
'''


