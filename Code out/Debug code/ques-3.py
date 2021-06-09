# Niche ek program hai jisme keys 1 se lekar 15 ke beech main hai aur values keys ka square hai jaise ki. Output kuch esha hona chahiye :- ab aapko is program ko theek karna hai.
 
c=0
dict1={}
for i in range(1,16):
    i=i*i
    c=c+1
    dict1.update({c:i})
print(dict1)  

