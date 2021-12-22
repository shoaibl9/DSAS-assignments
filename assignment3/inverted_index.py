import MapReduce
import sys

mr = MapReduce.MapReduce()

'''
Problem 1

Create an Inverted index. 
Given a set of documents, an inverted index is a dictionary
where each word is associated with a list of the document identifiers in which that word appears.
'''

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    words = value.split()
    for w in words:
      mr.emit_intermediate(w, key)

'''
magic shuffle phase here
    1) COMBINE values of unique keys from ONE mapper output into one key-value pair
    2) COLLECT values of unique keys from ALL mapper outputs into one key-value pair
'''

def reducer(key, list_of_values):
    # key: word
    # value: list of document identifiers
    '''
    new_list = []
    for i in list_of_values: # remove duplicates (method 1)
      if i not in new_list:
        new_list.append(i)
    '''

    new_list = list(set(list_of_values)) # remove duplicates (method 2)

    total = []

    for v in new_list:
      total.append(v)
    mr.emit((key, total))

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
