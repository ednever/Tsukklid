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


#A=input("Siseta arv")
#while int(A)<=1:
#    try:
#        A=int(input("Siseta "+str(i+1)+" arv"))
#    except:
#        TypeError
#Summa=0
#for i in range(1,int(A)+1):
#    Summa+=i
#print("Summa võrdub - ",Summa)


#korrutis=1
#for i in range(8):
#    arv=float(input("Siseta arv - "))
#    if arv>0:
#        korrutis*=arv
#print(korrutis)


#S=int(input("Sisesta summa - "))
#N=int(input("Mitu aastat - "))
#for aasta in range(1,N+1):
#    S*=1.03
#    print(aasta,"aasta pärast tulemus on ",round(S,2))


#kogus=0
#summa=0
#for i in range(100,1001):
#    if i%7==0:
#        print(i) #ekraanile
#        kogus+=1 #kogus suurendamine
#        summa+=i #i-de summa,mis jagatakse 7
#print("Arvude kogus on - ",kogus," ja arvude summa on - ",summa)


#for i in range(1000,5,-7):
#    print(i)
#print("Я гуль")


#for rjady in range(10):
#    for stroka in range(10):
#        print(stroka,end=" ")
#    print()


#for rjad in range(1,10):
#    for stroka in range(1,10):
#        if rjad==stroka:
#            print(stroka,end=" ")
#        else:
#            print(0,end=" ")
#    print()


#for rjad in range(1,10):
#    for stroka in range(1,10):
#        if rjad==stroka:
#            print("x",end=" ")
#        elif stroka==1:
#            print("x",end=" ")
#        elif stroka==2:
#            print("y",end=" ")
#        else:
#            print("0",end=" ")
#    print()


#loom=input("Купи слона!")
#while loom.title()!="Слон": #upper(),lower()
#    loom=input("Все говорят "+loom+"! А ты купи!!!")
#print("Молодец!!!")


from random import*
arv=0
print("Loterii".center(50,"*"))