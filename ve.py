   from itertools import zip_longest

   json1 = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
   json2 = [{'id': 101, 'age': 30}]

   zipped_pairs = zip_longest(json1, json2, fillvalue={})

   filtered_pairs = [(item1, item2) for item1, item2 in zipped_pairs if item1 and item2]

   print(filtered_pairs)
   