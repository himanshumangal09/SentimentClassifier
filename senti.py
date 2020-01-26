punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(word):
    newword = ''
    for char in word:
        #print(char)
        t=char
        if char in punctuation_chars:
            t = char.replace(char,'')
        newword = newword+t
    return newword
# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '/n':
            positive_words.append(lin.strip())
def get_pos(tweet):
    num = 0
    sentence = tweet.strip().split()
    #print(sentence)
    for word in sentence:
        nword = strip_punctuation(word.lower())
        if(nword in positive_words):
   # if sentence.lower() in positive_words:
            num+=1
    return num
negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
def get_neg(tweet):
    num = 0
    sentence = tweet.strip().split()
    #print(sentence)
    for word in sentence:
        nword = strip_punctuation(word.lower())
        if(nword in negative_words):
   # if sentence.lower() in positive_words:
            num+=1
    return num
tweet_file = open("project_twitter_data.csv","r")
datalines = tweet_file.readlines()
fieldnames = datalines[0]
result_file = open("resulting_data.csv","w")
result_file.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
result_file.write('\n')
#print(fieldnames)
for row in datalines[1:]:
    data = row.strip().split(',')
    tweet_text = data[0]
    retweet_count = data[1]
    reply_count = data[2]
    pos_score = get_pos(tweet_text)
    neg_score = get_neg(tweet_text)
    net_score = pos_score - neg_score
    #print(data)
    totalstring = '{},{},{},{},{}'.format(retweet_count,reply_count,pos_score,neg_score,net_score)
    result_file.write(totalstring)
    result_file.write('\n')
    
    