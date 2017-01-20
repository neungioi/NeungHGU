fr_1 = open("/home/neungioi/data/second/final.txt",'r')
fr_2 = open('/home/neungioi/data/second/X1_vec.txt','r')
fr_3 = open('/home/neungioi/data/second/X1_Nor.txt','r')
fw=open("/home/neungioi/data/third/trans.txt",'w')

i=0
count=0

l=fr_1.readline()
x_l=l.split()

size=len(x_l)

for i in range(0,size) :
    x_l[i]=0

fr_1.close()
fr_1 = open("/home/neungioi/data/second/final.txt",'r')        

for s_1 in fr_1:  
    s_2 = fr_2.readline()  
    s_3 = fr_3.readline()

    l_1 = s_1.split()  
    l_2 = s_2.split("]")  
    l_3 = s_3.split()   

    l_2[0] = l_2[0]+']'
    l_2[1] = l_2[1]+']' 
    l_2[2] = l_2[2]+']' 
    l_2[3] = l_2[3]+']' 
    l_2[4] = l_2[4]+']'     

    x_l= l_1[0:2] + l_2[0:1]+ l_3[0:3] + l_2[1:2] +l_2[2:3] +l_3[3:9]+ l_2[3:4] +l_3[9:len(l_3)] +l_2[4:5]

    fw.write(",".join(x_l))
    fw.write('\n')

fr_1.close()
fr_2.close()
fr_3.close()
fw.close()
