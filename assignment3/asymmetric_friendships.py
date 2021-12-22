import MapReduce
import sys

mr = MapReduce.MapReduce()

"""
Problem 4

The relationship "friend" is often symmetric, meaning that if I am your friend, you are my friend.
Implement a MapReduce algorithm to check whether this property holds. 
Generate a list of all non-symmetric friend relationships.
"""

def mapper(record):
    # key: personA/personB  pair
    # value: count of pair
    temp = [record[0], record[1]]
    pair = tuple(sorted(temp))
    mr.emit_intermediate(pair, 1)
'''
magic shuffle phase here
    1) COMBINE values of unique keys from ONE mapper output into one key-value pair
    2) COLLECT values of unique keys from ALL mapper outputs into one key-value pair
'''

def reducer(key, list_of_values):
    # key: personA/personB  pair
    # value: count of pairs
    if len(list_of_values) == 1:
        mr.emit((key[0], key[1]) )
        mr.emit((key[1], key[0]) )

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
