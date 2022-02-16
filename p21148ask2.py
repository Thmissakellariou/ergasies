#askhsh 2

import random

vimata=int(0)
mikrokapaki=int(1)
mesaiokapaki=int(2)
megalokapaki=int(3)




board = [[0,0,0],
            [0,0,0],
            [0,0,0]]

      




for ln in range(100):
  plithosmikrwn=int(9)
  plithosmesaiwn=int(9)
  plithosmegalwn=int(9) 
 
  board = [[0,0,0],
            [0,0,0],
            [0,0,0]]
    
  niki=0
  
  while niki==0:
    x=random.randint(1,3)
    if x==1 and plithosmikrwn>=1:
     x1=random.randint(0,2)
     y1=random.randint(0,2)    
     if board[x1][y1] ==0:
      board[x1][y1]=1 
      plithosmikrwn=plithosmikrwn-1
      vimata=vimata+1
    elif x==2 and plithosmesaiwn>=1:
      x1=random.randint(0,2)
      y1=random.randint(0,2)  
      if board[x1][y1] ==0 or board[x1][y1] ==1 :
        board[x1][y1]=2
        plithosmesaiwn=plithosmesaiwn-1
        vimata=vimata+1  
    elif x==3 and plithosmegalwn>=1:
        x1=random.randint(0,2)
        y1=random.randint(0,2)
        if board[x1][y1]==1 or board[x1][y1]==2 or board[x1][y1]==0 :
            board[x1][y1]=3
            plithosmegalwn=plithosmegalwn-1
            vimata=vimata+1
           
    if ((board[0][0]==board[0][1]==board[0][2]==1 ) or (board[0][0]==board[0][1]==board[0][2]==2)or (board[0][0]==board[0][1]==board[0][2]==3)):
      niki=1
    if ((board[1][0]==board[1][1]==board[1][2]==1 ) or (board[1][0]==board[1][1]==board[1][2]==2)or (board[1][0]==board[1][1]==board[1][2]==3)):
       niki=1
    if ((board[2][0]==board[2][1]==board[2][2]==1 ) or (board[2][0]==board[2][1]==board[2][2]==2)or (board[2][0]==board[2][1]==board[2][2]==3)):
       niki=1   
    if ((board[0][0]==board[1][0]==board[2][0]==1 ) or (board[0][0]==board[1][0]==board[2][0]==2)or (board[0][0]==board[1][0]==board[2][0]==3)):
       niki=1   
    if ((board[0][1]==board[1][1]==board[2][1]==1 ) or (board[0][1]==board[1][1]==board[1][1]==2)or (board[0][1]==board[1][1]==board[2][1]==3)):
       niki=1   
    if ((board[0][2]==board[1][2]==board[2][2]==1 ) or (board[0][2]==board[1][2]==board[2][2]==2)or (board[0][2]==board[1][2]==board[2][2]==3)):
       niki=1  
    if ((board[0][0]==board[1][1]==board[2][2]==1) or (board[0][0]==board[1][1]==board[2][2]==2) or (board[0][0]==board[1][1]==board[2][2]==3)):
       niki=1  
    if ((board[0][2]==board[1][1]==board[2][0]==1) or  (board[0][2]==board[1][1]==board[2][0]==2) or (board[0][2]==board[1][1]==board[2][0]==3)):
       niki=1
    if ((board[0][0]==1 and board[0][1]==2 and board[0][2]==3 ) or (board[0][0]==3 and board[0][1]==2 and board[0][2]==1 )): 
      niki=1
    if ((board[1][0]==1 and board[1][1]==2 and board[1][2]==3 ) or (board[1][0]==3 and board[1][1]==2 and board[1][2]==1 )): 
      niki=1
    if ((board[2][0]==1 and board[2][1]==2 and board[2][2]==3 ) or (board[2][0]==3 and board[2][1]==2 and board[2][2]==1 )): 
      niki=1
    if ((board[0][0]==1 and board[1][0]==2 and board[2][0]==3 ) or (board[0][0]==3 and board[1][0]==2 and board[2][0]==1 )): 
      niki=1
    if ((board[0][1]==1 and board[1][1]==2 and board[2][1]==3 ) or (board[0][1]==3 and board[1][1]==2 and board[2][1]==1 )): 
      niki=1  
    if ((board[0][2]==1 and board[1][2]==2 and board[2][2]==3 ) or (board[0][2]==3 and board[1][2]==2 and board[2][2]==1 )): 
      niki=1 
    if ((board[0][0]==1 and board[1][1]==2 and board[2][2]==3 ) or (board[0][0]==3 and board[1][1]==2 and board[2][2]==1 )): 
      niki=1  
    if ((board[0][2]==1 and board[1][1]==2 and board[2][0]==3 ) or (board[0][2]==3 and board[1][1]==2 and board[2][0]==1 )): 
      niki=1  
  




   
    
    
    
    
    
    
    
    
    
    
    
         
        






mesos_oros_vimatwn=vimata/100
print("O mesos oros vimatwn einai:",mesos_oros_vimatwn)
     
      

    
    