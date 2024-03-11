import random
#lista ranndom
miLista= [random.randint(0,5)for i in range(3)]
pass

def ordenar(l:list):
    lFinal=[]
    while True:
        lFinal.clear()
        while len(l)>0:
            if len(l)==1:
                lFinal.append(l[0])
                l.pop(0)
            elif l[0]>=l[1]:
                lFinal.append(l[1])
                l.pop(1)
            elif l[0]<=l[1]:
                lFinal.append(l[0])
                l.pop(0)
        l+=lFinal
        while lFinal[0]<=lFinal[1]:
            lFinal.pop(0)
            if len(lFinal)==1:
                return l



            
        
        

milista=[1,4,53,531,1,5,1]

print(ordenar(miista))




                

        

        

        
