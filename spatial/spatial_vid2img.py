# encoding: utf-8
import numpy as np
import cv2
import sys
import os
import pickle
import shutil
import gc
import scandir


def write_images():

    root = '/media/yanrui/文档/迅雷下载/Two-Stream/hmdb51_org/video'

    # with open('../dataset/merged_data.pickle', 'rb') as f:
    #    var1 = pickle.load(f)

    for path, subdirs, files in scandir.walk(root):

        for filename in files:
            # print  path[path.rfind("/"):]
            folder = './sp_images' + \
                path[path.rfind("/"):] + '/' + filename.split('.')[0] + '/'
            # print folder
            if not os.path.isdir(folder):
                os.makedirs(folder)
            else:
                shutil.rmtree(folder)
                os.mkdir(folder)
            try:
                cnt = 0
                full_path = path + '/' + filename
                cap = cv2.VideoCapture(full_path)
                #fcnt = 1

                while(cap.isOpened()):
                    ret, frame = cap.read()
                    if frame == None:
                        break

                    fpath = './sp_images'
                    vid_name = filename.split('.')[0]
                    img_path = folder + vid_name + '_{}.jpg'.format(cnt + 1)
                    img_name = vid_name + '_{}'.format(cnt + 1)
                    # if fcnt % 10 == 0:
                    print img_name
                    cv2.imwrite(img_path, frame)
                    cnt = cnt + 1
                    #fcnt += 1

                if cnt:
                    with open("count.txt", "a") as txt:
                        text = str(cnt) + " " + img_name.split('.')[0] + "\n"
                        txt.write(text)
                cap.release()
                cv2.destroyAllWindows()
            except e:
                with open("logfile.txt", "a") as h:
                    h.write(e)
                print "Some Error happened"
                cap.release()
                cv2.destroyAllWindows()


def data_prep():

    root = './sp_images/'
    path = os.path.join(root, "")

    with open('../dataset/merged_data.pickle', 'rb') as f:
        var1 = pickle.load(f)
    dic = {}
    vidno = 0

    for path, subdirs, files in os.walk(root):
        for filename in files:
            frame_name = filename.split('.')[0]
            idx = frame_name.rfind('_')
            vidname = frame_name[:idx]
            print frame_name
            print vidname
            dic[frame_name] = var1[vidname]

        vidno += 1

    print dic
    with open('../dataset/spatial_train_data_new.pickle', 'w') as f:
        pickle.dump(dic, f)

if __name__ == "__main__":
    f = open("count.txt", 'w')
    f.truncate()
    f = open("logfile.txt", 'w')
    f.truncate()
    # write_images()
    # gc.collect()
    data_prep()
