#encoding: utf-8
import numpy as np
import optical_flow_prep as ofp
import sys,os
import pickle
import scandir
import gc

def writeOF():

    ##root = "../videos"
    root = '/media/yanrui/文档/迅雷下载/Two-Stream/hmdb51_org/video/'
    w=224
    h=224
    c=0
    data={}

    for path, subdsirs, files in scandir.walk(root):
        for filename in files:
            
            count=ofp.writeOpticalFlow(path,filename,w,h,c)
            filename = filename.split('.')[0]
            if count:
                data[filename]=count
            print filename
            c+=1
            with open("done.txt", "a") as myfile:
                myfile.write(filename+'-'+str(c)+'\n')

    with open('../dataset/frame_count.pickle','wb') as f:
        pickle.dump(data,f)


def data_prep():
    print 'Starting with data prep'
    with open('../dataset/frame_count.pickle','rb') as f1:
        frame_count=pickle.load(f1)
    with open('../dataset/merged_data.pickle','rb') as f2:
        merged_data=pickle.load(f2)
    print 'Loaded dictionary'
    root = './of_images/'
    path = os.path.join(root, '')
    data={}
    misplaced_data=[]
    count=0
    for path, subdirs, files in scandir.walk(root):
        for filename in files:
            #print filename + '  ' + str(count)
            count+=1
            try:
                vidname=filename.split('_',1)[1].split('.')[0]
                #print filename
                #print vidname
                fc=frame_count[vidname]
                print fc
                for i,j in enumerate(merged_data[vidname]):
                    if j:
                        index=i
                        break
                for i in range(1,(fc/10)+1):
                    #print i
                    data[vidname+'@'+str(i)]=index+1
            except Exception,e:
                misplaced_data.append(filename)

    print 'Writing final training dictionary'
    #print data
    with open('../dataset/temporal_train_data.pickle','wb') as f3:
        pickle.dump(data,f3)

    print 'Writing misplaced videos'
    with open('../dataset/misplaced_data.pickle','wb') as f4:
        pickle.dump(misplaced_data,f4   )

if __name__ == "__main__":
    #writeOF()
    #gc.collect()
    data_prep()