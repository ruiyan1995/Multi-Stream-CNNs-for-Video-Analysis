#encoding: utf-8
import sys,os
import pickle

data={}
train_data={}
counter=0


with open('../dataset/data_ID.txt') as f1,open('../dataset/data_Label.txt') as f2:
	for x,y in zip(f1,f2):
		x=x[:-1] # delete 'enter'
		y=y[:-2] # delete 'enter + blank'
		temp = map(int,y.split(' ')) # string to array
		data[x]=temp # ID-Label
		counter+=1
		print counter


'''with open('../dataset/testVidID.txt') as f1,open('../dataset/testLabel.txt') as f2:
	for x,y in zip(f1,f2):
		x=x[:-1]
		y=y[:-2]
		temp = map(int,y.split(' '))
		data[x]=temp
		counter+=1
		print counter'''


with open('../dataset/merged_data.pickle','wb') as f4:
	pickle.dump(data,f4)