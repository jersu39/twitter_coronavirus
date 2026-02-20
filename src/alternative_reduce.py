#!/usr/bin/env python3

# args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--hashtags',nargs='+',required=True)
args = parser.parse_args()

# other imports
import os
import json
from collections import Counter,defaultdict
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.font_manager
import numpy as np
import glob

'''
CN_font = FontProperties(fname = '/usr/share/fonts/cmap/adobe-cns1')
KR_font = FontProperties(fname = '/usr/share/fonts/cmap/adobe-korea1')
JP_font = FontProperties(fname = '/usr/share/fonts/cmap/adobe-japan1')
EN_font = FontProperties('DejaVu Sans')
#mpl.rcParams['font.family'] = ['DejaVu Sans', CN_font, KR_font, JP_font]
'''

matplotlib.font_manager.findSystemFonts(fontpaths=None, fontext='ttf')


# load each of the input paths
total = defaultdict(lambda: Counter())
files = np.sort(glob.glob('outputs/geoTwitter20-*.zip.country'))
'''
for path in files:
    with open(path) as f:
        tmp = json.load(f)
        for subdic in tmp.values():
            print(subdic)
            #for trueval in subdic.values():
            #    print(trueval)
        for k in tmp:
            total[k] += tmp[k]
'''
# dic of dic of tweets in each lang/country mentioning subkey each day
'''
dic = {}
for key in args.hashtags:
    dic[key] = []
    for path in files:
        with open(path) as f:
            tmp = json.load(f)

            for subdic in tmp.values():
                print(subdic)
                #if list(subdic.items()) in args.hashtags:
                    dic[key].append(day)
'''
dic = {}
for hash in args.hashtags:
    temp_list = []
    for path in files:
        with open(path) as f:
            tmp = json.load(f)
            if hash in tmp.keys():
                temp_list.append(sum(tmp[hash].values()))
            else:
                temp_list.append(0)
    dic[hash] = temp_list
print(dic)

print(list(range(1,367)))

# LINE PLOT
# one line / hashtag
# x: day of year
# y: # tweets

# scan though all data in outputs w/ mapping
# make dataset w/ all info needed for plot
# call appropriate matplotlib func to plot data

for key in dic.keys():
    x = list(range(1,367))
    y = dic[key]
    plt.plot(x,y,label=key)
plt.legend()
plt.xlabel('Day in 2020')
plt.ylabel('Number of Tweets')
plt.title('Frequency of Tweets Using Covid-Related Hashtags in 2020')

plt.savefig('alt_reduce.png')





# UPLOAD
# delete current contents of readme
# insert into readme brief explanation of project
#   includes the 4 generated png files
#   explanation suitable for future employer
