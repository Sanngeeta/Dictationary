# {
#     'sonu':85,
#     'Kartik':90,
#     'Deepak':96,
#     'Aman':76,
#     'Somesh':60,
#     'Umesh':85,
#     'Amarpal':70,
#     'Roshan':57,
#     'Riyaz':98,
#     'Shabid':56
# } 


dic={}
num=int(input("enter the number:"))
for i in range(num):
    a=input("enter the key:")
    b=input("enter the value:")
    dic.update({a:b})
print(dic)    
