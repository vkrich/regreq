import requests as rq
import re

a='https://stepic.org/media/attachments/lesson/24472/sample0.html' #input().strip()
b='https://stepic.org/media/attachments/lesson/24472/sample0.html' #input().strip()

reg = r'(<a href=\")(.{1,})(\">)(.{1,})'#find link
reg2= r'http.{1,}html'

links_from_a = re.findall(reg2, rq.get(a).text)
flag=False
for link in links_from_a:
    links_from_b = re.findall(reg2, rq.get(link).text)
    if b in links_from_b:
        print("Yes")
        flag=True
        break
if flag != True:
    print("No")



  







#
 


