import MapReduce
import sys

mr = MapReduce.MapReduce()

'''
Problem 2

Implement a relational join as a MapReduce query
Your MapReduce query should produce the same result as this SQL query executed against an appropriate database.
SELECT * 
FROM Orders, LineItem 
WHERE Order.order_id = LineItem.order_id
'''

def mapper(record):
    # key: variable joined on (here, order_id)
    # value: entire record
    key = record[1]
    value = record
    mr.emit_intermediate(key, value)

'''
magic shuffle phase here
    1) COMBINE values of unique keys from ONE mapper output into one key-value pair
    2) COLLECT values of unique keys from ALL mapper outputs into one key-value pair
'''

def reducer(key, list_of_values):
    # key: order_id
    # list_of_values: list of tuples where order_id = key
    order_record = list_of_values.pop(0)
    for v in list_of_values:
        mr.emit(order_record + v)

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
