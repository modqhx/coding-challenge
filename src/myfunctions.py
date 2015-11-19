##################################################################################
# Methods used in both programs
# Author: Mudit Uppal (www.muppal.com)
# Email: mudit.uppal@yahoo.com
# Google style guide: https://google.github.io/styleguide/pyguide.html
##################################################################################

def remove_non_ascii(input_tweet):
    """
    Takes an input string and returns only ASCII between [32 and 127]
    """
    filtered = (i for i in input_tweet if 32 <= ord(i) <= 127) #returns an integer representing the Unicode code point of the character
    return ''.join(filtered)

def remove_whitespace_escape(input_tweet):
    """
    Removes any extra and leading whitespaces including whotespace escape
    """
    return ' '.join(input_tweet.split())

def extract_hashTags(input_tweet):
    """
    Takes an input as string and finds all hastags in the string.
    Does not include hashtags which are inside a url
    """
    return list(set(tweet[1:] for tweet in input_tweet.split() if tweet.startswith('#')))

def remove_punctuation(input_tweet):
    """
    Takes an input string and Removes all punctuation defined in default string.punctuation
    """
    punc = string.maketrans("","")
    return input_tweet.translate(punc, string.punctuation)

def generate_edges(graph):
    """
    Takes in a graph dictinoary as input and creates a list of all edges in the graph
    """
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))
    return edges

'''
    def identify_unicode(input_tweet):
    hasUni = re.search(r'\u[0-9A-Fa-f]{4}',input_tweet)
    if hasUni:
    return "text contains unicode"
    else:
    return "text does not contains unicode"
    
    def remove_escape_chars(input_tweet):
    filtered = input_tweet.replace(r'\/', '/').replace(r"\\\\", "/").replace(r"\\'","'").replace(r"\\n", " ").\
    replace(r"\\t", " ")
    return filtered

'''
