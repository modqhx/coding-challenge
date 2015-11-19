###############################################################################
# Example of program that cleans and calculates the number of unicode tweets

# Author: Mudit Uppal (www.muppal.com)
# Email: mudit.uppal@yahoo.com
# Tested on Unix, Linux 
# time taken: 

# Google style guide: https://google.github.io/styleguide/pyguide.html
# PEP styling: https://www.python.org/dev/peps/pep-0008/
# PyLint Score: 
###############################################################################

#!/usr/bin/env python
# coding: utf-8

from __future__ import division
import json
import string
import sys
from myfunctions import *

INPUT_FILE = sys.argv[1]
OUTPUT_FILE = sys.argv[2]
with open(OUTPUT_FILE, 'w+') as ft1:
    with open(INPUT_FILE, 'r') as tweetFile:
        
        number_unicode = 0
        hashTags = []
        for line in tweetFile:
            try:
                tweet_list = []  #empty list for tweet text
                tweet = json.loads(line, encoding='utf-8') #json loads handles much of the escape \
                                                           #characters automatically
                tweetText = tweet.get(u'text').encode('utf-8')
                tweetTime = tweet.get(u'created_at').encode('utf-8')
    
                try:
                    tweetText.decode('ascii')
                except UnicodeDecodeError:
                    #print "----NOT an ascii-encoded unicode string----"
                    #So now I know the string has "unicode in it". If the unicode contains one the escape 
                    #characters, replace them
                    number_unicode += 1
                    
                else:
                    # print "----an ascii-encoded unicode string----"  
                    # no exception raised here. Operation that can throw IOerror would go here
                    #print 'Some second operation you were trying to do caused an IO error'
                    continue
                    
                finally:
                    cleanedTweet = remove_non_ascii(tweetText).replace('\n', ' ').replace('\t', ' ').replace('\\\\', '\\')
                    cleanedTweet = remove_whitespace_escape(cleanedTweet)
                    hashTags = extract_hashTags(cleanedTweet) # a list of of all DISTINCT hashtags in the tweet pylint: disable
                    hashTags = [t.translate(None, string.punctuation) for t in hashTags]
                    hashTags = filter(None, hashTags) #remove useless chars. filter returns a list in Python 2
                    #cleanList = re.sub('[^A-Za-z0-9]+', '', cleanList)
    

                    ft1.write(cleanedTweet + ' (timestamp: ' + tweetTime + ')' + '\n')
                    #return cleanedTweet
                    #print cleanedTweet

            except:
                continue
        
        ft1.write('\n' + str(number_unicode) + ' tweets contained unicode.')
