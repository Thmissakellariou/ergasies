#ΣΚΑΚΙΕΡΑ 8x8 ERGASIA 6
import random

vathmos2=int(0)
vathmos1=int(0)
length = int(8)
breath = int(8)
board = []

i = int(0)
for i in range(length):
   board.append(["◻"] * breath)
for x in board:
   grid = (" ".join(x))
   

x1=int(1)
y1=int(1)



maxy=int(7)
maxx=int(7)
miny=int(0)
minx=int(0)


for lp in range(100):

 x1=random.randint(0, 7)
 y1=random.randint(0, 7)
 board[x1][y1]="♖"


 x2=random.randint(0, 7)
 y2=random.randint(0, 7)

 board[x2][y2]="♗"
 x2arxiko=x2
 y2arxiko=y2

 x3=random.randint(0,7)
 y3=random.randint(0,7)
 board[x3][y3]="♛"
 y3arxiko=y3
 x3arxiko=x3
 if x1==x3 or y1==y3:
    vathmos1=vathmos1+1 
    
 
 while x2>minx and y2<maxy :
     
     x2=x2-1
     y2=y2+1
     
     if x2==x3 and y2==y3:
       vathmos1=vathmos1+1
       vathmos2=vathmos2+1
     else:
        x2=x2-1
        y2=y2+1
        
 x2=x2arxiko
 y2=y2arxiko 
 while x2<maxx and y2<maxy :
     
       x2=x2+1
       y2=y2-1
       
       if x2==x3 and y2==y3:
        vathmos1=vathmos1+1
        vathmos2=vathmos2+1
        
       else:
        x2=x2+1
        y2=y2-1
        
 x2=x2arxiko
 y2=y2arxiko   
 while x2>minx and y2> miny :
     
      x2=x2-1
      y2=y2-1
      
      if x2==x3 and y2==y3:
        vathmos1=vathmos1+1
        vathmos2=vathmos2+1
        
      else:
         x2=x2-1
         y2=y2-1
         
 x2=x2arxiko
 y2=y2arxiko
 while x2<maxx and y2>miny :
     
      x2=x2+1
      y2=y2+1
      
      if x3==x2 and y3==y2:
        vathmos1=vathmos1+1
        vathmos2=vathmos2+1
        
      else :
         x2=x2+1
         y2=y2+1
         
 x2=x2arxiko
 y2=y2arxiko   
 

 
 
 #GIA THN VASILISA
 #H KINISH POU KANEI STHN  EYTHEIA
 if x3==x1 or y3==y1:
    vathmos2=vathmos2+1
 if x3==x2 or y3==y2:
    vathmos2=vathmos2+1  
 #H KINHSH POU KANEI PLAGIA
 


 while x3>minx and y3<maxy :
     
     x3=x3-1
     y3=y3+1
     
     if x1==x3 and y1==y3:
       vathmos2=vathmos2+1
       
     else:
        x3=x3-1
        y3=y3+1
        
 x3=x3arxiko
 y3=y3arxiko 
 while x3<maxx and y3<maxy :
     
       x3=x3+1
       y3=y3-1
       
       if x1==x3 and y1==y3:
        vathmos2=vathmos2+1
        
       else:
        x3=x3+1
        y3=y3-1
        
 x3=x3arxiko
 y3=y3arxiko   
 while x3>minx and y3> miny :
     
      x3=x3-1
      y3=y3-1
      
      if x1==x3 and y1==y3:
        vathmos2=vathmos2+1
        
      else:
         x3=x3-1
         y3=y3-1
         
 x3=x3arxiko
 y3=y3arxiko
 while x3<maxx and y3>miny :
     
      x3=x3+1
      y3=y3+1
      
      if x3==x1 and y3==y1:
        vathmos2=vathmos2+1
        
      else :
         x3=x3+1
         y3=y3+1
         
 x3=x3arxiko
 y3=y3arxiko
 

 
 #den elexgetai gia ton aksiomatiko kathws evala na pairnoun kai oi duo ponto kateytheian
 
 
 
 
 board = []
 i = int(0)
 for i in range(length):
   board.append(["◻"] * breath)
 for x in board:
   grid = (" ".join(x))
print("GIA THN SKAKIERA 8X8 OI VATHMOI EINAI:") 
print("OI VATHMOI TOY PAIKTH1/(aksiomatikos,pyrgos) EINAI " ,vathmos1)
print("OI VATHMOI TOY PAIKTH2/(vasilisa) EINAI",vathmos2)  