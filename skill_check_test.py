from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QMainWindow, QHeaderView, QTableWidgetItem, QComboBox
from PySide6.QtCore import Qt, QUrl
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtGui import QIntValidator
from ui_main import Ui_MainWindow
import sys
import datetime
import cv2
import numpy as np
import numpy as np  # pip install numpy
import matplotlib.pyplot as plt # pip install matplotlib
import time
from data import skill_identity_data, skill_normal_data
from Class.skill_check_function import custom_skill_check_function
#from Class.skill_check import skill_check_function, stack_check_function#, q_check_function, a_check_function
from data import cooltime_check_s_data, cooltime_check_m_data, stack_zero_check_data, cooltime_check_Aeromancer_s_data, \
                 stack_one_check_data, stack_two_check_data, q_check_data, a_check_data, cutscene_check_data, \
                 cooltime_check_Gunslinger_s_data, cooltime_check_Glaivier_s_data


def skill_check_function(img, skill_check_data, skill_table, frame, cap):

    return



#cap = cv2.VideoCapture("D:/Lostark/T4창술/short.mp4", cv2.CAP_FFMPEG)

cap = cv2.VideoCapture("C:/Users/SON/Videos/Lost Ark/건슬_카던.mp4", cv2.CAP_FFMPEG) # 2100

#width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # 1920
#height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # 1080
fps = cap.get(cv2.CAP_PROP_FPS) # 60

skill_table = []

result =[]

roi_imshow = 0 # 0은 안보이고, 1은 보이기
graph = 0  # 0은 안그래프, 1은 그래프
roi_wait = 0 # 0은 멈춤 1은 재생

start_frame = 0 ###
end_frame = 2000 ##

height = 918
width = 528
h = 1080-height  # 162
w = 1104-width  # 576

if roi_imshow == 1:
    cv2.namedWindow('Video Player', cv2.WINDOW_NORMAL)  # WINDOW_NORMAL을 사용하여 창 크기 조절 가능하도록 설정
    cv2.resizeWindow('Video Player', 576*2, 162*2) #int(width*w), int(height*h) x=0.275; y=0.85; w=0.3; h=1-y   
    cv2.moveWindow('Video Player', 200, 200)   

selected_class = '건슬링어'
skill_check_data = {**skill_identity_data[selected_class], **skill_normal_data}   
frame = {'current': 0, 'check': 0, 'total': int(end_frame-start_frame), 'start':start_frame, 'end': end_frame}

cap.set(cv2.CAP_PROP_POS_FRAMES, frame['start'])
if cap.isOpened():                 # 캡쳐 객체 초기화 확인
    start_time = time.perf_counter()  # 처리 시작 시간 기록 
    standard_roi = None
    cutscene = False
    first_frame = True
    while True:
        ret, img = cap.read()      # 다음 프레임 읽기      --- ②
        if not ret:  # 프레임 읽기 실패 시 종료
            break
        frame['current'] = int(cap.get(cv2.CAP_PROP_POS_FRAMES))# current_frame

        # roi = img[918:1080, 528:1104]
        roi = img[height:height+h, width:width+w]

        ########################################################################################################################### 
        ########################################################################################################################### 
        ########################################################################################################################### 
        ########################################################################################################################### 
        #skill = skill_check_data['stance']
        #cv2.rectangle(roi, (skill['x'][0]-width-1, skill['y'][0]-height-1), (skill['x'][0]+skill['sizex'][0]-width, skill['y'][0]+skill['sizey'][0]-height), (0, 255, 0), thickness=1)
        #cv2.rectangle(roi, (skill['x'][1]-width-1, skill['y'][1]-height-1), (skill['x'][1]+skill['sizex'][1]-width, skill['y'][1]+skill['sizey'][1]-height), (0, 255, 0), thickness=1)
        #cv2.rectangle(roi, (skill['x'][2]-width-1, skill['y'][2]-height-1), (skill['x'][2]+skill['sizex'][2]-width, skill['y'][2]+skill['sizey'][2]-height), (0, 255, 0), thickness=1)
        #sroi1=img[skill['y'][0]:skill['y'][0]+skill['sizey'][0], skill['x'][0]:skill['x'][0]+skill['sizex'][0]]
        #sroi2=img[skill['y'][1]:skill['y'][1]+skill['sizey'][1], skill['x'][1]:skill['x'][1]+skill['sizex'][1]]
        #sroi3=img[skill['y'][2]:skill['y'][2]+skill['sizey'][2], skill['x'][2]:skill['x'][2]+skill['sizex'][2]]
        
        #sroi=img[skill['y']:skill['y']+skill['sizey'], skill['x']:skill['x']+skill['sizex']]
        #cv2.rectangle(roi, (skill['x']-width-1, skill['y']-height-1), (skill['x']+skill['sizex']-width, skill['y']+skill['sizey']-height), (0, 255, 0), thickness=1)

        name = 'stance'
        skill = skill_check_data[name]
        sroi1=img[skill['y'][0]:skill['y'][0]+skill['sizey'][0], skill['x'][0]:skill['x'][0]+skill['sizex'][0]]
        sroi2=img[skill['y'][1]:skill['y'][1]+skill['sizey'][1], skill['x'][1]:skill['x'][1]+skill['sizex'][1]]
        sroi3=img[skill['y'][2]:skill['y'][2]+skill['sizey'][2], skill['x'][2]:skill['x'][2]+skill['sizex'][2]]
        cv2.rectangle(roi, (skill['x'][0]-width-1, skill['y'][0]-height-1), (skill['x'][0]+skill['sizex'][0]-width, skill['y'][0]+skill['sizey'][0]-height), (0, 255, 0), thickness=1)
        cv2.rectangle(roi, (skill['x'][1]-width-1, skill['y'][1]-height-1), (skill['x'][1]+skill['sizex'][1]-width, skill['y'][1]+skill['sizey'][1]-height), (0, 255, 0), thickness=1)
        cv2.rectangle(roi, (skill['x'][2]-width-1, skill['y'][2]-height-1), (skill['x'][2]+skill['sizex'][2]-width, skill['y'][2]+skill['sizey'][2]-height), (0, 255, 0), thickness=1)
        mean1 = cv2.mean(sroi1)[:3]
        mean2 = cv2.mean(sroi2)[:3]
        #mean3 = cv2.mean(sroi3)[:3]
        mean = [mean1,mean2]#,mean3]
        mean_list = [item for tup in mean for item in tup]
        hand_ref = 10; shot_ref = 10; rifle_ref = 10
        hand  = [105,  67,  33,  31, 180, 234 ]#,  82,  31,  85]
        shot  = [ 86,  31,  86, 243, 204,  45 ]#,  31,  59,  91]
        rifle = [ 32,  59,  90, 248,  19, 197 ]#, 108,  71,  33]

        hand2  = [ 81,  31,  85,  30, 180, 235 ]
        rifle2 = [ 32,  59,  90, 248,  19, 198 ]

        if all(abs(m - h) < hand_ref for m, h in zip(mean_list, hand)) and skill['state'] != 'hand' :
            skill_table.append([frame['current'], 'hand'])
            skill['state']='hand'
        if all(abs(m - h) < shot_ref for m, h in zip(mean_list, shot)) and skill['state'] != 'shot' :
            skill_table.append([frame['current'], 'shot'])
            skill['state']='shot'
        if all(abs(m - h) < rifle_ref for m, h in zip(mean_list, rifle)) and skill['state'] != 'rifle' :
            skill_table.append([frame['current'], 'rifle'])
            skill['state']='rifle'
        elif all(abs(m - h) < hand_ref for m, h in zip(mean_list, hand2)) : # 사시에서 hand 면 1프레임 늦음
            skill_table.append([frame['current'], 'hand'])
            skill['state']='hand'
    
        result.append( [mean1, mean2]  )

        if skill['state']=='clicked':
            skill_table.append([frame['current'], name])

        ########################################################################################################################### 
        ########################################################################################################################### 
        ########################################################################################################################### 
        ########################################################################################################################### 

        if roi_imshow == 1:
            cv2.imshow('Video Player', roi)
        if roi_wait == 0:
            cv2.waitKey()
        if cv2.waitKey(int(1000/fps)) & 0xFF == ord('q'):
            break
        if int(frame['end']) <= frame['current']:
            break
        #if int(end_frame) == int(cap.get(cv2.CAP_PROP_POS_FRAMES)):
        #    break
    print(skill_table)
    end_time = time.perf_counter()  # 처리 끝난 시간 기록

    # 처리 시간 계산
    processing_time = end_time - start_time
    print(f"Frame processing time: {processing_time:.4f} seconds")

else:
    print("can't open video.")
cap.release()
cv2.destroyAllWindows()
# print(skill_table)
# print(result)

with open('output.txt', 'w') as f:
    for i in range(len(result)):
        f.write(f'{i+1}, {result[i]} \n')

if graph  == 1:
    plt.plot(result, 'r.', label='r')
    #plt.plot(result1, 'g.', label='g')
    #plt.plot(result2, 'b.', label='b')

    plt.legend();plt.show()


