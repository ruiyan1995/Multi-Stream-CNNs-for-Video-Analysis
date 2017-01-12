# encoding: utf-8
import cv2
import numpy as np
import pickle
from PIL import Image
import os
import gc
import shutil

labelList=['brush_hair','cartwheel','catch','chew','clap','climb','climb_stairs','dive'
               ,'draw_sword','dribble','drink','eat','fall_floor','fencing','flic_flac','golf'
               ,'handstand','hit','hug','jump','kick','kick_ball','kiss','laugh'
               ,'pick','pour','pullup','punch','push','pushup','ride_bike','ride_horse'
               ,'run','shake_hands','shoot_ball','shoot_bow','shoot_gun','sit','situp','smile'
               ,'smoke','somersault','stand','swing_baseball','sword','sword_exercise','talk','throw'
               ,'turn','walk','wave']
def findLabel(filename):
	#print filename
	with open('../dataset/temporal_train_data.pickle', 'rb') as f1:
		temporal_train_data = pickle.load(f1)

	return labelList[temporal_train_data[filename]-1]


def stackOpticalFlow(blocks,temporal_train_data,img_rows,img_cols):
	# print blocks
	firstTime=1
	try:
		firstTimeOuter=1
		for block in blocks:
			fx = []
			fy = []
			filename,blockNo=block.split('@')
			'''print 'block:'+ block
			print 'label:'
			print findLabel(block)'''
			path = './of_images/'+ findLabel(block) + '/' + filename
			blockNo=int(blockNo)
			
			for i in range((blockNo*10)-9,(blockNo*10)+1):

				#print path+'/'+'h'+str(i)+'_'+str(filename)+'.jpg'
				#print path+'/'+'h'+str(i)+'_'+str(filename)+'.jpg'
				imgH=Image.open(path+'/'+'h'+str(i)+'_'+str(filename)+'.jpg')
				imgV=Image.open(path+'/'+'v'+str(i)+'_'+str(filename)+'.jpg')
				imgH=imgH.resize((img_rows,img_cols))
				imgV=imgV.resize((img_rows,img_cols))
				fx.append(imgH)
				fy.append(imgV)
				
			flowX = np.dstack((fx[0],fx[1],fx[2],fx[3],fx[4],fx[5],fx[6],fx[7],fx[8],fx[9]))
			flowY = np.dstack((fy[0],fy[1],fy[2],fy[3],fy[4],fy[5],fy[6],fy[7],fy[8],fy[9]))
			inp = np.dstack((flowX,flowY))
			inp = np.expand_dims(inp, axis=0)
			if not firstTime:
				inputVec = np.concatenate((inputVec,inp))
				labels=np.append(labels,temporal_train_data[block]-1)
			else:
				inputVec = inp
				labels=np.array(temporal_train_data[block]-1)
				firstTime = 0
		inputVec=np.rollaxis(inputVec,3,1)
		inputVec=inputVec.astype('float16',copy=False)
		labels=labels.astype('int',copy=False)
		gc.collect()

		return (inputVec,labels)
	except:
		return (None,None)


def writeOpticalFlow(path,filename,w,h,c):
	count=0
	try:
         cap = cv2.VideoCapture(path+'/'+filename)
         ret, frame1 = cap.read()
         if frame1==None:
			return count
   
         frame1 = cv2.resize(frame1, (w,h))
         prvs = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
          # folder = './sp_images' + path[path.rfind("/"):] +'/'+ filename.split('.')[0] + '/'
         folder = './of_images' + path[path.rfind("/"):] +'/'+ filename.split('.')[0] + '/'
         # dir = os.path.dirname(folder)
         # os.makedirs(dir)
         if not os.path.isdir(folder):
                os.makedirs(folder)
         else:
             shutil.rmtree(folder)
             os.mkdir(folder)
             

          
         while(1):
                   ret, frame2 = cap.read()
                   
                   if frame2==None:
                       break
                   count+=1
                   if count%1==0:
				# print (filename+':' +str(c)+'-'+str(count))
                    
                                frame2 = cv2.resize(frame2, (w,h))
                                next = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
                                # prevImg, nextImg, pyr_scale, levels, winsize, iterations, poly_n, poly_sigma
                                flow = cv2.calcOpticalFlowFarneback(prvs,next, 0.5, 3, 15, 3, 5, 1.2, 0)
                                # flow = cv2.calcOpticalFlowFarneback(prvs,next,0.5,1,3,15,3,5,1)
                                horz = cv2.normalize(flow[...,0], None, 0, 255, cv2.NORM_MINMAX)
                                vert = cv2.normalize(flow[...,1], None, 0, 255, cv2.NORM_MINMAX)
                                horz = horz.astype('uint8')
                                vert = vert.astype('uint8')

                                cv2.imwrite(folder+'h'+str(count)+'_'+filename.split('.')[0]+'.jpg',horz,[int(cv2.IMWRITE_JPEG_QUALITY), 90])
                                cv2.imwrite(folder+'v'+str(count)+'_'+filename.split('.')[0]+'.jpg',vert,[int(cv2.IMWRITE_JPEG_QUALITY), 90])
                    
                                prvs = next

         cap.release()
         cv2.destroyAllWindows()
         return count
	except Exception,e:
		print e
		return count
