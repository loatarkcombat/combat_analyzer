from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow, QHeaderView, QTableWidgetItem, QComboBox#, QProgressBar, QTableWidget, QWidget
#from PySide6.QtCore import Qt, QUrl, QThread, Signal, QTimer
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtGui import QIntValidator
from ui_main import Ui_MainWindow
#import sys
#import os
#import datetime
import cv2
#import numpy as np
#import matplotlib.pyplot as plt # pip install matplotlib
import json
from analysis import Ui_Analysis
#import time
from skill_check import skill_analysis_function
from data import skill_identity_data

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("전투 분석기 ver 0.3")

        self.fps = 0
        self.duration = ''
        self.manual_change = False
        #self.ui.Skill_table.setEditTriggers(QTableWidget.NoEditTriggers)

        #self.ui.Pattern_table.resizeColumnsToContents()
        self.ui.Pattern_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        #self.ui.Skill_table.resizeColumnsToContents()
        self.ui.Skill_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.ui.Class_combo.addItems(skill_identity_data.keys())

        self.player = QMediaPlayer(self)
        self.player.setVideoOutput(self.ui.Video_widget)

        int_validator = QIntValidator(self)
        self.ui.time_Line.setValidator(int_validator)

        self.ui.btn_New.clicked.connect(self.btn_New_clicked)
        self.ui.btn_start.clicked.connect(self.btn_start_clicked)
        self.ui.btn_end.clicked.connect(self.btn_end_clicked)
        self.ui.btn_move.clicked.connect(self.btn_move_clicked)

        self.ui.btn_play.clicked.connect(self.btn_play_clicked)
        self.ui.btn_pause.clicked.connect(self.btn_pause_clicked)
        self.ui.btn_fast.clicked.connect(self.btn_fast_clicked)
        self.ui.btn_slow.clicked.connect(self.btn_slow_clicked)

        self.ui.btn_m10.clicked.connect(self.btn_m10_clicked)
        self.ui.btn_m1.clicked.connect(self.btn_m1_clicked)
        self.ui.btn_p1.clicked.connect(self.btn_p1_clicked)
        self.ui.btn_p10.clicked.connect(self.btn_p10_clicked)
        
        self.ui.Time_Slider.sliderMoved.connect(self.Time_Slider_changed)       
        self.player.positionChanged.connect(self.position_changed)
 
        self.ui.btn_pattern_add.clicked.connect(self.btn_pattern_add_clicked)
        self.ui.btn_pattern_del.clicked.connect(self.btn_pattern_del_clicked)
        self.ui.btn_pattern_up.clicked.connect(self.btn_pattern_up_clicked)
        self.ui.btn_pattern_down.clicked.connect(self.btn_pattern_down_clicked)
        self.ui.btn_pattern_arrange.clicked.connect(self.btn_pattern_arrange_clicked)

        self.ui.btn_skill_add.clicked.connect(self.btn_skill_add_clicked)
        self.ui.btn_skill_del.clicked.connect(self.btn_skill_del_clicked)
        self.ui.btn_skill_up.clicked.connect(self.btn_skill_up_clicked)
        self.ui.btn_skill_down.clicked.connect(self.btn_skill_down_clicked)
        self.ui.btn_skill_arrange.clicked.connect(self.btn_skill_arrange_clicked)

        self.ui.btn_Load.clicked.connect(self.load_from_json)
        self.ui.btn_Save.clicked.connect(self.save_to_json)

        self.ui.btn_skill.clicked.connect(self.btn_skill_clicked)
        self.ui.btn_analysis.clicked.connect(self.analysis)

##### skill 추출
    def btn_skill_clicked(self):
        #스킬데이블 초기화  
        self.ui.Skill_table.clearContents() 
        self.ui.Skill_table.setRowCount(0) 
        self.ui.Pattern_table.clearContents() 
        self.ui.Pattern_table.setRowCount(0) 

        selected_class=self.ui.Class_combo.currentText() #직업 불러오기 아이덴티티 때문에 필요
        #시작 및 끝 프레임
        start_frame = int(self.ui.Start_line.text())
        end_frame = int(self.ui.End_line.text())

        #스킬 체크 함수
        skill_table, cutscene_table, self.fps = skill_analysis_function(self.file,selected_class,start_frame,end_frame,self.ui.Progress_label)

        #스킬 결과 데이블 표시
        for line, skill in enumerate(skill_table):
            self.ui.Skill_table.insertRow(line)
            item0 = QTableWidgetItem(f"{skill[0]}")
            self.ui.Skill_table.setItem(line, 0, item0)
            item1 = QTableWidgetItem(f"{skill[1]}")
            self.ui.Skill_table.setItem(line, 1, item1)
        for line, cutscene in enumerate(cutscene_table):
            self.ui.Pattern_table.insertRow(line)
            item0 = QTableWidgetItem(f"{cutscene[0]}")
            self.ui.Pattern_table.setItem(line, 0, item0)
            item1 = QTableWidgetItem(f"{cutscene[1]}")
            self.ui.Pattern_table.setItem(line, 1, item1)

    def analysis(self):   
        selected_class=self.ui.Class_combo.currentText()
        Pattern_table_data = []
        Pattern_table_data.append([ self.ui.Start_line.text()  , '시작'])

        for row in range(self.ui.Pattern_table.rowCount()):
            row_data = []
            for column in range(self.ui.Pattern_table.columnCount()):
                if column == 1:  # 두 번째 열
                    widget = self.ui.Pattern_table.cellWidget(row, column)
                    if isinstance(widget, QComboBox):  # 콤보 박스인 경우
                        row_data.append(widget.currentText())  # 선택된 텍스트 가져오기
                    else:
                        row_data.append("")  # 콤보 박스가 아닌 경우 빈 문자열 추가
                else:
                    item = self.ui.Pattern_table.item(row, column)
                    row_data.append(item.text() if item else "")  # 셀에 데이터가 있으면 추가
            Pattern_table_data.append(row_data)

        Pattern_table_data.append([ self.ui.End_line.text()  , '끝'])

        Pattern_table_data = sorted(Pattern_table_data, key=lambda x: int(x[0])) #오름차순 정리

        Skill_table_data = []
        for row in range(self.ui.Skill_table.rowCount()):
            row_data = []
            for column in range(self.ui.Skill_table.columnCount()):
                item = self.ui.Skill_table.item(row, column)
                row_data.append(item.text() if item else "")  # 셀에 데이터가 있으면 추가
            Skill_table_data.append(row_data)

        Skill_table_data = sorted(Skill_table_data, key=lambda x: int(x[0])) #오름차순 정리
        self.new_window = Ui_Analysis(selected_class, Pattern_table_data, Skill_table_data, self.fps)
        self.new_window.show()

#### Pattern Function #####
    def update_combobox_items(self, combo):
        # 테이블의 콤보박스 항목을 외부 콤보박스 값에 따라 변경
        combo.clear()
        pattern_data = ["컷신시작", "컷신끝"]
        combo.addItems(pattern_data)

    def btn_pattern_add_clicked(self):   
        current_row_count = self.ui.Pattern_table.rowCount()
        self.ui.Pattern_table.insertRow(current_row_count)

        time = self.ui.Running_label.text()

        item0 = QTableWidgetItem(f"{time}")
        self.ui.Pattern_table.setItem(current_row_count, 0, item0)

        combo = QComboBox(self)
        combo.wheelEvent = lambda event: event.ignore()
        self.update_combobox_items(combo)
        self.ui.Pattern_table.setCellWidget(current_row_count, 1, combo)

    def btn_pattern_del_clicked(self):   
        current_row_count  = self.ui.Pattern_table.currentRow()
        if current_row_count  >= 0:
            self.ui.Pattern_table.removeRow(current_row_count)
            self.ui.Pattern_table.setCurrentCell(-1, -1)

    def btn_pattern_up_clicked(self):
        current_row = self.ui.Pattern_table.currentRow()
        
        if current_row > 0:  # 첫 번째 행이 아니면 위로 이동 가능
            # 첫 번째 열의 데이터를 교환
            current_item_0 = self.ui.Pattern_table.takeItem(current_row, 0)
            above_item_0 = self.ui.Pattern_table.takeItem(current_row - 1, 0)
            self.ui.Pattern_table.setItem(current_row, 0, above_item_0)
            self.ui.Pattern_table.setItem(current_row - 1, 0, current_item_0)
            
            # 두 번째 열의 위젯 및 아이템을 가져옴
            current_widget = self.ui.Pattern_table.cellWidget(current_row, 1)
            above_widget = self.ui.Pattern_table.cellWidget(current_row-1, 1)
            current_item = self.ui.Pattern_table.item(current_row, 1)
            above_item = self.ui.Pattern_table.item(current_row - 1, 1)
            # 현재 행의 텍스트 또는 콤보 박스의 텍스트 읽기
            if current_item is not None:  # 현재 행이 텍스트인 경우
                current_text = current_item.text()
            elif isinstance(current_widget, QComboBox):  # 현재 행이 콤보 박스인 경우
                current_text = current_widget.currentText()
            else:
                current_text = None

            # 위 행의 텍스트 또는 콤보 박스의 텍스트 읽기
            if above_item is not None:  # 위 행이 텍스트인 경우
                above_text = above_item.text()
            elif isinstance(above_widget, QComboBox):  # 위 행이 콤보 박스인 경우
                above_text = above_widget.currentText()
            else:
                above_text = None

            # 새로 교환할 콤보 박스 생성 및 추가
            new_combo_current = QComboBox(self)
            new_combo_current.wheelEvent = lambda event: event.ignore()
            self.update_combobox_items(new_combo_current)
            new_combo_current.setCurrentText(above_text)  # 위 텍스트 선택

            new_combo_above = QComboBox(self)
            new_combo_above.wheelEvent = lambda event: event.ignore()
            self.update_combobox_items(new_combo_above)  # 현재 행의 텍스트를 콤보 박스에 추가
            new_combo_above.setCurrentText(current_text)  # 현재 텍스트 선택

            # 콤보 박스를 테이블에 설정
            self.ui.Pattern_table.removeCellWidget(current_row, 1)  # 현재 행의 위젯 제거
            self.ui.Pattern_table.takeItem(current_row, 1)
            self.ui.Pattern_table.setCellWidget(current_row, 1, new_combo_current)  # 현재 행에 새 콤보 박스 추가

            self.ui.Pattern_table.removeCellWidget(current_row - 1, 1)  # 위 행의 위젯 제거
            self.ui.Pattern_table.takeItem(current_row - 1, 1) 
            self.ui.Pattern_table.setCellWidget(current_row - 1, 1, new_combo_above)  # 위 행에 새 콤보 박스 추가

            # 새로 이동한 행을 선택
            self.ui.Pattern_table.setCurrentCell(current_row - 1, 0)
    
    def btn_pattern_down_clicked(self):
        current_row = self.ui.Pattern_table.currentRow()
        
        if current_row < self.ui.Pattern_table.rowCount() - 1:  # 마지막 행이 아니면 아래로 이동 가능
            # 첫 번째 열의 데이터를 교환
            current_item_0 = self.ui.Pattern_table.takeItem(current_row, 0)
            below_item_0 = self.ui.Pattern_table.takeItem(current_row + 1, 0)
            self.ui.Pattern_table.setItem(current_row, 0, below_item_0)
            self.ui.Pattern_table.setItem(current_row + 1, 0, current_item_0)
            
            # 두 번째 열의 위젯 및 아이템을 가져옴
            current_widget = self.ui.Pattern_table.cellWidget(current_row, 1)
            below_widget = self.ui.Pattern_table.cellWidget(current_row + 1, 1)
            current_item = self.ui.Pattern_table.item(current_row, 1)
            below_item = self.ui.Pattern_table.item(current_row + 1, 1)
            # 현재 행의 텍스트 또는 콤보 박스의 텍스트 읽기
            if current_item is not None:  # 현재 행이 텍스트인 경우
                current_text = current_item.text()
            elif isinstance(current_widget, QComboBox):  # 현재 행이 콤보 박스인 경우
                current_text = current_widget.currentText()
            else:
                current_text = None

            # 아래 행의 텍스트 또는 콤보 박스의 텍스트 읽기
            if below_item is not None:  # 아래 행이 텍스트인 경우
                below_text = below_item.text()
            elif isinstance(below_widget, QComboBox):  # 아래 행이 콤보 박스인 경우
                below_text = below_widget.currentText()
            else:
                below_text = None

            # 새로 교환할 콤보 박스 생성 및 추가
            new_combo_current = QComboBox(self)
            new_combo_current.wheelEvent = lambda event: event.ignore()
            self.update_combobox_items(new_combo_current)
            new_combo_current.setCurrentText(below_text)  # 아래 텍스트 선택

            new_combo_below = QComboBox(self)
            new_combo_below.wheelEvent = lambda event: event.ignore()
            self.update_combobox_items(new_combo_below)  # 현재 행의 텍스트를 콤보 박스에 추가
            new_combo_below.setCurrentText(current_text)  # 현재 텍스트 선택

            # 콤보 박스를 테이블에 설정
            self.ui.Pattern_table.removeCellWidget(current_row, 1)  # 현재 행의 위젯 제거
            self.ui.Pattern_table.takeItem(current_row, 1)
            self.ui.Pattern_table.setCellWidget(current_row, 1, new_combo_current)  # 현재 행에 새 콤보 박스 추가

            self.ui.Pattern_table.removeCellWidget(current_row + 1, 1)  # 아래 행의 위젯 제거
            self.ui.Pattern_table.takeItem(current_row + 1, 1) 
            self.ui.Pattern_table.setCellWidget(current_row + 1, 1, new_combo_below)  # 아래 행에 새 콤보 박스 추가

            # 새로 이동한 행을 선택
            self.ui.Pattern_table.setCurrentCell(current_row + 1, 0)

    def btn_pattern_arrange_clicked(self):
        data = self.get_table_data(self.ui.Pattern_table)
        data = sorted(data, key=lambda x: int(x[0])) #오름차순 정리
        self.set_pattern_table_data(self.ui.Pattern_table, data)

    def btn_skill_add_clicked(self):   
        current_row_count = self.ui.Skill_table.rowCount()
        self.ui.Skill_table.insertRow(current_row_count)

        time = self.ui.Running_label.text()

        item0 = QTableWidgetItem(f"{time}")
        self.ui.Skill_table.setItem(current_row_count, 0, item0)

        item1 = QTableWidgetItem('q')
        self.ui.Skill_table.setItem(current_row_count, 1, item1)

    def btn_skill_del_clicked(self):   
        current_row_count  = self.ui.Skill_table.currentRow()
        if current_row_count  >= 0:
            self.ui.Skill_table.removeRow(current_row_count)
            self.ui.Skill_table.setCurrentCell(-1, -1)

    def btn_skill_up_clicked(self):
        current_row = self.ui.Skill_table.currentRow()
        
        if current_row > 0:  # 첫 번째 행이 아니면 위로 이동 가능
            current_item_0 = self.ui.Skill_table.takeItem(current_row, 0)
            above_item_0 = self.ui.Skill_table.takeItem(current_row - 1, 0)
            self.ui.Skill_table.setItem(current_row, 0, above_item_0)
            self.ui.Skill_table.setItem(current_row - 1, 0, current_item_0)

            current_item_1 = self.ui.Skill_table.takeItem(current_row, 1)
            above_item_1 = self.ui.Skill_table.takeItem(current_row - 1, 1)
            self.ui.Skill_table.setItem(current_row, 1, above_item_1)
            self.ui.Skill_table.setItem(current_row - 1, 1, current_item_1)
            # 새로 이동한 행을 선택
            self.ui.Skill_table.setCurrentCell(current_row-1, 0)

    def btn_skill_down_clicked(self):
        current_row = self.ui.Skill_table.currentRow()
        
        if current_row < self.ui.Skill_table.rowCount() - 1:  # 마지막 행이 아니면 아래로 이동 가능
            current_item_0 = self.ui.Skill_table.takeItem(current_row, 0)
            below_item_0 = self.ui.Skill_table.takeItem(current_row + 1, 0)
            self.ui.Skill_table.setItem(current_row, 0, below_item_0)
            self.ui.Skill_table.setItem(current_row + 1, 0, current_item_0)

            current_item_0 = self.ui.Skill_table.takeItem(current_row, 1)
            below_item_0 = self.ui.Skill_table.takeItem(current_row + 1, 1)
            self.ui.Skill_table.setItem(current_row, 1, below_item_0)
            self.ui.Skill_table.setItem(current_row + 1, 1, current_item_0)
            # 새로 이동한 행을 선택
            self.ui.Skill_table.setCurrentCell(current_row + 1, 0)

    def btn_skill_arrange_clicked(self):
        data = self.get_table_data(self.ui.Skill_table)
        data = sorted(data, key=lambda x: int(x[0])) #오름차순 정리
        self.set_skill_table_data(self.ui.Skill_table, data)

    def save_to_json(self):
        data = {
            'Class': self.ui.Class_combo.currentText(),
            'Start': self.ui.Start_line.text(),
            'End': self.ui.End_line.text(),
            'fps': str(self.fps),
            'Pattern': self.get_table_data(self.ui.Pattern_table),
            'Skill': self.get_table_data(self.ui.Skill_table),
        }
        
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(self, "Save DAT File", "", "DAT Files (*.dat);;All Files (*)", options=options)
    
        if file_path:
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=4)

    def load_from_json(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Open DAT File", "", "DAT Files (*.dat);;All Files (*)", options=options)
    
        if file_path:
            with open(file_path, 'r') as f:
                data = json.load(f)
                self.fps = float(data['fps'])
                self.ui.Pattern_table.clearContents()  # 테이블의 내용을 지우고
                self.ui.Pattern_table.setRowCount(0)  # 행 수를 0으로 설정하여 초기화
                self.ui.Skill_table.clearContents()  # 테이블의 내용을 지우고
                self.ui.Skill_table.setRowCount(0)  # 행 수를 0으로 설정하여 초기화
                self.set_pattern_table_data(self.ui.Pattern_table, data.get('Pattern', []))
                self.set_skill_table_data(self.ui.Skill_table, data.get('Skill', []))
                self.ui.Start_line.setText(data.get('Start'))
                self.ui.End_line.setText(data.get('End'))
                self.ui.Class_combo.setCurrentText(data.get('Class'))

    def get_table_data(self, table):
        rows = table.rowCount()
        cols = table.columnCount()
        data = []
        for row in range(rows):
            row_data = []
            for col in range(cols):
                if table.cellWidget(row, col):  # 콤보박스가 있는 경우
                    item = table.cellWidget(row, col)
                    row_data.append(item.currentText())  # 콤보박스의 현재 선택된 텍스트 추가
                else:  # 일반 텍스트 아이템인 경우
                    item = table.item(row, col)
                    row_data.append(item.text() if item else "")
            data.append(row_data)
        return data

    def set_pattern_table_data(self, table, data):
        table.setColumnCount(2)
        table.setRowCount(len(data)) 
        for row_index, row_data in enumerate(data):
            for col_index, value in enumerate(row_data):
                if col_index == 1:  # 두 번째 열
                    item = QComboBox(self)
                    item.wheelEvent = lambda event: event.ignore()
                    self.update_combobox_items(item)
                    item.setCurrentText(value)  # 위 텍스트 선택
                    table.setCellWidget(row_index, col_index, item)
                elif col_index == 0:  # 두 번째 열
                    item = QTableWidgetItem(value)
                    table.setItem(row_index, col_index, item)

    def set_skill_table_data(self, table, data):
        table.setColumnCount(2)
        table.setRowCount(len(data)) 
        table.setColumnCount(len(data[0]) if data else 0)
        for row_index, row_data in enumerate(data):
            for col_index, value in enumerate(row_data):
                table.setItem(row_index, col_index, QTableWidgetItem(value))

 ### Video def ###
    def btn_New_clicked(self):
        self.file, ext = QFileDialog.getOpenFileName(self, 'Select one file to open', ''
                                             , 'Video (*.mp4 *.mpg *.mpeg *.avi *.wma)') 
        if self.file:
            self.player.setSource(self.file)
            self.player.play()
            self.player.pause()
            self.player.durationChanged.connect(self.set_duration)
            self.cap = cv2.VideoCapture(self.file)
            self.fps = self.cap.get(cv2.CAP_PROP_FPS) # 60
            self.current_frame = 0
            self.ui.Running_label.setText(str(self.current_frame))

    def set_duration(self):
        self.duration = self.player.duration()
        self.ui.Time_Slider.setRange(0, self.duration)
        self.ui.Time_Slider.setEnabled(True)
        self.player.durationChanged.disconnect(self.set_duration)
        
    def Time_Slider_changed(self, pos):   
        self.manual_change = True
        self.player.setPosition(pos)
        self.current_frame = int(pos / (1000 / self.fps))
        self.ui.Running_label.setText(str(self.current_frame))
        self.manual_change = False
        
    def position_changed(self, pos):   
        if not self.manual_change: 
            self.ui.Time_Slider.setSliderPosition(pos)
            self.current_frame = int(pos / (1000 / self.fps))
            self.ui.Running_label.setText(str(self.current_frame))

    def btn_start_clicked(self):
        time=self.ui.Running_label.text()
        self.ui.Start_line.setText(time)

    def btn_end_clicked(self):
        time=self.ui.Running_label.text()
        self.ui.End_line.setText(time)

    def btn_move_clicked(self):
        self.manual_change = True
        time=self.ui.time_Line.text()
        self.current_frame = int(time)
        self.ui.Running_label.setText(time)
        self.player.setPosition(int(int(time) * (1000 / self.fps)))
        self.ui.Time_Slider.setSliderPosition(int(int(time) * (1000 / self.fps)))
        self.manual_change = False

    def btn_play_clicked(self):    
        self.player.setPlaybackRate(1.0)
        self.player.play()
 
    def btn_fast_clicked(self):    
        self.player.setPlaybackRate(2.0)
        self.player.play()

    def btn_slow_clicked(self):    
        self.player.setPlaybackRate(0.5)
        self.player.play()

    def btn_pause_clicked(self):
        self.player.pause()

    def btn_m10_clicked(self):
        if self.current_frame > 10:
            self.manual_change = True
            self.current_frame = self.current_frame - 10
            ms_position = int(self.current_frame * (1000 / self.fps))
            self.player.setPosition(ms_position)
            self.ui.Running_label.setText(str(self.current_frame))
            self.manual_change = False
 
    def btn_m1_clicked(self):
        if self.current_frame > 0:
            self.manual_change = True
            self.current_frame = self.current_frame - 1 
            ms_position = int(self.current_frame * (1000 / self.fps))
            self.player.setPosition(ms_position)
            self.ui.Running_label.setText(str(self.current_frame))
            self.manual_change = False

    def btn_p1_clicked(self):
        self.manual_change = True
        self.current_frame = self.current_frame + 1 
        ms_position = int(self.current_frame * (1000 / self.fps))
        self.player.setPosition(ms_position)
        self.ui.Running_label.setText(str(self.current_frame))
        self.manual_change = False

    def btn_p10_clicked(self):
        self.manual_change = True
        self.current_frame = self.current_frame + 10
        ms_position = int(self.current_frame * (1000 / self.fps))
        self.player.setPosition(ms_position)
        self.ui.Running_label.setText(str(self.current_frame))
        self.manual_change = False

if __name__ == "__main__":
    app = QApplication([])
    window = MyMainWindow()
    window.show()
    app.exec()