#askhsh 5
from collections import Counter
from posixpath import split

f = open("tales.txt", "r")


theFullText = f.read()
x = theFullText.lower()
x=x.split()
theFullText=theFullText.lower()
theFullText=theFullText.split()

y=[]
y1=[]




newlist=(x)
newlist2=(x)
print(len(newlist))
for li in range (len(newlist2)):
  y.append(theFullText[li][:2])
  if len(theFullText[li])>2:
    y1.append(theFullText[li][:3])
  



Counter1= Counter(x)
dhmofilesterh = Counter1.most_common(10) #ελεγξα και την 11 και ειχε χρησιμοποιηθει λιγοτερο απο την 10 οποτε κρατησα αυτες.
print("OI DEKA DHMOFILESTERES EINAI:",dhmofilesterh)

Counter2=Counter(y)
dhmofilesterh2 = Counter2.most_common(3)
print("TA TRIA DHMOFILESTERA 2 PRWTA GRAMMATA EINAI:",dhmofilesterh2)
    


Counter3=Counter(y1)
dhmofilesterh3 = Counter3.most_common(3)
print("TA TRIA DHMOFILESTERA 3 PRWTA GRAMMATA EINAI:",dhmofilesterh3)