import sys
import json

def hw():
    print('Hello, world!')

def lines(fp):
    print(str(len(fp.readlines())))

def createDict(sent_file):
    afinnfile = open("AFINN-111.txt") # replace with open(sent_file)?
    scores = {}
    for line in afinnfile: # why didnt we have to do afinnfile.readlines()?
        term, score = line.split("\t")
        scores[term] = int(score)
    #print(scores.items())
    return scores

# useful:
# lines = file1.readlines()
# for line in lines:
#   for word in line.split():
#       do stuff

# note:
# my output.txt is not JSON formatted
# instead, each line is this string:
# json_response['data']['text'].replace("\n", "")

def scoreTweets(scores, tweet_file):
    # read each tweet separately (use given sample file)
    # read each word in text
    # if word in scores: scores += scores[word]
    # print score for tweet
    # the nth line of the output file should correspond to the nth tweet
    score = 0
    count = 1
    lines = tweet_file.readlines()

    for line in lines:
        # use below if working with single-line json object
        #json_response = json.loads(line)
        #text = json_response['text']
        #for word in text.split():
        for word in line.split():
            if word in scores:
                score += scores[word]
        print("Score for line " + str(count) + ": " + str(score))
        score = 0
        count += 1

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    scores = createDict(sent_file)
    scoreTweets(scores, tweet_file)

    #hw()
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
