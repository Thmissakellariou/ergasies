#askhsh11
import math
from urllib.request import Request, urlopen
import json
from collections import Counter
rand= [None] * 20 
req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()
data=json.loads(data)
rand[19]=data['randomness']
 
y=[]

m=data['round']-20
n=data['round']-1

while m<n:
  for li in range(0,19):
   req = Request('https://drand.cloudflare.com/public/'+str(m), headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
   data = urlopen(req).read()
   data=json.loads(data)
   if rand[li]==None:
    rand[li]=data['randomness']
    break
  m=m+1
    
y="".join(rand)

def entropy(y):
  p,lns=Counter(y) , float(len(y))
  return -sum(count/lns *math.log(count/lns,2) for count in p.values())

print("H ENTROPIA EINAI:",entropy(y))
#isws exw xrisimopoisei kapoia parapanw vivliothiki apla den tis evgala kalou kakou
#argei kapoia deyterolepta na ypologisei thn entropia