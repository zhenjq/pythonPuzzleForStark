def f(param_list,num):
    ptr = 0
    #since the list has already postively sorted,retrun -1 if
    #num < list at index 0
    if(num<=param_list[0]):
        return -1
    #if num > the last index of the postive sorted list function
    #will return list at last index
    elif(num>param_list[len(param_list)-1]):
        return param_list[len(param_list)-1]
    else:
        while(param_list[ptr]<num):
            ptr += 1
            return param_list[ptr-1]


list1 = [1,2,3,4,5,6,7,8,9,10]
result = f(list1,2)
print(result)
