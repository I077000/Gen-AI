# Filter only negative and zero in the list using list comprehension
# numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

numbers = [-4, -3, -2, -1, 0 ,2,4,6]

negative_zero_list = [x for x in numbers if x <=0]
print(negative_zero_list)

"""
Flatten the following list of lists of lists to a one dimensional list :

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

output
[1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

list_of_list = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
print(list_of_list)
flatten_list_level1 = [x[0]  for x in list_of_list]
print(flatten_list_level1)
flatten_list_level2 = [number  for row in flatten_list_level1 for number in row]
print(flatten_list_level2)



"""
Flatten the following list to a new list:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output:
[['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
"""

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
countries1 = [x[0] for x in countries]
country_base = [country for country2 in countries1 for country in country2 ]
print(country_base)