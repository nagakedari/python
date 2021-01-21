#sets doesn't care about the order unlike lists and tuples. it will not have duplicates
coureses = {'history', 'math', 'physics', 'compsci', 'math'}
print(coureses)
print('math' in coureses)
#finding common elements b/w 2 sets
coureses = {'history', 'math', 'physics', 'compsci'}
artcoureses = {'history', 'art', 'desgin', 'compsci'}
print(coureses.intersection(artcoureses))
#Finding difference
print(coureses.difference(artcoureses))
print(artcoureses.difference(coureses))
#all the courses among both
print(coureses.union(artcoureses))

#creating empty set
empty_set = set()