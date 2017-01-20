import math

f_xn1=open('/home/neungioi/data/second/X1_num.txt','r')

f_wxn1=open('/home/neungioi/data/second/X1_Nor.txt','w')

i=0
count=0

l=f_xn1.readline()
s_l=l.split()
m_l=l.split()
v_l=l.split()
sd_l=l.split()
x_l=l.split()
    
size=len(s_l)

for i in range(0,size) :
    s_l[i]=float(0)
    m_l[i]=float(0)
    v_l[i]=float(0)
    sd_l[i]=float(0)
    x_l[i]=float(0)


f_xn1.close()
f_xn1=open('/home/neungioi/data/second/X1_num.txt','r')

for s in f_xn1:
    i=0
    l = s.split()
    count=count+1

    for i in range(0,size):
        s_l[i]= float(s_l[i]) + float(l[i])

i=0
for i in range(0,size) :
    m_l[i]=float(s_l[i] / count)

i=0
for i in range(0,size) :
    v_l[i]=float(s_l[i]*s_l[i] / count)
    sd_l[i]=math.sqrt(v_l[i])

f_xn1.close()

f_xn1=open('/home/neungioi/data/second/X1_num.txt','r')            

for s in f_xn1:
    l = s.split()

    i=0
    for i in range(0,size):
        if(sd_l[i]==0) :
            print(i)
            print('errror')
            x_l[i]=str(x_l[i])
        else :
            x_l[i]= float((float(l[i])-m_l[i])) / float(sd_l[i])
            x_l[i]=str(x_l[i])

    f_wxn1.write(" ".join(x_l))
    f_wxn1.write('\n')
    
f_wxn1.close()    



