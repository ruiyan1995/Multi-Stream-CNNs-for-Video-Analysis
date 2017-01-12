import cv2
import pickle
import numpy as np


labelList=['brush_hair','cartwheel','catch','chew','clap','climb','climb_stairs','dive'
               ,'draw_sword','dribble','drink','eat','fall_floor','fencing','flic_flac','golf'
               ,'handstand','hit','hug','jump','kick','kick_ball','kiss','laugh'
               ,'pick','pour','pullup','punch','push','pushup','ride_bike','ride_horse'
               ,'run','shake_hands','shoot_ball','shoot_bow','shoot_gun','sit','situp','smile'
               ,'smoke','somersault','stand','swing_baseball','sword','sword_exercise','talk','throw'
               ,'turn','walk','wave']

def get_sample_data(chunk, img_row, img_col):
    X_train = []
    Y_train = []
    with open('../dataset/spatial_train_data_new.pickle', 'rb') as f1:
        spatial_train_data = pickle.load(f1)
    for imgname in chunk:
        idx = imgname.rfind('_')
        folder = imgname[:idx]
        filename = './sp_images' + '/' + folder + '/' + imgname + '.jpg'
        img = cv2.imread(filename)
        if img != None:
            img = np.rollaxis(cv2.resize(
                img, (img_row, img_col)).astype(np.float32), 2)
            X_train.append(img)  # get sample
            Y_train.append(spatial_train_data[imgname])  # get label

    X_train = np.asarray(X_train)
    Y_train = np.asarray(Y_train)
    return X_train, Y_train


def get_train_data(chunk, img_row, img_col):
    X_train = []
    Y_train = []
    with open('../dataset/spatial_train_data_new.pickle', 'rb') as f1:
        spatial_train_data = pickle.load(f1)
    try:
        for imgname in chunk:
            idx = imgname.rfind('_')
            folder = imgname[:idx]
            filename = './sp_images/' + labelList[spatial_train_data[imgname].index(1)] + '/' + folder + '/' + imgname + '.jpg'
            img = cv2.imread(filename)
            img = np.rollaxis(cv2.resize(img, (img_row, img_col)).astype(np.float32), 2)
            X_train.append(img)
            Y_train.append(spatial_train_data[imgname])

        X_train = np.asarray(X_train)
        Y_train = np.asarray(Y_train)
        return X_train, Y_train
    except:
        print filename
        X_train = None
        Y_train = None
        return X_train, Y_train


def get_test_data(chunk, img_row, img_col):
    X_train = []
    Y_train = []
    with open('../dataset/spatial_test_data.pickle', 'rb') as f1:
        spatial_test_data = pickle.load(f1)
    try:
        for imgname in chunk:
            
            idx = imgname.rfind('_')
            folder = imgname[:idx]
            filename = './sp_images/' + labelList[spatial_train_data[imgname].index(1)] + '/' + folder + '/' + imgname + '.jpg'
            if filename in testlist:
                img = cv2.imread(filename)
                img = np.rollaxis(cv2.resize(img, (img_row, img_col)).astype(np.float32), 2)
                X_train.append(img)
                Y_train.append(spatial_test_data[imgname])

        X_train = np.asarray(X_train)
        Y_train = np.asarray(Y_train)
        return X_train, Y_train
    except:
        X_train = None
        Y_train = None
        return X_train, Y_train

if __name__ == '__main__':
    get_data()
