import requests
with open ('C:\\Users\\on1xa\\Downloads\\dataset_3378_3.txt', 'r') as x:
    x=x.read().strip()
lastword="We"
lst=[[""]]
r=requests.get(x)
link="https://stepic.org/media/attachments/course67/3.6.3/"
nextlink=link+r.text
while lastword != lst[0][0]:
    lst.clear()
    r1 = requests.get(nextlink)
    nextlink=link+r1.text
    lst.insert(0, r1.text.split())
print(r1.text)
