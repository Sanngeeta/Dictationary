dic={'bijender':45,'deepak':60,'param':20,"anjili":30,"roshini":50}
# sorted(dic)
# print(sorted(dic))
# print(dic,reverse=True)

dict1={}

for i in dic:
    k=dic[i]
    for i in dic:
        a= dic[i]
        if k > a:
            dict1[i]= a
print(dict1)            

        