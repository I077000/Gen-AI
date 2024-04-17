# Create an empty tuple

empty_tuple = ()
print(type(empty_tuple))

non_empty_tuple = ("s","d")
print(type(non_empty_tuple))

sister_tuple =('a','b')
brother_tuple = ('A','B')
sibling_tuple =sister_tuple+brother_tuple
print(sibling_tuple)
print('A' in brother_tuple)