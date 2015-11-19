###########################################################################
# Example of program that calculates the average degree of hashtags

# Author: Mudit Uppal (www.muppal.com)
# Email: mudit.uppal@yahoo.com

# Tested on Unix, Linux 
# time taken: 
# Google style guide: https://google.github.io/styleguide/pyguide.html
# PEP styling: https://www.python.org/dev/peps/pep-0008/
# PyLint Score: 
############################################################################

#!/usr/bin/env python
# coding: utf-8

from __future__ import division
import json
from datetime import datetime
import string
import sys
from myfunctions import *


INPUT_FILE = sys.argv[1]
OUTPUT_FILE = sys.argv[2]
with open(OUTPUT_FILE, 'w+') as ft2, open(INPUT_FILE, 'r') as tweetFile:
    
    number_unicode = 0
    hashTags = []
    timeList = []
    graphdict = dict()
    for line in tweetFile:
        try:
            tweet_list = []  #empty list for tweet text
            tweet = json.loads(line, encoding='utf-8') #json loads handles much of the escape characters automatically
            tweetText = tweet.get(u'text').encode('utf-8')
            tweetTime = tweet.get(u'created_at').encode('utf-8')
            cleanedTweet = remove_non_ascii(tweetText).replace('\n', ' ').replace('\t', ' ').replace('\\\\', '\\')
            cleanedTweet = remove_whitespace_escape(cleanedTweet)
            hashTags = extract_hashTags(cleanedTweet) # a list of of all DISTINCT hashtags in the tweet
            hashTags = [t.translate(None, string.punctuation) for t in hashTags]
            hashTags = filter(None, hashTags) #remove useless chars. filter returns a list in Python 2
            #cleanList = re.sub('[^A-Za-z0-9]+', '', cleanList)
            timeFmt = '%a %b %d %H:%M:%S +0000 %Y'
            #parseDate = datetime.strptime(timestamp, timeFmt)
            hashTags.append(datetime.strptime(tweetTime, timeFmt)) # a dynamic list

            #print hashTags
            timeList.append(hashTags[-1]) #list of only times
            hashTagsList = hashTags[:-1] #list of only hashTags
            lengthTimeList = len(timeList) #static
            
            if lengthTimeList > 0: #average starting after first tweet
                #for i in range(lengthTimeList):
                deltaT = timeList[-1] - timeList[0] #assuming the tweet which come later has a later 
                                                    #timestamp; although streaming API can behave different
                if abs(deltaT.seconds) < 60:    #60 second window
                    #dictionary to create a tree graph
                    hashSet = set(hashTags[:-1]) #avoid duplicates
                    if len(hashSet) > 1: # atleast 2 hashtags;single hashtags does not make any node
                        for key in hashSet: #loop thru all hashtags
                            if not graphdict.has_key(key): #new key
                                graphdict[key] = hashTags[:-1]

                            else: #key already exists
                                a = set(graphdict[key])
                                a.update(hashSet)
                                graphdict[key] = list(a)

                            graphdict[key].remove(key) #self connection is not counted
                            
                        count = sum(len(v) for v in graphdict.itervalues())
                        average = count/len(graphdict)
                        #edges = generate_edges(graphdict)
                    else:
                        #if set is empty or contains single hashtag
                        average = 0

                    ft2.write(str("{0:.2f}".format(average)) + '\n')

                else:
                    hashTags = []
                    timeList = []
                    graphdict.clear()

        except:
            continue
