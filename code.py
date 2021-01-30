#Question:- to count charactor in string which occures only once?
st="aabasgdhbc"
count=0
st=sorted(st)
for i in range(0,len(st)-1):
    if(st[i]!=st[i+1] and i==0):
        count+=1
    elif(st[i]!=st[i+1] and st[i-1]!=st[i]):
        count+=1
    elif(i==len(st) and st[i-1]!=st[i]):
        count+=1
print(count)
        
