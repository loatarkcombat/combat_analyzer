from PySide6.QtWidgets import QApplication, QLabel#, QWidget, QFileDialog, QMainWindow, QHeaderView, QTableWidgetItem, QComboBox, QProgressBar, QTableWidget
#from PySide6.QtCore import Qt, QUrl, QThread, Signal, QTimer
#from PySide6.QtMultimedia import QMediaPlayer
#from PySide6.QtGui import QIntValidator
#from ui_main import Ui_MainWindow
#import sys
#import datetime
import cv2
import numpy as np
#import matplotlib.pyplot as plt # pip install matplotlib
#import json

import copy
import time
from data import skill_identity_data, skill_normal_data, cutscene_check_data
from Class.skill_check_function import stack_check_function, General_skill_check_function
from Class.Sorceress import Sorceress_skill_check_function
from Class.Gunslinger import Gunslinger_skill_check_function
from Class.Glaivier import Glaivier_skill_check_function
from Class.Aeromancer import Aeromancer_skill_check_function
from Class.Deathblade import Deathblade_skill_check_function


def skill_analysis_function(file,selected_class,start_frame,end_frame,label: QLabel):
    cap = cv2.VideoCapture(file, cv2.CAP_FFMPEG) # 동영상 캡쳐 객체 생성  ---①
    #동영상 정보 (임시)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # 1920
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # 1080
    fps = float(cap.get(cv2.CAP_PROP_FPS)) # 60
    # frame , check는 진행률 확인용
    frame = {'current': 0, 'check': 0, 'total': int(end_frame-start_frame), 'start':start_frame, 'end': end_frame}
    #필요 변수 정의
    skill_table =[] #스킬 결과 테이블  [프레임, 스킬명]
    first_cutscene_check = False
    cutscene_roi1 = None
    cutscene_roi2 = None
    cutscene = False
    cutscene_table = []
    skill_check_data = {  **copy.deepcopy(skill_identity_data[selected_class]), **copy.deepcopy(skill_normal_data)  }   
    for name, skill in skill_check_data.items(): #다시 눌르면 전에꺼 삭제
        skill['prev'] = []

    cap.set(cv2.CAP_PROP_POS_FRAMES, frame['start']) #프레임 이동
    if cap.isOpened():                 # 캡쳐 객체 초기화 확인
        start_time = time.perf_counter()  # 처리 시작 시간 기록 
        while True:
            ret, img = cap.read()      # 다음 프레임 읽기      --- ②
            if not ret:  # 프레임 읽기 실패 시 종료
                break
            frame['current'] = int(cap.get(cv2.CAP_PROP_POS_FRAMES))# current_frame
            #컷신 체크
            if first_cutscene_check is False: #첫프레임 기준 잡기
                cutscene_roi = cv2.cvtColor(img[12:17, 36:41], cv2.COLOR_BGR2GRAY)
                zero_values = cutscene_roi[cutscene_check_data == 0] ; one_values = cutscene_roi[cutscene_check_data == 1]
                zero_mean = np.mean(zero_values) ; one_ratio = np.sum(one_values > 180) / len(one_values)
                if zero_mean < 50 and one_ratio == 1 :
                    first_cutscene_check = True
                    for name, skill in skill_check_data.items(): # cutscene_roi1 is None 때문에 한번만 실행 -->  stack check
                        if name in ['q', 'w', 'e', 'r', 'a', 's', 'd', 'f', 't']:
                            sroi=img[skill['y']:skill['y']+skill['sizey'], skill['x']:skill['x']+skill['sizex']]
                            skill_state, skill_type = stack_check_function(sroi, skill['state'], skill['type'])# stack 스킬 확인 # skill_type
                            skill_check_data[name]['state'] = 'cooltime'
                            skill_check_data[name]['type'] = skill_type

            else: #그밖에 프레임 컷신 확인
                cutscene_roi = cv2.cvtColor(img[12:17, 36:41], cv2.COLOR_BGR2GRAY)
                zero_values = cutscene_roi[cutscene_check_data == 0] ; one_values = cutscene_roi[cutscene_check_data == 1]
                zero_mean = np.mean(zero_values) ; one_ratio = np.sum(one_values > 180) / len(one_values)
                if not (zero_mean < 50 and one_ratio == 1) and cutscene == False:
                    cutscene_table.append([int(cap.get(cv2.CAP_PROP_POS_FRAMES)), '컷신시작'])
                    cutscene = True
                    continue
                elif zero_mean < 50 and one_ratio == 1 and cutscene == True:
                    cutscene_table.append([int(cap.get(cv2.CAP_PROP_POS_FRAMES)), '컷신끝'])
                    cutscene = False


            # if cutscene_roi1 is None: #첫프레임 기준 잡기
            #     cutscene_roi1 =  cv2.Laplacian(cv2.cvtColor(img[1080-29:1080-11, 10:29], cv2.COLOR_BGR2GRAY), -1)   # 1080-29:1080-11, 10:60
            #     cutscene_roi2 =  cv2.Laplacian(cv2.cvtColor(img[1080-29:1080-11, 157:178], cv2.COLOR_BGR2GRAY), -1)  #1080-29:1080-11, 157:221
            #     for name, skill in skill_check_data.items(): #cutscene_roi1 is None 때문에 한번만 실행 -->  stack check
            #         if name in ['q', 'w', 'e', 'r', 'a', 's', 'd', 'f', 't']:
            #             sroi=img[skill['y']:skill['y']+skill['sizey'], skill['x']:skill['x']+skill['sizex']]
            #             skill_state, skill_type = stack_check_function(sroi, skill['state'], skill['type'])# stack 스킬 확인 # skill_type
            #             skill_check_data[name]['state'] = skill_state
            #             skill_check_data[name]['type'] = skill_type
            # else: #그밖에 프레임 컷신 확인
            #     diffs1 = cv2.absdiff(cv2.Laplacian(cv2.cvtColor(img[1080-29:1080-11, 10:29], cv2.COLOR_BGR2GRAY), -1), cutscene_roi1)
            #     diff_sum1 = sum(cv2.sumElems(diffs1))
            #     diffs2 = cv2.absdiff(cv2.Laplacian(cv2.cvtColor(img[1080-29:1080-11, 157:178], cv2.COLOR_BGR2GRAY), -1), cutscene_roi2)
            #     diff_sum2 = sum(cv2.sumElems(diffs2))
            #     if not (diff_sum1 < 7000 or diff_sum2 < 7000) and cutscene == False: 
            #         cutscene_table.append([int(cap.get(cv2.CAP_PROP_POS_FRAMES)), '컷신시작'])
            #         cutscene = True
            #         continue
            #     elif not (diff_sum1 > 7000 or diff_sum2 > 7000)  and cutscene == True:
            #         cutscene_table.append([int(cap.get(cv2.CAP_PROP_POS_FRAMES))-1, '컷신끝'])
            #         cutscene = False
            

        ########################################################################################################################### 
        ########################################################################################################################### 
        ########################################################################################################################### 
        ########################################################################################################################### 

            # 스킬 사용 체크
            if cutscene == False:  #컷신은 스킬 체크 안함 
                # input : img skill_check_data skill_table frame cap
                if selected_class =='소서리스':
                    Sorceress_skill_check_function(img, skill_check_data, skill_table, frame)
                #elif 타직업
                elif selected_class =='기상술사':
                    Aeromancer_skill_check_function(img, skill_check_data, skill_table, frame)
                elif selected_class =='창술사':
                    Glaivier_skill_check_function(img, skill_check_data, skill_table, frame)
                elif selected_class =='블레이드':
                    Deathblade_skill_check_function(img, skill_check_data, skill_table, frame)
                elif selected_class =='건슬링어':
                    Gunslinger_skill_check_function(img, skill_check_data, skill_table, frame)
                elif selected_class =='공용직업':
                    General_skill_check_function(img, skill_check_data, skill_table, frame)

                    


        ########################################################################################################################### 
        ########################################################################################################################### 
        ########################################################################################################################### 
        ########################################################################################################################### 

            #진행률 업데이트
            frame['check'] += 1
            progress = int((frame['check'] / (frame['total'])) * 100)
            if progress > 100: progress=100
            label.setText(f'{progress}%')  
            QApplication.processEvents() #진행률 업데이트용
            #동영상 종료
            if int(frame['end']) <= frame['current']:
                break
            #frame_number = frame['current']  - 1
            #cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)

        end_time = time.perf_counter()  # 처리 끝난 시간 기록
        # 처리 시간 계산
        processing_time = end_time - start_time
        print(f"Frame processing time: {processing_time:.4f} seconds")

    else:
        print("can't open video.")
    cap.release()
    cv2.destroyAllWindows()

    return skill_table, cutscene_table, fps
