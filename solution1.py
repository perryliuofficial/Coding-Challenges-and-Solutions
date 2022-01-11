def find_outlier(integers):
    even = [i for i in integers if i % 2 == 0] # add even numbers to list
    odd = [i for i in integers if i % 2 != 0] # add odd numbers to list
    
    if len(even) > len(odd): # if there are more even than odd numbers then return odd
        return odd[0]
    else: # if there are more odd than even numbers then return even
        return even[0]

print(find_outlier([2, 4, 6, 8, 10, 3]))
print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))