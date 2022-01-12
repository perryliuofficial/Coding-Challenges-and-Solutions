# This version breaks down the logic step by step. As you can see this is not very legible and is longer than necessary.

def find_outlier(integers):
    even=[]
    odd=[]
    return_number=str
    for i in integers:
        if (i % 2) == 0: # if number is even
            if even: # and if there's already an even number (hence we need to return odd)
                if odd: # if we've already found the odd number
                    return odd[0] # return the odd number
                else: # if we haven't found the odd number we remember that we need to return odd
                    return_number="odd"
            else: # and if this is the first even number
                even.append(i) # save it
                if return_number == "even": # if we previously concluded that we need to return an even number
                    return even[0] # then return
        else: # if number is odd
            if odd: # and if there's already an odd number (hence we need to return even)
                if even: # if we've already found the even number
                    return even[0] # return the even number
                else: # if we haven't found the odd number we remember that we need to return odd
                    return_number="even"
            else: # and if this is the first odd number
                odd.append(i) # save it
                if return_number == "odd": # if we previously concluded that we need to return an odd number
                    return odd[0] # then return

print(find_outlier([2, 4, 6, 8, 10, 3]))
print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))