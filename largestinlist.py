#largest element in list

#function
def largest(list):
    large= list[0]
    for i in list:
        if i>large:
            large=i
    return large

#list
list=[10, 20, 5, 8, 25, 3]
print("largest in ",list,"is")
print(largest(list))

