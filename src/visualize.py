#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
parser.add_argument('--output',required=True)
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib.pyplot as plt
import numpy as np

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
'''
countdown = 0
for k,v in items:
    if countdown < 10:
        print(k,':',v)
        countdown += 1
'''

# plot top 10
'''
print("items[1]=", items[1])
print("items[0]=", items[0])
print("items=", items)
'''
things = []
vals = []
for k, v in items:
    things = np.append(things, k)
    vals = np.append(vals, v)
# print("things=", things[:10])
# print("vals=", vals[:10])
# print("things[:10:-1]=", things[:10:-1])

things2 = things[:10]
vals2 = vals[:10]
plt.bar(things2[::-1], vals2[::-1])

if args.key[-1] == 's':
    plt.title("Tweets in 2020 (EN)")
    print("EN")
else:
    plt.title("Tweets in 2020 (KR)")

if things[0] == 'en':
    plt.xlabel("Language")
else:
    plt.xlabel("Country")

plt.ylabel("Number of Tweets")
plt.savefig(str(args.output) + '.png')
