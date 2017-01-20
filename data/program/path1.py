import glob
File_List=glob.glob('/home/neungioi/data/first/*.txt')

fw = open('/home/neungioi/data/second/final.txt','w')

fw_n1 = open('/home/neungioi/data/second/X1_num.txt','w')
fw_c1= open('/home/neungioi/data/second/X1_char.txt','w')
fw_n2 = open('/home/neungioi/data/second/Y1_num.txt','w')

for i in File_List :
    f=open(i,'r')
    for s in f :
        l=s.split()
        fw.write(' '.join(l))
        fw.write('\n')

    f.close()

fw.close()

f=open('/home/neungioi/data/second/final.txt','r')

for s in f:
    l = s.split()
            
    n_l1=l[3:6] +l[8:14] +l[15:111]

    c_s1=l[2:3]+l[6:7]+l[7:8]+l[14:15] +l[120:121]
            
    n_l2=l[111:120]

    fw_n1.write(" ".join(n_l1))
    fw_c1.write(' '.join(c_s1))
    fw_n2.write(' '.join(n_l2))
    
    fw_n1.write('\n')
    fw_c1.write('\n')
    fw_n2.write('\n')        

f.close()
fw_n1.close()
fw_c1.close()
fw_n2.close()
    
  
