#encoding: utf-8
import scandir
import numpy as np
def CreateID_Label(root):
    
    # labelList for HMDB
    labelList=['brush_hair','cartwheel','catch','chew','clap','climb','climb_stairs','dive'
               ,'draw_sword','dribble','drink','eat','fall_floor','fencing','flic_flac','golf'
               ,'handstand','hit','hug','jump','kick','kick_ball','kiss','laugh'
               ,'pick','pour','pullup','punch','push','pushup','ride_bike','ride_horse'
               ,'run','shake_hands','shoot_ball','shoot_bow','shoot_gun','sit','situp','smile'
               ,'smoke','somersault','stand','swing_baseball','sword','sword_exercise','talk','throw'
               ,'turn','walk','wave']
    labelDict = dict()
    label = ''
    for i in range(len(labelList)):
        labelDict[labelList[i]]=i
        label = label + "0 "
    #print labelDict
    
    # clear files
    f=open("../dataset/ID.txt",'w')
    f.truncate()
    f=open("../dataset/Label.txt",'w')
    f.truncate()
    
    # traverse folder
    for path, subdsirs, files in scandir.walk(root):
        for filename in files:
            ID = filename.split('.')[0]
            labelName = path[path.rfind("/")+1:]
            with open("../dataset/ID.txt", "a") as myfile:
                myfile.write(ID + '\n')

            try:
                LabelIndex = labelDict[labelName]*2
                Label = label[:LabelIndex] + '1' + label[LabelIndex+1:]
            except Exception:
                print "Cannot find this labelName:"+labelName
                return
            with open("../dataset/Label.txt", "a") as myfile:
                myfile.write(Label + '\n')  
if __name__ == "__main__":
    root='/media/yanrui/文档/迅雷下载/Two-Stream/hmdb51_org/video/'
    CreateID_Label(root)
    
    