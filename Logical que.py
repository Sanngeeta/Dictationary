def string_reverse(num):
    k=''
    i=len(num)
    while i>0:
        k +=num[i-1]
        i=i-1
    return(k)
print(string_reverse("1234abcd"))







# def string(str):
#     k=''
#     i=0
#     while i<len(str):
#         k+=str[i-1]
#         i=i+1
#     print(k)
# a=input("enter the any thing:-")
# var=list(str(a))
# string(var)    


#   x_digits = list(str(num1)) 