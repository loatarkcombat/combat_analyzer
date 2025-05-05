#from PySide6.QtWidgets import QMainWindow
from ui_analysis import Ui_analysis  # PySide6-Designer로 만든 UI 연결
from PySide6.QtWidgets import QFileDialog, QGraphicsView, QGraphicsScene, QGraphicsRectItem, QGraphicsTextItem, QFrame, QGraphicsItemGroup, QGraphicsLineItem, QDialog, QButtonGroup#, QApplication, QVBoxLayout, QWidget, QLabel
from PySide6.QtCore import Qt#, QRectF
from PySide6.QtGui import QPen, QPainter, QFont, QColor, QBrush, QIntValidator
import json
#import os
#import sys
import re
from data import skill_speed, rune_speed, skill_identity_data
from Class.skill_check_function import General_analysis_function
from Class.Sorceress import Sorceress_analysis_function
from Class.Gunslinger import Gunslinger_analysis_function
from Class.Glaivier import Glaivier_analysis_function
from Class.Aeromancer import Aeromancer_analysis_function
from Class.Deathblade import Deathblade_analysis_function


from functools import partial

class TimelineEventItem(QGraphicsRectItem):
    def __init__(self, x, y, width, height, name):
        super().__init__(x, y, width, height)

        if name == 'q' or name == '/q': self.setBrush(Qt.darkRed)
        elif name == 'w' or name == '/w': self.setBrush(Qt.darkGreen)
        elif name == 'e' or name == '/e': self.setBrush(Qt.darkBlue)
        elif name == 'r' or name == '/r': self.setBrush(Qt.darkCyan)
        elif name == 'a' or name == '/a': self.setBrush(Qt.red)
        elif name == 's' or name == '/s': self.setBrush(Qt.green)
        elif name == 'd' or name == '/d': self.setBrush(Qt.blue)
        elif name == 'f' or name == '/f': self.setBrush(Qt.cyan)
        elif name == 't': self.setBrush(Qt.magenta)
        elif name == 'v': self.setBrush(Qt.yellow)
        elif name == 'z' or name == 'z1' or name == 'z2' or name == 'z3': self.setBrush(Qt.darkMagenta)
        elif name == 'x' or name == 'x1' or name == 'x2' or name == 'x3': self.setBrush(Qt.darkYellow)
        elif name == 'nak': self.setBrush(Qt.gray)
        elif name == 'veff': self.setBrush(Qt.gray)
        elif name == 'ad1' or name == 'ad2' or name == 'ad3' or name == 'ad4' or name == 'ad5' or name == 'ad6': self.setBrush(Qt.gray)
        elif name == '컷신': self.setBrush(QBrush(Qt.red))

        if not (name == '컷신'):
            self.text = QGraphicsTextItem(name, self)
            self.text.setDefaultTextColor(Qt.white)
            self.text.setPos(x-2, y)  # 텍스트 위치
            if name == 'f' or name =='s'or name =='v' or name == '/f' or name =='/s'or name =='/v':
                self.text.setDefaultTextColor(Qt.black)

        #self.setFlags(QGraphicsRectItem.ItemIsMovable | QGraphicsRectItem.ItemIsSelectable)

        self.setFlags(QGraphicsRectItem.ItemIsSelectable)
        self.setPen(QPen(Qt.transparent))  # 테두리 없음

class TimelineView(QGraphicsView):
    def __init__(self, Pattern_table_data, skill_time_table):
        super().__init__()
        # 타임라인을 담을 QGraphicsScene 생성
        self.scenes = QGraphicsScene()
        self.setScene(self.scenes)
        self.setFrameShape(QFrame.NoFrame)

        # 시간 축 생성 (가로 막대)
        self.ini_frame=int(Pattern_table_data[0][0])
        self.last_farme=int(Pattern_table_data[-1][0])

        time_height = 40
        label_width = 100
        interval = 25
        pps = 60 # 초당 픽셀
        self.draw_time_axis(label_width, time_height, pps)

        time_table_labels = ['q', 'w', 'e', 'r', 'a', 's', 'd', 'f', 't', 'v', 'z', 'x', 'nak', 'veff', 'ad']
        n =  1 + len(time_table_labels)
        view_heigh = time_height + interval * n

        # 뷰포트 설정
        self.setRenderHint(QPainter.Antialiasing)  # 수정된 부분: QPainter.Antialiasing을 사용
        self.setSceneRect(0, 0, int(self.last_farme-self.ini_frame)+label_width+pps, view_heigh) 
        
        # 수평 라인 추가 
        lines_y_positions = list(range(time_height, time_height + interval * n, interval)) #[40, 70, 100, 130, 160, 190, 220, 250, 280, 310, 340]
        for y in lines_y_positions:
            color = Qt.black if y == time_height else Qt.gray
            self.scenes.addLine(0, y, self.last_farme - self.ini_frame + label_width, y, QPen(color))

        # 이벤트 추가
        for pattern_table in Pattern_table_data:
            if pattern_table[1] == '컷신시작':
                self.cutstart = pattern_table[0]
            elif pattern_table[1] == '컷신끝':
                self.add_event(int(self.cutstart) - self.ini_frame + label_width, time_height, int(pattern_table[0]) - int(self.cutstart) - 1, interval, '컷신')
        
        skill_y_mapping = {
            key: time_height + index * interval
            for index, key in enumerate(time_table_labels, start=1)
        }
        for skill in skill_time_table:
            name = re.sub(r'\d+$', '', re.sub(r'^/', '', skill[2])  )  
            if name in skill_y_mapping:
                y = skill_y_mapping[name]
                self.add_event(int(skill[0]) - self.ini_frame + label_width, y, int(skill[1])- int(skill[0]), interval, skill[2])

        # 텍스트 그룹 추가
        self.text_group = QGraphicsItemGroup()
        labels = ['시간', '컷신'] + time_table_labels
        font = QFont()
        font.setPixelSize(int(interval/2))  # 픽셀 단위 크기 설정

        for idx, label in enumerate(labels):
            y = time_height + (idx -1)* interval
            text_item = QGraphicsTextItem(label)
            text_item.setFont(font)
            text_item.setPos(0, y)
            self.text_group.addToGroup(text_item)

        # 라인 추가 (텍스트 그룹용)
        for y in lines_y_positions:
            color = QColor("black") if y == time_height else QColor("gray")
            line = QGraphicsLineItem(0, y, label_width, y)
            line.setPen(QPen(color, 1))
            self.text_group.addToGroup(line)

        background_rect = QGraphicsRectItem(0, 0, label_width, view_heigh)  # 크기 조정
        background_rect.setBrush(QColor("white"))  # 배경색 흰색
        background_rect.setPen(QPen(Qt.transparent))  # 테두리 없음
        background_rect.setZValue(-1)  # 텍스트 아래에 배치
        self.text_group.addToGroup(background_rect)
        
        line = QGraphicsLineItem(label_width, 0, label_width, view_heigh)  # 시작점 (0, 0)에서 끝점 (200, 0)
        line.setPen(QPen(QColor("black"), 2))  # 검은색, 두께 2의 선
        self.text_group.addToGroup(line)

        self.scenes.addItem(self.text_group)
        self.text_group.setPos(0, 0)

        # 스크롤바의 valueChanged 시그널에 슬롯 연결
        self.verticalScrollBar().valueChanged.connect(self.update_fixed_item_position)
        self.horizontalScrollBar().valueChanged.connect(self.update_fixed_item_position)

    def update_fixed_item_position(self):
        # 현재 뷰의 스크롤 위치를 가져와서 고정 아이템 위치 업데이트
        scroll_x = self.horizontalScrollBar().value()
        # 아이템의 위치를 스크롤 위치에 맞춰 조정
        self.text_group.setPos(0 + scroll_x, 0)


    def draw_time_axis(self, label_width, time_height, pps):
        # 시간 축 그리기 (가로 라인)
        pen = QPen(Qt.black)  # 선을 그리기 위한 펜
        time_font = QFont()
        time_font.setPixelSize(int(time_height/4))  # 픽셀 단위 크기 설정
        for i in range(0, int(self.last_farme-self.ini_frame), pps):  # 60 픽셀 간격으로 선을 그림  #1초 간격 6픽셀
            self.scenes.addLine(i+label_width, int(time_height/2), i+label_width, time_height, pen)  # 세로 시간 눈금
            time_label = QGraphicsTextItem(f"{i // pps}s")  # 시간 라벨 (초)
            time_label.setPos(i+label_width, 0)
            time_label.setFont(time_font)
            self.scenes.addItem(time_label)
            frame_label = QGraphicsTextItem(f"{i+self.ini_frame}")  # 시간 라벨 (초)
            frame_label.setPos(i+label_width, int(time_height/2))
            frame_label.setFont(time_font)
            self.scenes.addItem(frame_label)

    def add_event(self, x, y, width, height, name):
        # 타임라인에 이벤트 추가
        event = TimelineEventItem(x, y, width, height, name)
        self.scenes.addItem(event)

class Ui_Analysis(QDialog): # Skill_table_data 오름차순 정리 후 받음
    def __init__(self, selected_class, Pattern_table_data, Skill_table_data, fps):
    #def __init__(self):
        super().__init__()
        self.ui = Ui_analysis()
        self.ui.setupUi(self)
        self.setWindowTitle("Analysis")
        self.timeline_view = None
        self.setWindowFlags(self.windowFlags() | Qt.WindowMinMaxButtonsHint)
        self.fps = fps
        #current_dir = os.getcwd()
        #current_dir = os.path.dirname(os.path.abspath(__file__))  # 현재 파일의 절대 경로
        #file_path = os.path.join(current_dir, 'skill.json')
        #with open(file_path, 'r') as f:
        #    self.skill_speed_data = json.load(f)
        self.skill_speed = skill_speed
        
        self.Pattern_table_data = Pattern_table_data
        self.Skill_table_data = Skill_table_data

        for key in ['q', 'w', 'e', 'r', 'a', 's', 'd', 'f', 't', 'v']:
            getattr(self.ui, f"{key}_combo").view().setMinimumWidth(300)

        for key in ['q', 'w', 'e', 'r', 'a', 's', 'd', 'f']:
            combo = getattr(self.ui, f"{key}_rune_combo")
            combo.addItems(rune_speed.keys())
            combo.view().setMinimumWidth(100)

        self.ui.speed_line.setText('100')

        self.ui.class_combo.addItems(self.skill_speed.keys())
        self.ui.class_combo.setCurrentText(selected_class)

        self.skill_list, self.skill_setting, self.skill_damge = self.initial_skill_list()  ## 스탠스에 따라 스킬 리스트 및 갯수정의
        self.initial_skill_setting() #클래스에 따른 스킬콤보 박스 초기 세팅

        self.ui.nak1_combo.addItems(sum([['-'],self.skill_list,['z','x']],[]))
        self.ui.nak2_combo.addItems(sum([['-'],self.skill_list,['z','x']],[]))

        self.ui.veff1_combo.addItems(sum([['-'],self.skill_list,['z','x']],[]))
        self.ui.veff2_combo.addItems(sum([['-'],self.skill_list,['z','x']],[]))

        self.ui.stance1_check.setChecked(True)
        self.ui.stance2_check.setChecked(False)

        self.ui.stance1_check.stateChanged.connect(self.stance_check_changed)
        self.ui.stance2_check.stateChanged.connect(self.stance_check_changed)

        self.ui.class_combo.currentTextChanged.connect(self.initial_skill_setting)

        self.ui.btn_analysis.clicked.connect(self.analysis)
        self.ui.btn_damage.clicked.connect(self.damage_analysis)
        self.ui.btn_load.clicked.connect(self.load_setting)
        self.ui.btn_save.clicked.connect(self.save_setting)
        
        for key in ['q', 'w', 'e', 'r', 'a', 's', 'd', 'f', 't', 'v']: 
            combo = getattr(self.ui, f"{key}_combo")
            combo.currentTextChanged.connect(lambda _, k=key: self.skill_change(k))

        for key in ['q', 'w', 'e', 'r', 'a', 's', 'd', 'f']: 
            rune_combo = getattr(self.ui, f"{key}_rune_combo")
            rune_combo.currentTextChanged.connect(lambda _, k=key: self.skill_change(k))

        for key in ['q', 'w', 'e', 'r', 'a', 's', 'd', 'f', 't', 'v', 'z', 'z1', 'z2', 'z3', 'x', 'x1', 'x2', 'x3']: 
            dmg_line = getattr(self.ui, f"dmg_{key}_line")
            dmg_line.textChanged.connect(lambda _, k=key: self.damge_change(k))

    def damge_change(self, key):
        if key in ['t','v', 'z', 'z1', 'z2', 'z3', 'x', 'x1', 'x2', 'x3']:
            dmg_line = getattr(self.ui, f"dmg_{key}_line")
            self.skill_damge[key] = dmg_line.text()
        elif self.ui.stance1_check.isChecked():
            if key in ['q', 'w', 'e', 'r', 'a','s','d','f']:
                dmg_line = getattr(self.ui, f"dmg_{key}_line")
                self.skill_damge[key] = dmg_line.text()
        elif self.ui.stance2_check.isChecked():
            if key in ['q', 'w', 'e', 'r', 'a','s','d','f']:
                dmg_line = getattr(self.ui, f"dmg_{key}_line")
                self.skill_damge[f"/{key}"] = dmg_line.text()

    def skill_change(self, key):
        if key in ['t','v']:
            combo = getattr(self.ui, f"{key}_combo")
            self.skill_setting[key] = [combo.currentText(), '-']
        elif self.ui.stance1_check.isChecked():
            if key in ['q', 'w', 'e', 'r', 'a','s','d','f']:
                combo = getattr(self.ui, f"{key}_combo")
                rune_combo = getattr(self.ui, f"{key}_rune_combo")
                self.skill_setting[key] = [combo.currentText(), rune_combo.currentText()]

        elif self.ui.stance2_check.isChecked():
            if key in ['q', 'w', 'e', 'r', 'a','s','d','f']:
                combo = getattr(self.ui, f"{key}_combo")
                rune_combo = getattr(self.ui, f"{key}_rune_combo")
                self.skill_setting[f"/{key}"] = [combo.currentText(), rune_combo.currentText()]
        
    def stance_check_changed(self, state):
        sender = self.sender()
        if state == 2:
            if sender == self.ui.stance1_check:
                self.ui.stance2_check.setChecked(False)
                for key in ['q', 'w', 'e', 'r', 'a', 's', 'd', 'f']:
                    getattr(self.ui, f"{key}_combo").setCurrentText(self.skill_setting[key][0])
                    getattr(self.ui, f"{key}_rune_combo").setCurrentText(self.skill_setting[key][1])
                    getattr(self.ui, f"dmg_{key}_line").setText(self.skill_damge[key])
                    getattr(self.ui, f"dmg_{key}_label").setText(f'{key}')
            elif sender == self.ui.stance2_check:
                self.ui.stance1_check.setChecked(False)
                for key in ['q', 'w', 'e', 'r', 'a', 's', 'd', 'f']:
                    value = self.skill_setting[f"/{key}"]
                    value2 = self.skill_damge[f"/{key}"]
                    getattr(self.ui, f"{key}_combo").setCurrentText(value[0])
                    getattr(self.ui, f"{key}_rune_combo").setCurrentText(value[1])
                    getattr(self.ui, f"dmg_{key}_line").setText(value2)
                    getattr(self.ui, f"dmg_{key}_label").setText(f'/{key}')

    def initial_skill_list(self): 
        self.selected_class = self.ui.class_combo.currentText()
        if 'stance' in skill_identity_data[self.selected_class]:
            skill_list = ['q','w','e','r','a','s','d','f','/q','/w','/e','/r','/a','/s','/d','/f','t','v']
            skill_setting = {'q' : None, 'w' : None, 'e' : None, 'r' : None, 'a' : None, 's' : None, 'd' : None, 'f' : None, 
                             '/q': None, '/w': None, '/e': None, '/r': None, '/a': None, '/s': None, '/d': None, '/f': None, 
                             't' : None, 'v' : None }
            skill_damge = {'q' : None, 'w' : None, 'e' : None, 'r' : None, 'a' : None, 's' : None, 'd' : None, 'f' : None, 
                             '/q': None, '/w': None, '/e': None, '/r': None, '/a': None, '/s': None, '/d': None, '/f': None, 
                             't' : None, 'v' : None , 'z': None, 'z1': None, 'z2': None, 'z3': None, 'x': None, 'x1': None, 'x2': None, 'x3': None }
        else:
            skill_list = ['q','w','e','r','a','s','d','f','t','v']
            skill_setting = {'q' : None, 'w' : None, 'e' : None, 'r' : None, 'a' : None, 's' : None, 'd' : None, 'f' : None,
                            't': None, 'v': None }
            skill_damge = {'q' : None, 'w' : None, 'e' : None, 'r' : None, 'a' : None, 's' : None, 'd' : None, 'f' : None,
                            't': None, 'v': None, 'z': None, 'z1': None, 'z2': None, 'z3': None, 'x': None, 'x1': None, 'x2': None, 'x3': None }

        return skill_list, skill_setting, skill_damge

    #공속 관련 아이텐티티 정보 추가
    def initial_skill_setting(self): 
        self.ui.v_combo.clear();self.ui.q_combo.clear();self.ui.w_combo.clear();self.ui.e_combo.clear();self.ui.r_combo.clear()
        self.ui.t_combo.clear();self.ui.a_combo.clear();self.ui.s_combo.clear();self.ui.d_combo.clear();self.ui.f_combo.clear()
        
        self.ui.stance1_check.setChecked(True)
        self.ui.stance2_check.setChecked(False)

        self.skill_list, self.skill_setting, self.skill_damge = self.initial_skill_list() # 초기 스킬 리스트 빈 행렬 정의

        keys = ['q','w','e','r','a','s','d','f']
        for k in keys: getattr(self.ui, f"{k}_combo").addItems(self.skill_speed[self.selected_class]['일반스킬'].keys()) # 초기 스킬 콤보 아이템 추가
        for k in ['t','v']: getattr(self.ui, f"{k}_combo").addItems(self.skill_speed[self.selected_class][k].keys())

        for k in keys + ['t','v', 'z', 'x']:  getattr(self.ui, f"dmg_{k}_line").setText(self.skill_damge[k]) # 초기 데미지 값 세팅

        for k in keys: # 초기 스킬 콤보 룬 콤보 세팅 저장
            self.skill_setting[k] = [getattr(self.ui, f"{k}_combo").currentText(), getattr(self.ui, f"{k}_rune_combo").currentText()]
        self.skill_setting['t'] = [self.ui.t_combo.currentText(), '-']
        self.skill_setting['v'] = [self.ui.v_combo.currentText(), '-']

        if 'stance' in skill_identity_data[self.selected_class]: # 초기 스탠스 변경 스킬 콤보 룬 콤보 세팅 저장
            for k in keys: self.skill_setting[f"/{k}"] = [getattr(self.ui, f"{k}_combo").currentText(), getattr(self.ui, f"{k}_rune_combo").currentText()]

        validator = QIntValidator(0, 9999, self)

        self.ui.identity1_check.setChecked(False) # 1 아이텐티 전부 비활성화
        self.ui.identity1_check.setDisabled(True)
        self.ui.identity1_line.setValidator(validator)
        self.ui.identity1_line.setDisabled(True)

        self.ui.identity2_check.setChecked(False) # 2 아이텐티 전부 비활성화
        self.ui.identity2_check.setDisabled(True)
        self.ui.identity2_line.setValidator(validator)
        self.ui.identity2_line.setDisabled(True)

        if 'stance' in skill_identity_data[self.selected_class]: # 스탠스 체크 활성화
            self.ui.stance1_check.setVisible(True) 
            self.ui.stance2_check.setVisible(True)
        else:
            self.ui.stance1_check.setVisible(False)
            self.ui.stance2_check.setVisible(False)



        ########################################################################################################################### 
        ########################################################################################################################### 
        ########################################################################################################################### 
        ########################################################################################################################### 



        if self.selected_class == '소서리스':
            self.ui.identity1_label.setText('점화 깨달음 마나순환 안찍으면 체크해제 (마나순환: 점화후 30초간 8% 공속증가)')
            self.ui.identity1_check.setDisabled(False) # 1 활성화
            self.ui.identity1_check.setChecked(True)  # 1 체크가 기본
            self.ui.identity2_label.setText('속전속결 캐스팅 추가 공속')
            self.ui.identity2_check.setDisabled(False) # 2 활성화
            self.ui.identity2_check.setChecked(False)  # 2 체크헤제가 기본
            self.ui.identity2_line.setDisabled(False)# 2 line 활성화
        elif self.selected_class == '창술사':
            self.ui.identity1_label.setText('z가 버블')
            self.ui.stance1_check.setText('절제') 
            self.ui.stance2_check.setText('절정')
        elif self.selected_class == '건슬링어':
            self.ui.identity1_label.setText('피메 평화 주의자 안찍으면 체크 해제, text에 공속 입력 (평화 주의자: 스탠스 변경시 9초 간 공속 10%, 13%, 16%)')
            self.ui.identity1_check.setDisabled(False) # 1 활성화
            self.ui.identity1_check.setChecked(True)  # 1 체크가 기본
            self.ui.identity1_line.setDisabled(False)# 1 line 활성화
            self.ui.identity1_line.setText('13')# 1 line 활성화
            self.ui.identity2_label.setText('아이텐티티2 설명')  

        else:
            self.ui.identity1_label.setText('아이텐티티1 설명')
            self.ui.identity2_label.setText('아이텐티티2 설명')



        ########################################################################################################################### 
        ########################################################################################################################### 
        ########################################################################################################################### 
        ########################################################################################################################### 


    def save_setting(self):
        data = {
            'Class' : self.ui.class_combo.currentText(),
            'Skill': self.skill_setting,
            'Speed': self.ui.speed_line.text(),
            'Nak' : [ self.ui.nak1_combo.currentText(), self.ui.nak1_line.text() ,self.ui.nak2_combo.currentText(), self.ui.nak2_line.text()],
            'Veff' : [ self.ui.veff1_combo.currentText(), self.ui.veff1_line.text() ,self.ui.veff2_combo.currentText(), self.ui.veff2_line.text()],
            'Identity' : [ self.ui.identity1_check.isChecked(), self.ui.identity1_line.text() ,self.ui.identity2_check.isChecked(), self.ui.identity2_line.text()],
            'Damage' : self.skill_damge,
        }
        options = QFileDialog.Options()
        #file_path, _ = QFileDialog.getSaveFileName(self, "Save JSON File", "", "JSON Files (*.json);;All Files (*)", options=options)
        file_path, _ = QFileDialog.getSaveFileName(self, "Save DAT File", "", "DAT Files (*.dat);;All Files (*)", options=options)

        if file_path:
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=4)

    def load_setting(self):
        options = QFileDialog.Options()
        #file_path, _ = QFileDialog.getOpenFileName(self, "Open JSON File", "", "JSON Files (*.json);;All Files (*)", options=options)
        file_path, _ = QFileDialog.getOpenFileName(self, "Open DAT File", "", "DAT Files (*.dat);;All Files (*)", options=options)
        #file_path = 'D:/VSC/Ark/lastest.json'
        if file_path:
            with open(file_path, 'r') as f:
                data = json.load(f)
                self.skill_setting = data['Skill']
                self.skill_damge = data['Damage']
                self.ui.class_combo.setCurrentText(data['Class'])
                self.ui.q_combo.setCurrentText(data['Skill']['q'][0])
                self.ui.w_combo.setCurrentText(data['Skill']['w'][0])
                self.ui.e_combo.setCurrentText(data['Skill']['e'][0])
                self.ui.r_combo.setCurrentText(data['Skill']['r'][0])
                self.ui.a_combo.setCurrentText(data['Skill']['a'][0])
                self.ui.s_combo.setCurrentText(data['Skill']['s'][0])
                self.ui.d_combo.setCurrentText(data['Skill']['d'][0])
                self.ui.f_combo.setCurrentText(data['Skill']['f'][0])
                self.ui.t_combo.setCurrentText(data['Skill']['t'][0])
                self.ui.v_combo.setCurrentText(data['Skill']['v'][0])
                self.ui.q_rune_combo.setCurrentText(data['Skill']['q'][1])
                self.ui.w_rune_combo.setCurrentText(data['Skill']['w'][1])
                self.ui.e_rune_combo.setCurrentText(data['Skill']['e'][1])
                self.ui.r_rune_combo.setCurrentText(data['Skill']['r'][1])
                self.ui.a_rune_combo.setCurrentText(data['Skill']['a'][1])
                self.ui.s_rune_combo.setCurrentText(data['Skill']['s'][1])
                self.ui.d_rune_combo.setCurrentText(data['Skill']['d'][1])
                self.ui.f_rune_combo.setCurrentText(data['Skill']['f'][1])

                self.ui.dmg_q_line.setText(self.skill_damge['q'])
                self.ui.dmg_w_line.setText(self.skill_damge['w'])
                self.ui.dmg_e_line.setText(self.skill_damge['e'])
                self.ui.dmg_r_line.setText(self.skill_damge['r'])
                self.ui.dmg_a_line.setText(self.skill_damge['a'])
                self.ui.dmg_s_line.setText(self.skill_damge['s'])
                self.ui.dmg_d_line.setText(self.skill_damge['d'])
                self.ui.dmg_f_line.setText(self.skill_damge['f'])
                self.ui.dmg_t_line.setText(self.skill_damge['t'])
                self.ui.dmg_v_line.setText(self.skill_damge['v'])
                self.ui.dmg_z_line.setText(self.skill_damge['z'])
                self.ui.dmg_z1_line.setText(self.skill_damge['z1'])
                self.ui.dmg_z2_line.setText(self.skill_damge['z2'])
                self.ui.dmg_z3_line.setText(self.skill_damge['z3'])
                self.ui.dmg_x_line.setText(self.skill_damge['x'])
                self.ui.dmg_x1_line.setText(self.skill_damge['x1'])
                self.ui.dmg_x2_line.setText(self.skill_damge['x2'])
                self.ui.dmg_x3_line.setText(self.skill_damge['x3'])

                self.ui.speed_line.setText(data['Speed'])
                self.ui.nak1_combo.setCurrentText(data['Nak'][0])
                self.ui.nak1_line.setText(data['Nak'][1])
                self.ui.nak2_combo.setCurrentText(data['Nak'][2])
                self.ui.nak2_line.setText(data['Nak'][3])

                self.ui.veff2_combo.setCurrentText(data['Veff'][0])
                self.ui.veff2_line.setText(data['Veff'][1])
                self.ui.veff2_combo.setCurrentText(data['Veff'][2])
                self.ui.veff2_line.setText(data['Veff'][3])

                self.ui.identity1_check.setChecked(data['Identity'][0])
                self.ui.identity1_line.setText(data['Identity'][1])
                self.ui.identity2_check.setChecked(data['Identity'][2])
                self.ui.identity2_line.setText(data['Identity'][3])
                  
    def analysis(self):  
        # time line 초기화
        if self.timeline_view is not None:
            self.ui.Result_Layout.removeWidget(self.timeline_view)
            self.timeline_view.deleteLater()
            self.timeline_view = None
    
        #필요 정보 셋팅
        selected_class=self.ui.class_combo.currentText()
        default_speed=float(self.ui.speed_line.text())

        speed_veff_data={}
        skill_speed_data={}
        rune_combo_table={}
        for key in self.skill_list:
            if key == 't':
                speed_veff_data[key] = self.skill_speed[selected_class]['t'][self.skill_setting[key][0]]['공속버프']
                skill_speed_data[key] = self.skill_speed[selected_class]['t'][self.skill_setting[key][0]]['시전시간']
                rune_combo_table[key] = self.skill_setting[key][1]
            elif key =='v':
                speed_veff_data[key] = self.skill_speed[selected_class]['v'][self.skill_setting[key][0]]['공속버프']
                skill_speed_data[key] = self.skill_speed[selected_class]['v'][self.skill_setting[key][0]]['시전시간']
                rune_combo_table[key] = self.skill_setting[key][1]
            else:
                speed_veff_data[key] = self.skill_speed[selected_class]['일반스킬'][self.skill_setting[key][0]]['공속버프']
                skill_speed_data[key] = self.skill_speed[selected_class]['일반스킬'][self.skill_setting[key][0]]['시전시간']
                rune_combo_table[key] = self.skill_setting[key][1]

        # 기믹 무력 컷신 제거 구간 설정 excluded_ranges 정의 [시작, 끝]
        excluded_ranges = []  # 제외할 구간을 모아둠
        start_frame = None   
        i = 0
        exclude_ranges = { '컷신시작': '컷신끝' }

        while i < len(self.Pattern_table_data):
            frame, label = self.Pattern_table_data[i]
            frame = int(frame)
            if label in exclude_ranges:
                end_label = exclude_ranges[label] 
                for j in range(i + 1, len(self.Pattern_table_data)):
                    end_time, end_label_found = self.Pattern_table_data[j]
                    end_time = int(end_time)
                    if end_label_found == end_label:
                        excluded_ranges.append([frame, end_time])
                        i = j  
                        break
            else:
                if start_frame is None:
                    start_frame = frame
                elif label == '끝':
                    end_frame = frame
                i += 1

        # 총 프레임에서 제거 구간 제거  => 총 딜구간 damage_table 계산 [시작, 끝]
        damage_table = []
        for exclude_start, exclude_end in excluded_ranges:
            damage_table.append([start_frame, exclude_start - 1])
            start_frame = exclude_end + 1
        if start_frame <= end_frame:
            damage_table.append([start_frame, end_frame])

        #컷신 관련 패턴만 찾기
        cutscene = []
        cutscene_table = []
        #컷신 프레임만 추출 [[프레임, 컷신시작],[프레임, 컷신끝]....]
        for pattern_table in self.Pattern_table_data:
            if pattern_table[1] == '컷신시작' or pattern_table[1] == '컷신끝':
                cutscene.append(pattern_table)
        #컷신 테이터 형식 변환 [시작,끝]
        for i in range(0, len(cutscene), 2):
            start = cutscene[i][0]
            end = cutscene[i + 1][0]
            cutscene_table.append([int(start), int(end)])
        
        #컷신 구간 스킬 제거 = filtered_skill_table[시작, 스킬명]
        if len(cutscene_table) > 0:
            filtered_skill_table = [ skill for skill in self.Skill_table_data
                if not any(int(cut_start) <= int(skill[0]) <= int(cut_end) for cut_start, cut_end in cutscene_table) ]
        else:
            filtered_skill_table = self.Skill_table_data

        filtered_skill_table = sorted(filtered_skill_table, key=lambda x: int(x[0])) 

        ########################################################################################################################### 
        ########################################################################################################################### 
        ########################################################################################################################### 
        ########################################################################################################################### 

        # input : filtered_skill_table identity default_speed rune_combo_table  speed_veff_data   import skill_speed_data rune_speed
        # output : skill_time_table

        # 아이텐티티시 구간 정의/ 시전시간 변경 및 공속 버프에서 활용
        # 시전시간이 변경되는 스킬은 시전시간이 [선딜, 후딜, 아이텐티티선딜, 아이텐티티후딜]로 정의됨
        # 아이텐티티 공속증가는 버프 타임라인에서 추가
        identity = [ self.ui.identity1_check.isChecked(), self.ui.identity1_line.text() ,self.ui.identity2_check.isChecked(), self.ui.identity2_line.text()]

        if selected_class =='소서리스':
            skill_time_table = Sorceress_analysis_function(filtered_skill_table, identity, default_speed, rune_combo_table, skill_speed_data, speed_veff_data, self.fps)
        #elif 타직업
        elif selected_class =='기상술사':
            skill_time_table = Aeromancer_analysis_function(filtered_skill_table, identity, default_speed, rune_combo_table, skill_speed_data, speed_veff_data, self.fps)
        elif selected_class =='창술사':
            skill_time_table = Glaivier_analysis_function(filtered_skill_table, identity, default_speed, rune_combo_table, skill_speed_data, speed_veff_data, self.fps)  
        elif selected_class =='블레이드':
            skill_time_table = Deathblade_analysis_function(filtered_skill_table, identity, default_speed, rune_combo_table, skill_speed_data, speed_veff_data, self.fps)
        elif selected_class =='건슬링어':
            skill_time_table = Gunslinger_analysis_function(filtered_skill_table, identity, default_speed, rune_combo_table, skill_speed_data, speed_veff_data, self.fps)
        elif selected_class =='공용직업':
            skill_time_table = General_analysis_function(filtered_skill_table, identity, default_speed, rune_combo_table, skill_speed_data, speed_veff_data, self.fps)


        ########################################################################################################################### 
        ########################################################################################################################### 
        ########################################################################################################################### 
        ########################################################################################################################### 


        ####  skill_time_table [시작, 끝, 스킬명]

        buff_duration = 360
        max_stack = 6

        veff_ad = []
        buff_stack = 0
        buff_expire = -1

        for i in range(len(skill_time_table)):
            start, end, skill = skill_time_table[i]
            next_start = skill_time_table[i + 1][0] if i + 1 < len(skill_time_table) else None
            # 중첩 갱신
            if start > buff_expire:
                buff_stack = 1
            else:
                buff_stack = min(buff_stack + 1, max_stack)
            # 버프 만료 시점
            buff_expire = start + buff_duration
            # 이번 구간의 종료는 다음 스킬 시작 전 or 버프 만료 중 빠른 것
            if next_start is None:
                interval_end = buff_expire
            else:
                interval_end = min(buff_expire, next_start)
            veff_ad.append([start, interval_end - 1, f'ad{buff_stack}'])

        veff_ad_merged = []
        for seg in veff_ad:
            if not veff_ad_merged:
                veff_ad_merged.append(seg)
            else:
                last = veff_ad_merged[-1]
                # 인접하고 중첩 같으면 병합
                if last[1] + 1 == seg[0] and last[2] == seg[2]:
                    last[1] = seg[1]  # 끝만 늘리기
                else:
                    veff_ad_merged.append(seg)

        ### 아드 시간 계산

        veff_ad_merged = sorted(veff_ad_merged, key=lambda x: int(x[0])) 
        merged = []
        for start, end, name in veff_ad_merged:
            if name == 'ad6':
                if not merged or merged[-1][1] < start - 1:
                    merged.append([start, end])
                else:
                    merged[-1][1] = max(merged[-1][1], end)
        ad_time = sum(end - start + 1 for start, end in merged)
        self.ui.ad_time_text.setText(f'아드유지 : {float(ad_time/self.fps):.1f} 초')

        for i in veff_ad_merged:
            skill_time_table.append(i)

        ###낙인1
        nak_skill=[]
        nak1_skill=[]
        if self.ui.nak1_combo.currentText() != '-':
            for skill_start, skill_end, skill_name in skill_time_table:
                name = re.sub(r'\d+$', '', skill_name  )  
                if name == self.ui.nak1_combo.currentText():
                    nak_skill.append([ int(skill_start) ,int(skill_start) + int(float(self.ui.nak1_line.text())*self.fps) - 1])
            for damage_start, damage_end in damage_table:
                for skill_start, skill_end in nak_skill:
                    overlap_start = max(damage_start, skill_start)
                    overlap_end = min(damage_end, skill_end)
                    if overlap_start <= overlap_end:
                        nak1_skill.append( [ overlap_start, overlap_end ] )
        ###낙인2
        nak_skill=[]
        nak2_skill=[]
        if self.ui.nak2_combo.currentText() != '-':
            for skill_start, skill_end, skill_name in skill_time_table:
                name = re.sub(r'\d+$', '', skill_name  )  
                if name == self.ui.nak2_combo.currentText():
                    nak_skill.append([ int(skill_start) ,int(skill_start) + int(float(self.ui.nak2_line.text())*self.fps) - 1])
            for damage_start, damage_end in damage_table:
                for skill_start, skill_end in nak_skill:
                    overlap_start = max(damage_start, skill_start)
                    overlap_end = min(damage_end, skill_end)
                    if overlap_start <= overlap_end:
                        nak2_skill.append( [ overlap_start, overlap_end ] )

        ### 낙인 시간 계산
        all_ranges = nak1_skill + nak2_skill
        all_ranges = sorted(all_ranges, key=lambda x: int(x[0])) 
        merged1 = []
        for start, end in all_ranges:
            if not merged1 or merged1[-1][1] < start - 1:
                merged1.append([start, end])
            else:
                merged1[-1][1] = max(merged1[-1][1], end)
        nak_time = sum(end - start + 1 for start, end in merged1)

        ###공증1
        veff_skill=[]
        veff1_skill=[]
        if self.ui.veff1_combo.currentText() != '-':
            for skill_start, skill_end, skill_name in skill_time_table:
                name = re.sub(r'\d+$', '', skill_name  )  
                if name == self.ui.veff1_combo.currentText():
                    veff_skill.append([int(skill_start),  int(skill_start) + int(float(self.ui.veff1_line.text())*self.fps) - 1])
            for damage_start, damage_end in damage_table:
                for skill_start, skill_end in veff_skill:
                    overlap_start = max(damage_start, skill_start)
                    overlap_end = min(damage_end, skill_end)
                    if overlap_start <= overlap_end:
                        veff1_skill.append( [ overlap_start, overlap_end ] )
        ###공증2
        veff_skill=[]
        veff2_skill=[]
        if self.ui.veff2_combo.currentText() != '-':
            for skill_start, skill_end, skill_name in skill_time_table:
                name = re.sub(r'\d+$', '', skill_name  )  
                if name == self.ui.veff2_combo.currentText():
                    veff_skill.append([int(skill_start),  int(skill_start) + int(float(self.ui.veff2_line.text())*self.fps) - 1])
            for damage_start, damage_end in damage_table:
                for skill_start, skill_end in veff_skill:
                    overlap_start = max(damage_start, skill_start)
                    overlap_end = min(damage_end, skill_end)
                    if overlap_start <= overlap_end:
                        veff2_skill.append( [ overlap_start, overlap_end ] )

        ### 공증 시간 계산
        all_ranges = veff1_skill + veff2_skill
        all_ranges = sorted(all_ranges, key=lambda x: int(x[0])) 
        merged2 = []
        for start, end in all_ranges:
            if not merged2 or merged2[-1][1] < start - 1:
                merged2.append([start, end])
            else:
                merged2[-1][1] = max(merged2[-1][1], end)
        veff_time = sum(end - start + 1 for start, end in merged2)

        for i in merged1:
            skill_time_table.append([i[0], i[1], 'nak'])
        for i in merged2:
            skill_time_table.append([i[0], i[1], 'veff'])

        ### time line 추가
        skill_time_table = sorted(skill_time_table, key=lambda x: int(x[0])) #오름차순 정리
        self.timeline_view = TimelineView(self.Pattern_table_data, skill_time_table)
        self.ui.Result_Layout.addWidget(self.timeline_view, alignment=Qt.AlignLeft)

        ### 결과 출력
        ini_frame=int(self.Pattern_table_data[0][0])
        last_farme=int(self.Pattern_table_data[-1][0])

        self.ui.total_time_text.setText(f'(총시간 : {float((last_farme-ini_frame)/self.fps):.1f} 초)')
        # 기본 키 목록
        base_keys = ['q', 'w', 'e', 'r', 'a', 's', 'd', 'f', 't', 'v', 'z', 'x']

        # stance가 있는 클래스인 경우
        if 'stance' in skill_identity_data[self.selected_class]:
            all_keys = base_keys[:8]  # 'q' ~ 'f' 까지
            self.number_skill = {}
            for key in all_keys:
                normal_count = sum(1 for item in skill_time_table if item[2] == key)
                stance_count = sum(1 for item in skill_time_table if item[2] == f'/{key}')
                self.number_skill[key] = normal_count
                self.number_skill[f'/{key}'] = stance_count
                getattr(self.ui, f'no_{key}_text').setText(f'{key} {normal_count} / {stance_count} 회')

            for key in base_keys[8:]:  # 't', 'v', 'z', 'x'
                count = sum(1 for item in skill_time_table if item[2] == key)
                self.number_skill[key] = count
                getattr(self.ui, f'no_{key}_text').setText(f'{key} {count} 회')
        else:
            self.number_skill = {}
            for key in base_keys:
                count = sum(1 for item in skill_time_table if item[2] == key)
                self.number_skill[key] = count
                getattr(self.ui, f'no_{key}_text').setText(f'{key} {count} 회')

        if self.ui.nak1_combo.currentText() != '-' or self.ui.nak2_combo.currentText() != '-' :
            self.ui.nak_time_text.setText(f'낙인유지 : {float(nak_time/self.fps):.1f} 초')
        if self.ui.veff1_combo.currentText() != '-' or self.ui.veff2_combo.currentText() != '-' :
            self.ui.veff_time_text.setText(f'공증유지 : {int(veff_time/self.fps):.1f} 초')

    def damage_analysis(self):
        total = 0
        dmage_table = []
        for key in self.number_skill:
            if key in self.skill_damge:
                try:
                    num1 = float(self.skill_damge[key])
                    num2 = float(self.number_skill[key])
                    
                    dmage_table.append( [key, num1 * num2 ])

                    total += num1 * num2
                except (TypeError, ValueError):
                    continue
        merged = {}

        for key, value in dmage_table:
            if key.startswith('/'):
                base_key = key[1:]
                if base_key in merged:
                    merged[base_key].append(value)
            else:
                merged[key] = [value]

        result = [[k] + v for k, v in merged.items()]
        for r in result:
            if len(r) == 2:
                getattr(self.ui, f"dmg_{r[0]}_text").setText(f'{r[0]} : {str(r[1])}') 
            elif len(r) ==3:
                getattr(self.ui, f"dmg_{r[0]}_text").setText(f'{r[0]} : {str(r[1])} / {str(r[2])}') 

        self.ui.dmg_total_text.setText(f'Total : {str(total)}')


