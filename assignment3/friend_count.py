import MapReduce
import sys

mr = MapReduce.MapReduce()

"""
Problem 3

Consider a simple social network dataset consisting of a set of key-value pairs (person, friend)
representing a friend relationship between two people. 
Describe a MapReduce algorithm to count the number of friends for each person.
"""

def mapper(record):
    # key: personA
    # value: friend of personA
    key = record[0]
    value = record[1]
    mr.emit_intermediate(key, 1)

'''
magic shuffle phase here
    1) COMBINE values of unique keys from ONE mapper output into one key-value pair
    2) COLLECT values of unique keys from ALL mapper outputs into one key-value pair
'''

def reducer(key, list_of_values):
    # key: personA
    # value: list of friend counts
    total = 0
    for v in list_of_values:
      total += v
    mr.emit((key, total))

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
