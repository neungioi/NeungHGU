vec_input = open('/home/neungioi/data/second/X1_char.txt','r')
vec_output = open('/home/neungioi/data/second/X1_vec.txt','w')

seen_1=set()
seen_2=set()
seen_3=set()
seen_4=set()
seen_5=set()

count=0
result = []

for s in vec_input:
    l = s.split()
    result.append(l)
    count=count+1



for i in range (0,count): 
    for j in range (0,len(l)) :
        if(j==0) :
            seen_1.add(result[i][j])
        elif(j==1) :
            seen_2.add(result[i][j])
        elif(j==2) :
            seen_3.add(result[i][j])
        elif(j==3) :
            seen_4.add(result[i][j])
        else :
            seen_5.add(result[i][j])

lst_1=list(seen_1)
lst_2=list(seen_2)
lst_3=list(seen_3)
lst_4=list(seen_4)
lst_5=list(seen_5)

size1=len(lst_1) 
size2=len(lst_2)
size3=len(lst_3)
size4=len(lst_4)
size5=len(lst_5)

map1=[]
map2=[]
map3=[]
map4=[]
map5=[]

for i in range(0,size1): 
    map1.append("0")    
for i in range(0,size2):
    map2.append("0")
for i in range(0,size3):
    map3.append("0")
for i in range(0,size4):    
    map4.append("0")
for i in range(0,size5):    
    map5.append("0")


map1_r=[]
map2_r=[]
map3_r=[]
map4_r=[]
map5_r=[]

for i in range(0,size1):
    map1_r.append("0")

for i in range(0,size1): 
    map1[i]="1"
    map1_r[i]=list(map1)
    map1[i]="0"    


for i in range(0,size2):
    map2_r.append("0")
    
for i in range(0,size2): 
    map2[i]="1"
    map2_r[i]=list(map2)
    map2[i]="0"    

for i in range(0,size3):
    map3_r.append("0")
    
for i in range(0,size3): 
    map3[i]="1"
    map3_r[i]=list(map3)
    map3[i]="0"
    
for i in range(0,size4):
    map4_r.append("0")

for i in range(0,size4): 
    map4[i]="1"
    map4_r[i]=list(map4)
    map4[i]="0"

for i in range(0,size5):
    map5_r.append("0")

for i in range(0,size5): 
    map5[i]="1"
    map5_r[i]=list(map5)
    map5[i]="0"    

dic1={}
dic2={}
dic3={}
dic4={}
dic5={}

for i in range(0,len(lst_1)):
    dic1[lst_1[i]]=map1_r[i]  

for i in range(0,len(lst_2)):
    dic2[lst_2[i]]=map2_r[i]

for i in range(0,len(lst_3)):
    dic3[lst_3[i]]=map3_r[i]

for i in range(0,len(lst_4)):
    dic4[lst_4[i]]=map4_r[i]
    
for i in range(0,len(lst_5)):
    dic5[lst_5[i]]=map5_r[i]


for i in range (0,count):  
    for j in range (0,len(l)) :
        if(j==0) :
            if(result[i][j] in dic1) :
                    result[i][j]=dic1[result[i][j]]
        elif(j==1) :
            if(result[i][j] in dic2) :
                    result[i][j]=dic2[result[i][j]]
        elif(j==2) :
            if(result[i][j] in dic3) :
                    result[i][j]=dic3[result[i][j]]
        elif(j==3) :
            if(result[i][j] in dic4) :
                    result[i][j]=dic4[result[i][j]]
        else :
            if(result[i][j] in dic5) :
                    result[i][j]=dic5[result[i][j]] 



for i in range(0,count) :
    vec_output.write("".join(map(str,result[i])))
    vec_output.write('\n')

vec_output.close()
vec_input.close()
