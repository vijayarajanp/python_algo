# All conforms
# Identify the minimum # of iteration for flip the caps
# F - forward cap
# B - Backward cap
# Referrenc MIT open coureware

caps_1 = ['F','B','F','B','F','F','F','B','B','B']
caps = ['F','B','F','B','F','F','F','B','B','B','F','F','F']
i=1
forward=0
backward=0
start=0
flip=''
Lst=[]
while i<len(caps):
   # print(caps[i])
    if caps[start]!=caps[i]:
        Lst.append((start,i-1,caps[start]))
        start=i
    if caps[i]=='F':
        forward+=1
    elif caps[i]=='B':
        backward+=1
    i+=1

    if i == len(caps):
        t=Lst[len(Lst)-1]
        start = t[1]+1
        Lst.append((start,i-1,caps[start]))    
    
if forward<backward:
    flip='F'
else:
    flip='B'

    #print("flip",flip)   

for j in Lst:
    #print(j)
    if j[2] == flip:
        if j[0] != j[1]:
            print("People ",j[0]," to ",j[1]," flip cap")
        else:
            print("flip the cap ",j[0])
    

#print("Forward:",forward)
#print("Backward:",backward)
#print(fLst)


#### Tunned version ####
# All conforms
# Identify the minimum # of iteration for flip the caps
# F - forward cap
# B - Backward cap
# Referrenc MIT opencoure ware

caps_1 = ['F','B','F','B','F','F','F','B','B','B']
caps = ['F','B','F','B','F','F','F','B','B','B','F','F','F']

caps.append("END")

i=1
forward=0
backward=0
start=0
flip=''
Lst=[]

while i<len(caps):
   # print(caps[i])
    if caps[start]!=caps[i]:
        Lst.append((start,i-1,caps[start]))
        start=i
    if caps[i]=='F':
        forward+=1
    elif caps[i]=='B':
        backward+=1
    i+=1

# Eliminate the below block code from adding the one more entry in the Main list
#    if i == len(caps):
#        t=Lst[len(Lst)-1]
#        start = t[1]+1
#        Lst.append((start,i-1,caps[start]))    
    
if forward<backward:
    flip='F'
else:
    flip='B'

    #print("flip",flip)   

for j in Lst:
    #print(j)
    if j[2] == flip:
        if j[0] != j[1]:
            print("People ",j[0]," to ",j[1]," flip cap")
        else:
            print("flip the cap ",j[0])
    

#print("Forward:",forward)
#print("Backward:",backward)
#print(fLst)
