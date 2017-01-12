# encoding:utf:8
import random
import pickle
data_ID = []
data_Label = []

'''# split the dataset into trainset and testset randomly
def splitData(IDfile,Labelfile,ratio):
    # IDfile: the file path of data ID
    # Labelfile: the file path of data Label
    # ratio: the ratio of training set and testing set
    with open(IDfile) as f1,open(Labelfile) as f2:
        for ID,Label in zip(f1,f2):
            data_ID.append(ID)
            data_Label.append(Label)
    lines = len(data_ID)
    random_ID=random.sample(range(0,lines),lines)
    threshold = lines*ratio #
    train_ID = random_ID[:threshold]
    test_ID = random_ID[threshold:]       
    for i in train_ID:
        with open("../dataset/trainID.txt", "a") as trainID,open("../dataset/trainLabel.txt", "a") as trainLabel:
            trainID.write(data_ID[i])
            trainLabel.write(data_Label[i])
        
    for i in test_ID:
        with open("../dataset/testID.txt", "a") as testID,open("../dataset/testLabel.txt", "a") as testLabel:
            testID.write(data_ID[i])
            testLabel.write(data_Label[i])'''

train_data = {}
test_data = {}


def splitData(IDfile, Labelfile, Train_data_file, Test_data_file, Merged_data_file, ratio):
    # IDfile: the file path of data ID
    # Labelfile: the file path of data Label
    # ratio: the ratio of training set and testing set
    with open(IDfile) as f1, open(Labelfile) as f2:
        for ID, Label in zip(f1, f2):
            data_ID.append(ID)
            data_Label.append(Label)
    lines = len(data_ID)
    random_ID = random.sample(range(0, lines), lines)
    threshold = (int)(lines * ratio)
    #print threshold
    train_ID = random_ID[:threshold]
    test_ID = random_ID[threshold:]
    for i in train_ID:
        x = data_ID[i]
        y = data_Label[i]
        x = x[:-1]  # delete 'enter'
        y = y[:-2]  # delete 'enter + blank'
        temp = map(int, y.split(' '))  # string to array
        train_data[x] = temp  # ID-Label

    for i in test_ID:
        x = data_ID[i]
        y = data_Label[i]
        x = x[:-1]  # delete 'enter'
        y = y[:-2]  # delete 'enter + blank'
        temp = map(int, y.split(' '))  # string to array
        test_data[x] = temp  # ID-Label

    with open(Train_data_file,'wb') as f3, open(Test_data_file,'wb') as f4, open(Merged_data_file,'wb') as f5:
        pickle.dump(train_data, f3)
        pickle.dump(test_data, f4)
        pickle.dump(dict(train_data, **test_data), f5)

if __name__ == "__main__":
    # clear files
    '''f = open("../dataset/testID.txt", 'w')
    f.truncate()
    f = open("../dataset/trainID.txt", 'w')
    f.truncate()
    f = open("../dataset/testLabel.txt", 'w')
    f.truncate()
    f = open("../dataset/trainLabel.txt", 'w')
    f.truncate()'''

    IDfile = '../dataset/data_ID.txt'
    Labelfile = '../dataset/data_Label.txt'
    Train_data_file = '../dataset/train_data.pickle'
    Test_data_file = '../dataset/test_data.pickle'
    Merged_data_file = '../dataset/merged_data.pickle'
    splitData(IDfile, Labelfile, Train_data_file, Test_data_file, Merged_data_file, 0.9)
