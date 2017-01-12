#encoding: utf-8
from __future__ import unicode_literals
import sys,os
import youtube_dl
rootpath='/home/yanrui/桌面/Video-Classification-2-Stream-CNN-master/'
savepath='/media/yanrui/文档/迅雷下载/Two-Stream/YouTube/'
netPath='https://www.youtube.com/watch?v='
class MyLogger(object):
	def debug(self, msg):
		pass

	def warning(self, msg):
		pass

	def error(self, msg):
		print(msg)


def my_hook(d):
	if d['status'] == 'finished':
		print('Done downloading\n\n\n')
	if d['status'] == 'downloading':
		print 'Video count: ' + str(count) + '\tVideo title: ' + str(d['filename']) + '\tETA: ' + str(d['eta'])

name='starting'
ydl_opts = {
	'format': 'mp4',
	'ignoreerrors': True,
	'outtmpl': name,
	'logger': MyLogger(),
	'progress_hooks': [my_hook],
}
os.chdir(savepath+'train')
count=0
with open(rootpath+'dataset/trainVidID.txt') as f:
	for i,vidId in enumerate(f):
		vidId=vidId[:-1]
		ydl_opts['outtmpl']=vidId+''
		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
			try:
				count+=1
				print netPath+vidId
				ydl.download([netPath+vidId])

			except:
				print sys.exc_info()[0]

os.chdir(savepath+'videos/test')
count=0
with open(rootpath+'dataset/testVidID.txt') as f:
	for i,vidId in enumerate(f):
		vidId=vidId[:-1]
		ydl_opts['outtmpl']=vidId+''
		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
			try:
				count+=1
				ydl.download([netPath+vidId])
			except:
				print sys.exc_info()[0]
