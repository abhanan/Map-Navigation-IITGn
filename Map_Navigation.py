c=0
from pylab import*
from matplotlib.pyplot import figure, show
fig = figure()
def map():
 x1=np.linspace(0,5,200)
 y1=x1*c
 plot(x1,y1)

 x2=np.linspace(5,10,200)
 y2=x2*c
 plot(x2,y2)

 x3=np.linspace(10,15,200)
 y3=x3-10
 plot(x3,y3)

 x4=np.linspace(10,15,200)
 y4=-x4+20
 plot(x4,y4)

 x5=np.linspace(5,10,200)
 y5=np.linspace(0,10,200)
 plot(x5,y5*0+10)
 
 x6=np.linspace(0,5,200)
 y6=np.linspace(0,10,200)
 plot(x6,y6*0+10)

 x7=np.linspace(0,5,200)
 y7=np.linspace(5,10,200)
 plot(x7*c,y7)

 x8=np.linspace(0,5,200)
 y8=np.linspace(0,5,200)
 plot(x8*c,y8)

 x9=np.linspace(0,5,200)
 y9=np.linspace(0,10,200)
 plot(x9,y9*0+5)

 x10=np.linspace(5,10,200)
 y10=np.linspace(0,10,200)
 plot(x10,y10*0+5)

 x11=np.linspace(10,15,200)
 y11=np.linspace(0,10,200)
 plot(x11,y11*0+5)

 x12=np.linspace(0,5,200)
 y12=x12
 plot(x12,y12)

 x13=np.linspace(0,5,200)
 y13=-x13+10
 plot(x13,y13)

 x14=np.linspace(5,10,200)
 y14=-x14+10
 plot(x14,y14)

 x15=np.linspace(5,10,200)
 y15=-x15+15
 plot(x15,y15)

 x16=np.linspace(0,5,200)
 y16=np.linspace(0,5,200)
 plot(x16*0+5,y16)

 x17=np.linspace(0,5,200)
 y17=np.linspace(5,10,200)
 plot(x17*0+5,y17)

 x18=np.linspace(0,5,200)
 y18=np.linspace(0,5,200)
 plot(x18*0+10,y18)

 annotate('Ashok Vihar', xy=(0,0), xytext=(-4,-2),
          arrowprops=dict(facecolor='black',width=1,headwidth=4, shrink=0.05))
 annotate('NBH', xy=(0,5), xytext=(-3,5),
          arrowprops=dict(facecolor='black',width=1,headwidth=4, shrink=0.05))
 annotate('L Block', xy=(0,10), xytext=(-4,11),
          arrowprops=dict(facecolor='black',width=1,headwidth=4, shrink=0.05))
 annotate('FootBall Ground', xy=(5,10), xytext=(4,13),
          arrowprops=dict(facecolor='black',width=1,headwidth=4, shrink=0.05))
 annotate('Shed 4', xy=(10,10), xytext=(11,12),
          arrowprops=dict(facecolor='black',width=1,headwidth=4, shrink=0.05))
 annotate('Shed 5', xy=(15,5), xytext=(17,5),
          arrowprops=dict(facecolor='black',width=1,headwidth=4, shrink=0.05))
 annotate('Shed 3', xy=(10,0), xytext=(10,-2),
          arrowprops=dict(facecolor='black',width=1,headwidth=4, shrink=0.05)) 
 annotate('Shed 1', xy=(5,0), xytext=(5,-2),
          arrowprops=dict(facecolor='black',width=1,headwidth=4, shrink=0.05))
 annotate('B.B.C.', xy=(5,5), xytext=(6,3),
          arrowprops=dict(facecolor='black',width=1,headwidth=4, shrink=0.05))
 annotate('Shed 2', xy=(10,5), xytext=(11,6),
          arrowprops=dict(facecolor='black',width=1,headwidth=4, shrink=0.05))
 annotate('10', xy=(2.5,-1))
 annotate('9', xy=(7.5,-1))
 annotate('7', xy=(12.5,2))
 annotate('12', xy=(12.5,7.8))
 annotate('1', xy=(7.5,10))
 annotate('17', xy=(2.5,10))
 annotate('4', xy=(-1,7.5))
 annotate('14', xy=(-1,2.5))
 annotate('2', xy=(2.5,5))
 annotate('8', xy=(7.5,5))
 annotate('15', xy=(12.5,5))
 annotate('14', xy=(2.5,2.2))
 annotate('10', xy=(2.5,7.2))
 annotate('18', xy=(5,2))
 annotate('11', xy=(5,7))
 annotate('20', xy=(7,2))
 annotate('16', xy=(7.5,7.5))
 annotate('3', xy=(10,2.2))
 annotate('IITGn Map ', xy=(2,22))

 xlim(-6,25)
 ylim(-6,25)
 
 
def path1(i):
    
    if(i=='shed1'):
     x1=np.linspace(0,5,200)
     y1=x1*c
     plot(x1,y1,linewidth=4)
     annotate('Distance Travelled = 10', xy=(0,18))
          
    

    elif(i=='shed3'):
     x1=np.linspace(0,5,200)
     y1=x1*c
     plot(x1,y1,linewidth=4)
    
     x2=np.linspace(5,10,200)
     y2=x2*c
     plot(x2,y2,linewidth=4)
    
     annotate('Distance Travelled = 19', xy=(0,18))
          
     

    elif(i=='shed5'):
     x1=np.linspace(0,5,200)
     y1=x1*c
     plot(x1,y1,linewidth=4)
    
     x2=np.linspace(5,10,200)
     y2=x2*c
     plot(x2,y2,linewidth=4)
    
     x3=np.linspace(10,15,200)
     y3=x3-10
     plot(x3,y3,linewidth=4)
     
     annotate('Distance Travelled = 26', xy=(0,18))
         
    
     
    
    elif(i=='shed4'):
     x12=np.linspace(0,5,200)
     y12=x12
     plot(x12,y12,linewidth=4)
    
     x17=np.linspace(0,5,200)
     y17=np.linspace(5,10,200)
     plot(x17*0+5,y17,linewidth=4)
    
     x5=np.linspace(5,10,200)
     y5=np.linspace(0,10,200)
     plot(x5,y5*0+10,linewidth=4)
     
     annotate('Distance Travelled = 26', xy=(0,18))
         
    
     
    
    elif(i=='footballground'):
     x12=np.linspace(0,5,200)
     y12=x12
     plot(x12,y12,linewidth=4)
    
     x17=np.linspace(0,5,200)
     y17=np.linspace(5,10,200)
     plot(x17*0+5,y17,linewidth=4)
     
     annotate('Distance Travelled = 25', xy=(0,18))
          
    
     
    
    elif(i=='lblock'):
     x7=np.linspace(0,5,200)
     y7=np.linspace(5,10,200)
     plot(x7*c,y7,linewidth=4)

     x8=np.linspace(0,5,200)
     y8=np.linspace(0,5,200)
     plot(x8*c,y8,linewidth=4)
     
     annotate('Distance Travelled = 18', xy=(0,18))
          
    
     
    
    elif(i=='nbh'):
     x8=np.linspace(0,5,200)
     y8=np.linspace(0,5,200)
     plot(x8*c,y8,linewidth=4)
     
     annotate('Distance Travelled = 14', xy=(0,18))
         

     
    
    elif(i=='basketballcourt'):
     x12=np.linspace(0,5,200)
     y12=x12
     plot(x12,y12,linewidth=4)
     
     annotate('Distance Travelled = 14', xy=(0,18))
          
    
    
    
    elif(i=='shed2'):
     x12=np.linspace(0,5,200)
     y12=x12
     plot(x12,y12,linewidth=4)
    
     x10=np.linspace(5,10,200)
     y10=np.linspace(0,10,200)
     plot(x10,y10*0+5,linewidth=4)
     
     annotate('Distance Travelled = 22', xy=(0,18))
     
    else:
        print "Wrong Input"
        print "Chek Out The Map"
        
def path2(i):
    
 if(i=='ashokvihar'):
    x7=np.linspace(0,5,200)
    y7=np.linspace(5,10,200)
    plot(x7*c,y7,linewidth=4)
    
    x8=np.linspace(0,5,200)
    y8=np.linspace(0,5,200)
    plot(x8*c,y8,linewidth=4)
    
    annotate('Distance Travelled = 18', xy=(0,18))

 elif(i=='shed1'):
    x7=np.linspace(0,5,200)
    y7=np.linspace(5,10,200)
    plot(x7*c,y7,linewidth=4)
    
    x9=np.linspace(0,5,200)
    y9=np.linspace(0,10,200)
    plot(x9,y9*0+5,linewidth=4)
    
    x16=np.linspace(0,5,200)
    y16=np.linspace(0,5,200)
    plot(x16*0+5,y16,linewidth=4)
    
    annotate('Distance Travelled = 24', xy=(0,18))
    
 elif(i=='shed3'):
    x7=np.linspace(0,5,200)
    y7=np.linspace(5,10,200)
    plot(x7*c,y7,linewidth=4)
    
    x9=np.linspace(0,5,200)
    y9=np.linspace(0,10,200)
    plot(x9,y9*0+5,linewidth=4)
    
    x10=np.linspace(5,10,200)
    y10=np.linspace(0,10,200)
    plot(x10,y10*0+5,linewidth=4)
    
    x18=np.linspace(0,5,200)
    y18=np.linspace(0,5,200)
    plot(x18*0+10,y18,linewidth=4)
    
    annotate('Distance Travelled = 17', xy=(0,18))
    
 elif(i=='shed5'):
    x7=np.linspace(0,5,200)
    y7=np.linspace(5,10,200)
    plot(x7*c,y7,linewidth=4)
    
    x9=np.linspace(0,5,200)
    y9=np.linspace(0,10,200)
    plot(x9,y9*0+5,linewidth=4)
    
    x10=np.linspace(5,10,200)
    y10=np.linspace(0,10,200)
    plot(x10,y10*0+5,linewidth=4)
    
    x3=np.linspace(10,15,200)
    y3=x3-10
    plot(x3,y3,linewidth=4)
    
    x18=np.linspace(0,5,200)
    y18=np.linspace(0,5,200)
    plot(x18*0+10,y18,linewidth=4)
    
    
    annotate('Distance Travelled = 24', xy=(0,18))
    
 elif(i=='shed4'):
    x5=np.linspace(5,10,200)
    y5=np.linspace(0,10,200)
    plot(x5,y5*0+10,linewidth=4)
 
    x6=np.linspace(0,5,200)
    y6=np.linspace(0,10,200)
    plot(x6,y6*0+10,linewidth=4)
    
    annotate('Distance Travelled = 18', xy=(0,18))
    
 elif(i=='footballground'):
    x6=np.linspace(0,5,200)
    y6=np.linspace(0,10,200)
    plot(x6,y6*0+10,linewidth=4)
    
    annotate('Distance Travelled = 17', xy=(0,18))

 elif(i=='nbh'):
    x7=np.linspace(0,5,200)
    y7=np.linspace(5,10,200)
    plot(x7*c,y7,linewidth=4)
    
    annotate('Distance Travelled = 4', xy=(0,18))
    
 elif(i=='basketballcourt'):
    x13=np.linspace(0,5,200)
    y13=-x13+10
    plot(x13,y13,linewidth=4)
    
    annotate('Distance Travelled = 10', xy=(0,18))
    
 elif(i=='shed2'):
    x7=np.linspace(0,5,200)
    y7=np.linspace(5,10,200)
    plot(x7*c,y7,linewidth=4)
    
    x9=np.linspace(0,5,200)
    y9=np.linspace(0,10,200)
    plot(x9,y9*0+5,linewidth=4)
    
    x10=np.linspace(5,10,200)
    y10=np.linspace(0,10,200)
    plot(x10,y10*0+5,linewidth=4)
    
    annotate('Distance Travelled = 14', xy=(0,18))
    
 else:
     print "Wrong Input"
     print "Chek Out The Map"
     
def path3(i):
    
   if(i=='ashokvihar'):
    x8=np.linspace(0,5,200)
    y8=np.linspace(0,5,200)
    plot(x8*c,y8,linewidth=4)
    
    annotate('Distance Travelled = 14', xy=(0,18))
    
   elif(i=='shed1'):
    x9=np.linspace(0,5,200)
    y9=np.linspace(0,10,200)
    plot(x9,y9*0+5,linewidth=4)
    
    x16=np.linspace(0,5,200)
    y16=np.linspace(0,5,200)
    plot(x16*0+5,y16,linewidth=4)
    
    annotate('Distance Travelled = 20', xy=(0,18))
    
   elif(i=='shed3'):
    x9=np.linspace(0,5,200)
    y9=np.linspace(0,10,200)
    plot(x9,y9*0+5,linewidth=4)
    
    x10=np.linspace(5,10,200)
    y10=np.linspace(0,10,200)
    plot(x10,y10*0+5,linewidth=4)
    
    x18=np.linspace(0,5,200)
    y18=np.linspace(0,5,200)
    plot(x18*0+10,y18,linewidth=4)
    
    annotate('Distance Travelled = 13', xy=(0,18))
    
   elif(i=='shed5'):
    x9=np.linspace(0,5,200)
    y9=np.linspace(0,10,200)
    plot(x9,y9*0+5,linewidth=4)
    
    x10=np.linspace(5,10,200)
    y10=np.linspace(0,10,200)
    plot(x10,y10*0+5,linewidth=4)
    
    x18=np.linspace(0,5,200)
    y18=np.linspace(0,5,200)
    plot(x18*0+10,y18,linewidth=4)
    
    x3=np.linspace(10,15,200)
    y3=x3-10
    plot(x3,y3,linewidth=4)
    
    annotate('Distance Travelled = 20', xy=(0,18))
    
   elif(i=='shed4'):
    x9=np.linspace(0,5,200)
    y9=np.linspace(0,10,200)
    plot(x9,y9*0+5,linewidth=4)
    
    x17=np.linspace(0,5,200)
    y17=np.linspace(5,10,200)
    plot(x17*0+5,y17,linewidth=4)
    
    x5=np.linspace(5,10,200)
    y5=np.linspace(0,10,200)
    plot(x5,y5*0+10,linewidth=4)
    
    annotate('Distance Travelled = 14', xy=(0,18))
    
   elif(i=='footballground'):
    x9=np.linspace(0,5,200)
    y9=np.linspace(0,10,200)
    plot(x9,y9*0+5,linewidth=4)
    
    x17=np.linspace(0,5,200)
    y17=np.linspace(5,10,200)
    plot(x17*0+5,y17,linewidth=4)
    
    annotate('Distance Travelled = 13', xy=(0,18))

   elif(i=='lblock'):
    x7=np.linspace(0,5,200)
    y7=np.linspace(5,10,200)
    plot(x7*c,y7,linewidth=4)
    
    annotate('Distance Travelled = 4', xy=(0,18))
    
   elif(i=='basketballcourt'):
    x9=np.linspace(0,5,200)
    y9=np.linspace(0,10,200)
    plot(x9,y9*0+5,linewidth=4)
    
    annotate('Distance Travelled = 2', xy=(0,18))
    
   elif(i=='shed2'):
    x9=np.linspace(0,5,200)
    y9=np.linspace(0,10,200)
    plot(x9,y9*0+5,linewidth=4)

    x10=np.linspace(5,10,200)
    y10=np.linspace(0,10,200)
    plot(x10,y10*0+5,linewidth=4)
    
    annotate('Distance Travelled = 10', xy=(0,18))
   
   else:
        print "Wrong Input"
        print "Chek Out The Map"
        
print "Enter 1 for Ashok Vihar\n2 for NBH\n3 for L Block"
q=input("Enter The value ")
if(q==1):
    print "In This Graph Ashok Vihar is Your Home\n And You have nine more places to go"
    j1=raw_input("Enter Where You Want to go from Ashok Vihar To  ")
    map()
    path1(j1)
    show()
    
elif(q==2):
    print "In This Graph NBH is Your Home\n And You have nine more places to go"
    j2=raw_input("Enter Where You Want to go from NBH To  ")
    map()
    path3(j2)
    show()

elif(q==3):
    print "In This Graph L Block is Your Home\n And You have nine more places to go"
    j3=raw_input("Enter Where You Want to go from L Block To  ")
    map()
    path2(j3)
    show()

else:
    print "Wrong Input"
