from random import randrange
import platform
import os
import pickle
non=input("antre psedo pou jwet la \n").lower().replace(" ","")
if platform.system()=="Windows":
    if not os.path.exists("c:/Users/Public/lis_sko/sko.txt"):
        d="lis_sko"
        b="c:/Users/Public/"
        p=os.path.join(b,d)
        os.mkdir(p)
        fichye=open("c:/Users/Public/lis_sko/sko.txt","wb")
        done=dict()
        pickle.dump(done,fichye)
        fichye.close()
        fichye=open("c:/Users/Public/lis_sko/sko.txt","rb")
        done=pickle.load(fichye)
        fichye.close()
    else:
        fichye=open("c:/Users/Public/lis_sko/sko.txt","rb")
        done=pickle.load(fichye)
        fichye.close()
else:
    if not os.path.exists("/home/lis_sko/sko.txt"):
        d="lis_sko"
        b="/home/"
        p=os.path.join(b,d)
        os.mkdir(p)
        fichye=open("/home/lis_sko/sko.txt","wb")
        done=dict()
        pickle.dump(done,fichye)
        fichye.close()
        fichye=open("/home/lis_sko/sko.txt","rb")
        done=pickle.load(fichye)
        fichye.close()
    else:
        fichye=open("/home/lis_sko/sko.txt","rb")
        done=pickle.load(fichye)
        fichye.close()
        print("\t====****************************************************====\n ")
print("\t \t     byenveni nan jwèt la "+non+"\n")
print("\t====****************************************************====\n ")
while True:
    A=randrange(0,10)
    l=5
    while l!=0: 
        n=input("antre nonb wap chwazi nan intèval 0 a 9\n")
        while(not n.isdigit() or int(n)>9 or int(n)<0):
            n=input("erè antre nonb lan entèval 0 a 9\n")
        n=int(n)
        if(n==A):
            print("BRAVO !! ou genyen ")
            o=done.get(non)
            if o is None:
                done[non]=l*30
                print("nouvo sko a ase :"+str(done[non])+"\n peze k siw pap kontinye nenpot pou kontinye")
            else:
                print("ansyen sko ase :"+str(o))
                done[non]=l*30+o
                print("nouvo sko a ase :"+str(done[non])+"\npeze k siw pap kontinye nenpot pou kontinye")
            if platform.system()=="Windows":
                fichye_mw=open("c:/Users/Public/lis_sko/sko.txt","wb")
                pickle.dump(done,fichye_mw)
                fichye_mw.close()
            else:
                fichye_mw=open("/home/lis_sko/sko.txt","wb")
                pickle.dump(done,fichye_mw)
                fichye_mw.close()
            break
        if(n!=A):
            l-=1
            if(n>A):
                print("ou pa jwenn li ou rete ",l,"chans  epi nonb ou chwazi a pigro ke sak soti a")   
            else:
                print("ou pa jwenn li ou rete ",l,"chans epi nonb ou chwazi a pi piti ke sak soti a")
    if l==0:         
        print("nonb kache a se ",A,"    siw pap  kontinye peze k\n")
    
    b=input().lower()
    if b=="k":
       break
print("\t====****************************************************====\n ")
print("\t \t    mèsi paskew te jwe !!!!!!!! \n")
print("\t====****************************************************====\n ")

