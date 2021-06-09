# Ek code likhiye jo dictionary ki 3 highest value print karaye.
# [58,56,100]




my_dict = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20
    }
list2_key=[]
list1_key=[]

for i in range(3):
    max = 0
    for x in my_dict:
        if max<my_dict[x]:
            max=my_dict[x]
            key=x
    list2_key.append(max)
    list1_key.append(key)
    my_dict.pop(key)

print(list2_key )
print(list1_key)

    







# for i in my_dict.values():
#     if my_dict>values:
        