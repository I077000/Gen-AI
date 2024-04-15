# Declare an empty list

empty_list =[]

non_empty_list = [1,2,3,4,5]

print("length of my list >>>"+ str(len(non_empty_list)))

# Get the first item, the middle item and the last item of the list

print(non_empty_list[0])
print(non_empty_list[len(non_empty_list)-1])
middle_index = (0 + (len(non_empty_list)-1))//2
print(non_empty_list[middle_index])

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

mixed_list = ['shrijan', 35, 5.7 , True, 'blore']

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle" , "Amazon"]
it_companies.append("SAP")
print(str(len(it_companies)))
print(it_companies[0])
print(it_companies[len(it_companies)-1])
middle_index = 0+(len(it_companies)-1)//2



print(it_companies[middle_index])

it_companies.insert(middle_index,"Nvidia")
print(it_companies)
print(it_companies[middle_index])
print('#;'.join(it_companies))
it_companies.sort()
print(it_companies)
it_companies.reverse()
print(it_companies)
print(it_companies[:3])
print(it_companies[-3:])

