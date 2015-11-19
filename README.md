Insight Data Engineering - Coding Challenge
===========================================================

###### Google style guide: https://google.github.io/styleguide/pyguide.html
###### PEP styling: https://www.python.org/dev/peps/pep-0008/
###### PyLint Score: 
###### External dependencies/libraries: None

This program implements two features:

1. Clean and extract the text from the raw JSON tweets that come from the Twitter Streaming API, and track the number of tweets that contain unicode.

    - Unicode different results based on machine, native encoding, version of python. 
    - I am using python 2. Attemps were made to make it compatible with all version of python
    - Multiple methods were tried for "unicode-containing-tweet" for most efficient way to identify unicode
    - json loads handles much of character replacement automatically 
    - To avoid catching a tweet which contained a "unicode" as text, the original tweet was first decoded with (unicode_escape) and then searched for native unicode. [not fully tested]
    - Tested on ipython notebook, spyder and terminal
    - Unit Tests: 
    - Tested on Unix(MacOSX) and Linux
    - Not tested with Streaming API 





2. Calculate the average degree of a vertex in a Twitter hashtag graph for the last 60 seconds, and update this each time a new tweet appears.



    - Every tweets needs to be processed even if it has no hashtags, (as stated in FAQ)
    - If there is 1 or no hashtags in the tweet, rolling average is 0 and no new node is added to the graph
    - An alternate version of this program has been provided in the src folder using a separate 'Graph' class which calculates edges, adds vertices dynamically, and calculates degree of a vertex
    - Tested on ipython notebook, spyder and terminal
    - Unit Tests: 
    - Tested on Unix(MacOSX) and Linux
    - Not tested with Streaming API 







NOTE: These programs were implemented in very short period due to recent cahnges in my schedule. Hence not extensively tested. Code readability and efficiency can be improved with using classes especially for the graph strucure. If any issues with code, please reach out at: mudit.uppal[at]live[dot]com 


#### Repo directory structure

	├── README.md  
	├── run.sh  
	├── src  
	│   ├── average_degree.py  
	│   └── tweets_cleaned.py  
	├── tweet_input  
	│   └── tweets.txt  
	└── tweet_output  
	    ├── ft1.txt  
	    └── ft2.txt  

