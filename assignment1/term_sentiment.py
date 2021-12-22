import sys

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def createDict(sent_file):
    # adds pre-existing terms below
    afinnfile = open("AFINN-111.txt") # replace with open(sent_file)?
    scores = {}
    for line in afinnfile: # why didnt we have to do afinnfile.readlines()?
        term, score = line.split("\t")
        scores[term] = int(score)
    
    #add non-existing terms below

    #make dictionary for each unique term in entire file not in dict
    #that dictionary will hold term and its key will be net sentiment
    #, where net sentiment is defined as the average of the total sentiment of each line it is found in / words in that line
    #combine two dictionaries and output final dict

    #print(scores.items())
    #return scores

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    dict = createDict(sent_file)

    hw()
    lines(sent_file)
    lines(tweet_file)

if __name__ == '__main__':
    main()
