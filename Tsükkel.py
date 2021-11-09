#p=0
#for i in range(15): #i=0,1,2,3...
#    A=0
#    while type(A)!=float:
#        try:
#            A=float(input("Sisesta "+str(i+1)+" arv - "))
#        except ValueError:
#            print("Vale andmetüüp")
#    if A==round(A):
#        p+=1
#        print(str(A)+" on täisarv")
#    else:
#        print(str(A)+" ei ole täisarv")
#print(str(p)+" Täisarvud")

#for i in range(10,21,1):
#    print(i**2)

#from random import*
#A=randint(10,100)
#B=randint(100,1000)
#print("A = "+str(A))
#print("B = "+str(B))
#K=int(input("K: "))
#for i in range(A,B+1):
#    if i%K==0:print(i)

#from random import*
#p=0
#n=0
#N=randint(1,10)
#print(N)
#for i in range(N):
#    Arv=int(input("Siseta arv - "))
#    if Arv>0:
#        p+=1
#    elif Arv<0:
#        n+=1
#print("Negatiivsed = "+str(n))
#print("Positiivsed = "+str(p))
#print("Nullid = "+str(N-n-p))