import glob
import random
import math

original_fList = glob.glob("/home/neungioi/data_filtering/data_processing/*.txt")
train = open("/home/neungioi/data_filtering/after_processing/train.txt",'w')
train_validation = open("/home/neungioi/data_filtering/after_processing/train_validation.txt",'w')
sample = open("/home/neungioi/data_filtering/after_processing/test.txt",'w')
sample_validation = open("/home/neungioi/data_filtering/after_processing/test_validation.txt",'w')
meta = open("/home/neungioi/data_filtering/after_processing/meta.txt",'w')

seen_0=set()
seen_4=set()
seen_5=set()
seen_6=set()
seen_7=set()
seen_8=set()
seen_9=set()
seen_10=set()
seen_11=set()
seen_13=set()
seen_14=set()
seen_68=set()
seen_69=set()
seen_70=set()

count=0
result = []
real_result=[]
mom=[]
validation=[]
mom_validation=[]

for i in original_fList :
    f=open(i,'r')
    for s in f :
        l = s.split('\t')
        result.append(l)
        count=count+1
    f.close()

for i in range(0,count) :   
    for j in range(0,len(l)) :   
        if(j >= 0 and j<=1) :
            continue
        elif(j>=21 and j<=27):
            continue
        elif(j>=29 and j<=42):
            continue
        elif(j>=85 and j<=105):
            continue
        elif(j==112) :
            continue
        elif(j>=113 and j<=120):  
            validation.append(result[i][j])
        elif(j>=122 and j<=129):
            continue
        else:
            real_result.append(result[i][j])
    mom.append(real_result)
    mom_validation.append(validation)
    real_result=[]
    validation=[]



for i in range (0,count):    
    for j in range (0,len(mom[0])) :
        if(j==0) :
            seen_0.add(mom[i][j])
        elif(j==4) :
            seen_4.add(mom[i][j])
        elif(j==5) :
            seen_5.add(mom[i][j])
        elif(j==6) :
            seen_6.add(mom[i][j])
        elif(j==7) :
            seen_7.add(mom[i][j])
        elif(j==8) :
            seen_8.add(mom[i][j])
        elif(j==9) :
            seen_9.add(mom[i][j])
        elif(j==10) :
            seen_10.add(mom[i][j])
        elif(j==11) :
            seen_11.add(mom[i][j])
        elif(j==13) :
            seen_13.add(mom[i][j]) 
        elif(j==14) :
            seen_14.add(mom[i][j])
        elif(j==68) :
            seen_68.add(mom[i][j])
        elif(j==69) :
            seen_69.add(mom[i][j])
        elif(j==70) :
            seen_70.add(mom[i][j])

dictionary={}                 
dictionary[0]=len(seen_0)
dictionary[4]=len(seen_4)
dictionary[5]=len(seen_5)
dictionary[6]=len(seen_6)
dictionary[7]=len(seen_7)
dictionary[8]=len(seen_8)
dictionary[9]=len(seen_9)
dictionary[10]=len(seen_10)
dictionary[11]=len(seen_11)
dictionary[13]=len(seen_13)
dictionary[14]=len(seen_14)
dictionary[68]=len(seen_68)
dictionary[69]=len(seen_69)
dictionary[70]=len(seen_70)

for k in dictionary.keys():
    meta.write(str(k))
    meta.write(',')
    meta.write(str(dictionary[k]))
    meta.write(' ')

meta.close()

map0=""          
map4=""
map5=""
map6=""
map7=""
map8=""
map9=""
map10=""
map11=""
map13=""
map14=""
map68=""
map69=""
map70=""

for i in range(0,len(seen_0)-1): 
    map0=map0+'0,'
for i in range(0,len(seen_4)-1):
    map4=map4+'0,'
for i in range(0,len(seen_5)-1):
    map5=map5+'0,'
for i in range(0,len(seen_6)-1):    
    map6=map6+'0,'
for i in range(0,len(seen_7)-1):    
    map7=map7+'0,'
for i in range(0,len(seen_8)-1): 
    map8=map8+'0,'
for i in range(0,len(seen_9)-1):
    map9=map9+'0,'
for i in range(0,len(seen_10)-1):
    map10=map10+'0,'
for i in range(0,len(seen_11)-1):    
    map11=map11+'0,'
for i in range(0,len(seen_13)-1):    
    map13=map13+'0,'
for i in range(0,len(seen_14)-1): 
    map14=map14+'0,'
for i in range(0,len(seen_68)-1):
    map68=map68+'0,'
for i in range(0,len(seen_69)-1):
    map69=map69+'0,'
for i in range(0,len(seen_70)-1):    
    map70=map70+'0,'

map0=map0+'0'
map4=map4+'0'
map5=map5+'0'
map6=map6+'0'
map7=map7+'0'
map8=map8+'0'
map9=map9+'0'
map10=map10+'0'
map11=map11+'0'
map13=map13+'0'
map14=map14+'0'
map68=map68+'0'
map69=map69+'0'
map70=map70+'0'


map0_r=[]
map4_r=[]
map5_r=[]
map6_r=[]
map7_r=[]
map8_r=[]
map9_r=[]
map10_r=[]
map11_r=[]
map13_r=[]
map14_r=[]
map68_r=[]
map69_r=[]
map70_r=[]


for i in range(0,len(seen_0)):
    map0_r.append(map0)
    m0="0"*(len(seen_0)-(i+1))+"1"+"0"*i
    map0_r[i]=m0
for i in range(0,len(seen_4)):
    map4_r.append(map4)
    m4="0"*(len(seen_4)-(i+1))+"1"+"0"*i
    map4_r[i]=m4
for i in range(0,len(seen_5)):
    map5_r.append(map5)
    m5="0"*(len(seen_5)-(i+1))+"1"+"0"*i
    map5_r[i]=m5
for i in range(0,len(seen_6)):
    map6_r.append(map6)
    m6="0"*(len(seen_6)-(i+1))+"1"+"0"*i
    map6_r[i]=m6
for i in range(0,len(seen_7)):
    map7_r.append(map8)
    m7="0"*(len(seen_7)-(i+1))+"1"+"0"*i
    map7_r[i]=m7
for i in range(0,len(seen_8)):
    map8_r.append(map8)
    m8="0"*(len(seen_8)-(i+1))+"1"+"0"*i
    map8_r[i]=m8
for i in range(0,len(seen_9)):
    map9_r.append(map9)
    m9="0"*(len(seen_9)-(i+1))+"1"+"0"*i
    map9_r[i]=m9
for i in range(0,len(seen_10)):
    map10_r.append(map10)
    m10="0"*(len(seen_10)-(i+1))+"1"+"0"*i
    map10_r[i]=m10
for i in range(0,len(seen_11)):
    map11_r.append(map11)
    m11="0"*(len(seen_11)-(i+1))+"1"+"0"*i
    map11_r[i]=m11
for i in range(0,len(seen_13)):
    map13_r.append(map13)
    m13="0"*(len(seen_13)-(i+1))+"1"+"0"*i
    map13_r[i]=m13
for i in range(0,len(seen_14)):
    map14_r.append(map14)
    m14="0"*(len(seen_14)-(i+1))+"1"+"0"*i
    map14_r[i]=m14
for i in range(0,len(seen_68)):
    map68_r.append(map68)
    m68="0"*(len(seen_68)-(i+1))+"1"+"0"*i
    map68_r[i]=m68
for i in range(0,len(seen_69)):
    map69_r.append(map69)
    m69="0"*(len(seen_69)-(i+1))+"1"+"0"*i
    map69_r[i]=m69
for i in range(0,len(seen_70)):
    map70_r.append(map70)
    m70="0"*(len(seen_70)-(i+1))+"1"+"0"*i
    map70_r[i]=m70

dic0={}                
dic4={}
dic5={}
dic6={}
dic7={}
dic8={}
dic9={}
dic10={}
dic11={}
dic13={}
dic14={}
dic68={}
dic69={}
dic70={}

lst0=list(seen_0)
lst4=list(seen_4)
lst5=list(seen_5)
lst6=list(seen_6)
lst7=list(seen_7)
lst8=list(seen_8)
lst9=list(seen_9)
lst10=list(seen_10)
lst11=list(seen_11)
lst13=list(seen_13)
lst14=list(seen_14)
lst68=list(seen_68)
lst69=list(seen_69)
lst70=list(seen_70)

for i in range(0,len(seen_0)):
    dic0[lst0[i]]=map0_r[i]
    
for i in range(0,len(seen_4)):
    dic4[lst4[i]]=map4_r[i]
    
for i in range(0,len(seen_5)):
    dic5[lst5[i]]=map5_r[i]
    
for i in range(0,len(seen_6)):
    dic6[lst6[i]]=map6_r[i]
    
for i in range(0,len(seen_7)):
    dic7[lst7[i]]=map7_r[i]
    
for i in range(0,len(seen_8)):
    dic8[lst8[i]]=map8_r[i]
    
for i in range(0,len(seen_9)):
    dic9[lst9[i]]=map9_r[i]
    
for i in range(0,len(seen_10)):
    dic10[lst10[i]]=map10_r[i]
    
for i in range(0,len(seen_11)):
    dic11[lst11[i]]=map11_r[i]
    
for i in range(0,len(seen_13)):
    dic13[lst13[i]]=map13_r[i]
    
for i in range(0,len(seen_14)):
    dic14[lst14[i]]=map14_r[i]
    
for i in range(0,len(seen_68)):
    dic68[lst68[i]]=map68_r[i]
    
for i in range(0,len(seen_69)):
    dic69[lst69[i]]=map69_r[i]
    
for i in range(0,len(seen_70)):
    dic70[lst70[i]]=map70_r[i]

for i in range (0,count):               
    for j in range (0,len(mom[0])) :
        if(j==0) :
            if(mom[i][j] in dic0) :
                    mom[i][j]=dic0[mom[i][j]]
        elif(j==4) :
            if(mom[i][j] in dic4) :
                    mom[i][j]=dic4[mom[i][j]]
        elif(j==5) :
            if(mom[i][j] in dic5) :
                    mom[i][j]=dic5[mom[i][j]]
        elif(j==6) :
            if(mom[i][j] in dic6) :
                    mom[i][j]=dic6[mom[i][j]]
        elif(j==7) :
            if(mom[i][j] in dic7) :
                    mom[i][j]=dic7[mom[i][j]]
        elif(j==8) :
            if(mom[i][j] in dic8) :
                    mom[i][j]=dic8[mom[i][j]]
        elif(j==9) :
            if(mom[i][j] in dic9) :
                    mom[i][j]=dic9[mom[i][j]]
        elif(j==10) :
            if(mom[i][j] in dic10) :
                    mom[i][j]=dic10[mom[i][j]]
        elif(j==11) :
            if(mom[i][j] in dic11) :
                    mom[i][j]=dic11[mom[i][j]] 
        elif(j==13) :
            if(mom[i][j] in dic13) :
                    mom[i][j]=dic13[mom[i][j]]
        elif(j==14) :
            if(mom[i][j] in dic14) :
                    mom[i][j]=dic14[mom[i][j]]
        elif(j==68) :
            if(mom[i][j] in dic68) :
                    mom[i][j]=dic68[mom[i][j]]
        elif(j==69) :
            if(mom[i][j] in dic69) :
                    mom[i][j]=dic69[mom[i][j]]
        elif(j==70) :
            if(mom[i][j] in dic70) :
                    mom[i][j]=dic70[mom[i][j]]

for i in range(0,count) :
    mom[i]=mom[i]+mom_validation[i]

col_count=0
number=9*int(count/10)
                           
random.shuffle(mom)

re_1=[]
mom_re_1=[]
re_2=[]
mom_re_2=[]

for i in range(0,count) :
    for j in range(0,len(mom[0])) :
        if(j<=len(mom[0])-9) :
            re_1.append(mom[i][j])   
        else :
            re_2.append(mom[i][j])

    mom_re_1.append(re_1)
    re_1=[]
    mom_re_2.append(re_2)
    re_2=[]

train_data_x = mom_re_1[:number]
train_data_y = mom_re_2[:number]
test_data_x = mom_re_1[number:]
test_data_y = mom_re_2[number:]




for i in range(0,number) :
    train_validation.write(",".join(map(str,train_data_y[i])))
    train_validation.write("\n")

for i in range(0,count-number) :
    sample_validation.write(",".join(map(str,test_data_y[i])))
    sample_validation.write("\n")

train_validation.close()
sample_validation.close()

for i in range(0,len(mom_re_1[0])) :
    col_count=col_count+1


s_l=[]
v_l=[]
v_l2=[]
pow_l=[]
m_l=[]
sd_l=[]
tx_l=[]
sx_l=[]


for i in range(0,col_count) :
    s_l.append("0")
    v_l.append("0")
    pow_l.append("0")
    m_l.append("0")
    sd_l.append("0")
    tx_l.append("0")
    sx_l.append("0")



for i in range(0,number) :
    for j in range(0,col_count) :
        if(j==0) :
            continue
        elif(j>=4 and j<=11):
            continue
        elif(j==13 or j==14) :
            continue
        elif(j>=68 and j<=70):
            continue
        else :
            s_l[j]=float(s_l[j])+float(train_data_x[i][j])
            pow_l[j]=float(pow_l[j])+float(train_data_x[i][j])*float(train_data_x[i][j])

for i in range(0,col_count) :
    if(i==0) :
        continue
    elif(i>=4 and i<=11) :
        continue
    elif(i== 13 or i==14) :
        continue
    elif(i>=68 and i<=70):
        continue
    else :
        m_l[i]=float(float(s_l[i]) / number)

for i in range(0,number) :
    for j in range(0,col_count) :
        if(j==0) :
            continue
        elif(j>=4 and j<=11):
            continue
        elif(j==13 or j==14) :
            continue
        elif(j>=68 and j<=70):
            continue
        else :       
            v_l[j]=(float(pow_l[j])-2*m_l[j]*s_l[j])/number + m_l[j]*m_l[j]
            sd_l[j]=math.sqrt(v_l[j])

for i in range(0,len(train_data_x)) :
    for j in range(0,col_count) :
        if(j==0) :
            tx_l[j]=train_data_x[i][j]
        elif(j>=4 and j<=11):
            tx_l[j]=train_data_x[i][j]
        elif(j==13 or j==14) :
            tx_l[j]=train_data_x[i][j]
        elif(j>=68 and j<=70):
            tx_l[j]=train_data_x[i][j]
        else :
            if(sd_l[j]==0) :
               tx_l[j]=float(0)
            else :
                tx_l[j]=float((float(train_data_x[i][j])-m_l[j])) / float(sd_l[j])
        
    train.write(",".join(map(str,tx_l)))
    train.write('\n')


for i in range(0,len(test_data_x)) :
    for j in range(0,col_count) :
        if(j==0) :
            sx_l[j]=test_data_x[i][j]
        elif(j>=4 and j<=11):
            sx_l[j]=test_data_x[i][j]
        elif(j==13 or j==14) :
            sx_l[j]=test_data_x[i][j]
        elif(j>=68 and j<=70):
            sx_l[j]=test_data_x[i][j]
        else :
            if(sd_l[j]==0):
                sd_l[j]=float(0)
            else :
                sx_l[j]=float((float(test_data_x[i][j])-m_l[j])) / float(sd_l[j])
        
    sample.write(",".join(map(str,sx_l)))
    sample.write('\n')

train.close()
sample.close()

