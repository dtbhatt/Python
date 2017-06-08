# #Prints all odds and even between 0 and 2000

# def oddEven():
#     for i in range(1, 2000):
#         if (i % 2 == 0):
#             print "Number is ", i, ". This is an even number."
#         else :
#             print "Number is ", i, ". This is an odd number."

# oddEven()


# #Multiply by 5
def multiply(arr,int):
    multi = []
    for i in arr:
        product = i * int
        multi.append(product)
    print multi
    return multi


multiply([1,2,3,4], 3)

# Hacker Challenge

inList = [2,4,5]

def layered_multiples(arr):
    temp = []
    new_array = []

    for i in arr:
        for j in range(0, i):
            temp.append(1)

        new_array.append(temp)
        temp = []

    return new_array

new_list = layered_multiples(multiply(inList, 3))
print new_list