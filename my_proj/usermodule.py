s=input()
s=s+" "
cnt=1
counter=1
for i in s:
  if counter!=0 and s[counter]==s[counter-1]:
    cnt+=1    
  elif counter!=len(s):
    print(s[counter-1], end='')
    print(cnt)
    cnt=1
  
  if counter!=len(s)-1:
    counter+=1
  
  