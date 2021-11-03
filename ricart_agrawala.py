import random
import time

class RA():
    number=int(input("Enter the number of processes to be considered in the system: "))
    def __init__(self):
        global number
        number=self.number
        print("The processes are :")
        for i in range (number):
            print(f"P{i}",end=" ")
    
    def process(self):
        global number
        P={}
        RA.process.P=P
        number=self.number
        print("\n\nThe timetsamp of request for Critical State for each process is:")
        for i in range(number):
            TimeStamp=random.randint(0,5)
            P[i]=TimeStamp                                #Dictionary of processes alongwith their timestamps
        print(P)
        print("\nThe RD arrays for each process is")
        T1=list(P.values())
        RD={}
        RA.process.RD=RD
        for key,value in P.items():
            RDi=[]
            for i in range(len(T1)):
                if key==i:
                    RDi.append(0)
                elif T1[i]<value or T1[i]==value:
                    RDi.append(0)
                elif T1[i]>value:
                    RDi.append(1)
            RD[key]=RDi                                   #RD array of all processes
            print("P",key," ",RDi)
        print("\n")
        return RD,P     
    
    t0=time.perf_counter()                                #Start timer to enter CS
    def critical_section(self):
        global number
        global t0
        t0=self.t0
        number=self.number
        RD=RA.process.RD
        T1=list(RD.values())
        T2=[]
        for i in range(len(T1)):
            a=T1[i].count(1)
            T2.append(a)
        if max(T2)==0:
            for key,value in RD.items():                
                t1=time.perf_counter()
                total=t1-t0
                print(f"P {key} will enter critical section and the wait time was {total:0.5f}\n")
                print("That was the Ricart Agrawala Algorithm!!!!")
                exit()
        else:
            maxi=max(T2)
            counter=0
            for key,value in RD.items():
                if value.count(1)==maxi and counter==0:       #Process with higher index and lowest TS will enter CS
                    t1=time.perf_counter()
                    total=t1-t0
                    print(f"P {key} will enter critical section and the wait time was {total:0.5f}")
                    counter=1
                    a=key
                elif value.count(1)!=maxi or counter!=0:
                    print(f"P {key} will not enter critical section and will wait")
                else:
                    t1=time.perf_counter()
                    total=t1-t0
                    print(f"P {key} will enter critical section and the wait time was {total:0.5f}")
                    counter=1
                    a=key                     
            print(f"P {a} will release CS after use and give reply to all other request\n")
            RD.pop(a)                                         #Process gives reply to all other process after releasing CS
            RA.critical_section(self)
                                         
obj=RA()
obj.process()
obj.critical_section()