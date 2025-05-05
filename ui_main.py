# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainIOfxgE.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1260, 860)
        self.Main_widget = QWidget(MainWindow)
        self.Main_widget.setObjectName(u"Main_widget")
        self.horizontalLayout_12 = QHBoxLayout(self.Main_widget)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, 2, -1, 2)
        self.Movie_widget = QWidget(self.Main_widget)
        self.Movie_widget.setObjectName(u"Movie_widget")
        self.verticalLayout_5 = QVBoxLayout(self.Movie_widget)
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.Top_widget = QWidget(self.Movie_widget)
        self.Top_widget.setObjectName(u"Top_widget")
        self.horizontalLayout_2 = QHBoxLayout(self.Top_widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_New = QPushButton(self.Top_widget)
        self.btn_New.setObjectName(u"btn_New")

        self.horizontalLayout_2.addWidget(self.btn_New)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_Save = QPushButton(self.Top_widget)
        self.btn_Save.setObjectName(u"btn_Save")

        self.horizontalLayout_2.addWidget(self.btn_Save)

        self.btn_Load = QPushButton(self.Top_widget)
        self.btn_Load.setObjectName(u"btn_Load")

        self.horizontalLayout_2.addWidget(self.btn_Load)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 1)
        self.horizontalLayout_2.setStretch(3, 1)

        self.verticalLayout_5.addWidget(self.Top_widget)

        self.Time_widget = QWidget(self.Movie_widget)
        self.Time_widget.setObjectName(u"Time_widget")
        self.horizontalLayout_4 = QHBoxLayout(self.Time_widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.Running_label = QLabel(self.Time_widget)
        self.Running_label.setObjectName(u"Running_label")

        self.horizontalLayout_4.addWidget(self.Running_label)

        self.btn_start = QPushButton(self.Time_widget)
        self.btn_start.setObjectName(u"btn_start")

        self.horizontalLayout_4.addWidget(self.btn_start)

        self.Start_line = QLineEdit(self.Time_widget)
        self.Start_line.setObjectName(u"Start_line")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Start_line.sizePolicy().hasHeightForWidth())
        self.Start_line.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.Start_line)

        self.btn_end = QPushButton(self.Time_widget)
        self.btn_end.setObjectName(u"btn_end")

        self.horizontalLayout_4.addWidget(self.btn_end)

        self.End_line = QLineEdit(self.Time_widget)
        self.End_line.setObjectName(u"End_line")
        sizePolicy.setHeightForWidth(self.End_line.sizePolicy().hasHeightForWidth())
        self.End_line.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.End_line)

        self.line = QFrame(self.Time_widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line)

        self.time_Line = QLineEdit(self.Time_widget)
        self.time_Line.setObjectName(u"time_Line")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.time_Line.sizePolicy().hasHeightForWidth())
        self.time_Line.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.time_Line)

        self.btn_move = QPushButton(self.Time_widget)
        self.btn_move.setObjectName(u"btn_move")

        self.horizontalLayout_4.addWidget(self.btn_move)


        self.verticalLayout_5.addWidget(self.Time_widget)

        self.Video_widget = QVideoWidget(self.Movie_widget)
        self.Video_widget.setObjectName(u"Video_widget")
        self.Video_widget.setAutoFillBackground(True)

        self.verticalLayout_5.addWidget(self.Video_widget)

        self.Time_Slider = QSlider(self.Movie_widget)
        self.Time_Slider.setObjectName(u"Time_Slider")
        self.Time_Slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_5.addWidget(self.Time_Slider)

        self.btn_widget = QWidget(self.Movie_widget)
        self.btn_widget.setObjectName(u"btn_widget")
        self.horizontalLayout_9 = QHBoxLayout(self.btn_widget)
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.btn_pause = QPushButton(self.btn_widget)
        self.btn_pause.setObjectName(u"btn_pause")

        self.horizontalLayout_9.addWidget(self.btn_pause)

        self.btn_slow = QPushButton(self.btn_widget)
        self.btn_slow.setObjectName(u"btn_slow")

        self.horizontalLayout_9.addWidget(self.btn_slow)

        self.btn_play = QPushButton(self.btn_widget)
        self.btn_play.setObjectName(u"btn_play")

        self.horizontalLayout_9.addWidget(self.btn_play)

        self.btn_fast = QPushButton(self.btn_widget)
        self.btn_fast.setObjectName(u"btn_fast")

        self.horizontalLayout_9.addWidget(self.btn_fast)

        self.btn_m10 = QPushButton(self.btn_widget)
        self.btn_m10.setObjectName(u"btn_m10")

        self.horizontalLayout_9.addWidget(self.btn_m10)

        self.btn_m1 = QPushButton(self.btn_widget)
        self.btn_m1.setObjectName(u"btn_m1")

        self.horizontalLayout_9.addWidget(self.btn_m1)

        self.btn_p1 = QPushButton(self.btn_widget)
        self.btn_p1.setObjectName(u"btn_p1")

        self.horizontalLayout_9.addWidget(self.btn_p1)

        self.btn_p10 = QPushButton(self.btn_widget)
        self.btn_p10.setObjectName(u"btn_p10")

        self.horizontalLayout_9.addWidget(self.btn_p10)


        self.verticalLayout_5.addWidget(self.btn_widget)

        self.verticalLayout_5.setStretch(2, 90)
        self.verticalLayout_5.setStretch(3, 5)

        self.horizontalLayout_12.addWidget(self.Movie_widget)

        self.line_3 = QFrame(self.Main_widget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_12.addWidget(self.line_3)

        self.widget_5 = QWidget(self.Main_widget)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_4 = QVBoxLayout(self.widget_5)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.widget_7 = QWidget(self.widget_5)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 0, 0, 0)
        self.widget_11 = QWidget(self.widget_7)
        self.widget_11.setObjectName(u"widget_11")
        self.verticalLayout = QVBoxLayout(self.widget_11)
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_12 = QWidget(self.widget_11)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout = QHBoxLayout(self.widget_12)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget_12)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.Class_combo = QComboBox(self.widget_12)
        self.Class_combo.setObjectName(u"Class_combo")

        self.horizontalLayout.addWidget(self.Class_combo)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)

        self.verticalLayout.addWidget(self.widget_12)


        self.horizontalLayout_10.addWidget(self.widget_11)

        self.horizontalLayout_10.setStretch(0, 1)

        self.verticalLayout_4.addWidget(self.widget_7)

        self.btn_skill = QPushButton(self.widget_5)
        self.btn_skill.setObjectName(u"btn_skill")
        self.btn_skill.setMinimumSize(QSize(250, 46))

        self.verticalLayout_4.addWidget(self.btn_skill)

        self.Progress_label = QLabel(self.widget_5)
        self.Progress_label.setObjectName(u"Progress_label")
        self.Progress_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.Progress_label)

        self.line_2 = QFrame(self.widget_5)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_2)

        self.widget_6 = QWidget(self.widget_5)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_7 = QVBoxLayout(self.widget_6)
        self.verticalLayout_7.setSpacing(2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.Skill_widget = QWidget(self.widget_6)
        self.Skill_widget.setObjectName(u"Skill_widget")
        self.verticalLayout_3 = QVBoxLayout(self.Skill_widget)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 2, -1, 2)
        self.Skill_label = QLabel(self.Skill_widget)
        self.Skill_label.setObjectName(u"Skill_label")

        self.verticalLayout_3.addWidget(self.Skill_label)

        self.Skill_table = QTableWidget(self.Skill_widget)
        if (self.Skill_table.columnCount() < 2):
            self.Skill_table.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.Skill_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.Skill_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.Skill_table.setObjectName(u"Skill_table")

        self.verticalLayout_3.addWidget(self.Skill_table)

        self.widget_4 = QWidget(self.Skill_widget)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.btn_skill_up = QPushButton(self.widget_4)
        self.btn_skill_up.setObjectName(u"btn_skill_up")

        self.horizontalLayout_7.addWidget(self.btn_skill_up)

        self.btn_skill_down = QPushButton(self.widget_4)
        self.btn_skill_down.setObjectName(u"btn_skill_down")

        self.horizontalLayout_7.addWidget(self.btn_skill_down)


        self.verticalLayout_3.addWidget(self.widget_4)

        self.widget_3 = QWidget(self.Skill_widget)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.btn_skill_add = QPushButton(self.widget_3)
        self.btn_skill_add.setObjectName(u"btn_skill_add")

        self.horizontalLayout_6.addWidget(self.btn_skill_add)

        self.btn_skill_del = QPushButton(self.widget_3)
        self.btn_skill_del.setObjectName(u"btn_skill_del")

        self.horizontalLayout_6.addWidget(self.btn_skill_del)


        self.verticalLayout_3.addWidget(self.widget_3)

        self.btn_skill_arrange = QPushButton(self.Skill_widget)
        self.btn_skill_arrange.setObjectName(u"btn_skill_arrange")

        self.verticalLayout_3.addWidget(self.btn_skill_arrange)


        self.verticalLayout_7.addWidget(self.Skill_widget)

        self.Pattern_widget = QWidget(self.widget_6)
        self.Pattern_widget.setObjectName(u"Pattern_widget")
        self.verticalLayout_2 = QVBoxLayout(self.Pattern_widget)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 2, -1, 2)
        self.Pattern_label = QLabel(self.Pattern_widget)
        self.Pattern_label.setObjectName(u"Pattern_label")

        self.verticalLayout_2.addWidget(self.Pattern_label)

        self.Pattern_table = QTableWidget(self.Pattern_widget)
        if (self.Pattern_table.columnCount() < 2):
            self.Pattern_table.setColumnCount(2)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.Pattern_table.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.Pattern_table.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        self.Pattern_table.setObjectName(u"Pattern_table")

        self.verticalLayout_2.addWidget(self.Pattern_table)

        self.widget = QWidget(self.Pattern_widget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_pattern_up = QPushButton(self.widget)
        self.btn_pattern_up.setObjectName(u"btn_pattern_up")

        self.horizontalLayout_3.addWidget(self.btn_pattern_up)

        self.btn_pattern_down = QPushButton(self.widget)
        self.btn_pattern_down.setObjectName(u"btn_pattern_down")

        self.horizontalLayout_3.addWidget(self.btn_pattern_down)


        self.verticalLayout_2.addWidget(self.widget)

        self.widget_2 = QWidget(self.Pattern_widget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_pattern_add = QPushButton(self.widget_2)
        self.btn_pattern_add.setObjectName(u"btn_pattern_add")

        self.horizontalLayout_5.addWidget(self.btn_pattern_add)

        self.btn_pattern_del = QPushButton(self.widget_2)
        self.btn_pattern_del.setObjectName(u"btn_pattern_del")

        self.horizontalLayout_5.addWidget(self.btn_pattern_del)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.btn_pattern_arrange = QPushButton(self.Pattern_widget)
        self.btn_pattern_arrange.setObjectName(u"btn_pattern_arrange")

        self.verticalLayout_2.addWidget(self.btn_pattern_arrange)


        self.verticalLayout_7.addWidget(self.Pattern_widget)

        self.verticalLayout_7.setStretch(0, 2)
        self.verticalLayout_7.setStretch(1, 1)

        self.verticalLayout_4.addWidget(self.widget_6)

        self.btn_analysis = QPushButton(self.widget_5)
        self.btn_analysis.setObjectName(u"btn_analysis")
        self.btn_analysis.setMinimumSize(QSize(0, 46))

        self.verticalLayout_4.addWidget(self.btn_analysis)


        self.horizontalLayout_12.addWidget(self.widget_5)

        self.horizontalLayout_12.setStretch(0, 10)
        self.horizontalLayout_12.setStretch(2, 1)
        MainWindow.setCentralWidget(self.Main_widget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\uc804\ud22c \ubd84\uc11d\uae30", None))
        self.btn_New.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.btn_Save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.btn_Load.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.Running_label.setText(QCoreApplication.translate("MainWindow", u"Running time", None))
        self.btn_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.btn_end.setText(QCoreApplication.translate("MainWindow", u"end", None))
        self.btn_move.setText(QCoreApplication.translate("MainWindow", u"Move", None))
        self.btn_pause.setText(QCoreApplication.translate("MainWindow", u"\u275a\u275a", None))
        self.btn_slow.setText(QCoreApplication.translate("MainWindow", u"\u25b6 x 0.5", None))
        self.btn_play.setText(QCoreApplication.translate("MainWindow", u"\u25b6", None))
        self.btn_fast.setText(QCoreApplication.translate("MainWindow", u"\u25b6 x 2", None))
        self.btn_m10.setText(QCoreApplication.translate("MainWindow", u"-10 frame", None))
        self.btn_m1.setText(QCoreApplication.translate("MainWindow", u"-1 frame", None))
        self.btn_p1.setText(QCoreApplication.translate("MainWindow", u"1 frame", None))
        self.btn_p10.setText(QCoreApplication.translate("MainWindow", u"10 frame", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\uc9c1\uc5c5", None))
        self.btn_skill.setText(QCoreApplication.translate("MainWindow", u"\uc2a4\ud0ac \ucd94\ucd9c", None))
        self.Progress_label.setText(QCoreApplication.translate("MainWindow", u"\uc9c4\ud589\ub960", None))
        self.Skill_label.setText(QCoreApplication.translate("MainWindow", u"\uc2a4\ud0ac", None))
        ___qtablewidgetitem = self.Skill_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uac04", None));
        ___qtablewidgetitem1 = self.Skill_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\uc2a4\ud0ac", None));
        self.btn_skill_up.setText(QCoreApplication.translate("MainWindow", u"Up", None))
        self.btn_skill_down.setText(QCoreApplication.translate("MainWindow", u"Down", None))
        self.btn_skill_add.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.btn_skill_del.setText(QCoreApplication.translate("MainWindow", u"Del", None))
        self.btn_skill_arrange.setText(QCoreApplication.translate("MainWindow", u"\uc624\ub984\ucc28\uc21c", None))
        self.Pattern_label.setText(QCoreApplication.translate("MainWindow", u"\ucef7\uc2e0", None))
        ___qtablewidgetitem2 = self.Pattern_table.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uac04", None));
        ___qtablewidgetitem3 = self.Pattern_table.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\ud328\ud134", None));
        self.btn_pattern_up.setText(QCoreApplication.translate("MainWindow", u"Up", None))
        self.btn_pattern_down.setText(QCoreApplication.translate("MainWindow", u"Down", None))
        self.btn_pattern_add.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.btn_pattern_del.setText(QCoreApplication.translate("MainWindow", u"Del", None))
        self.btn_pattern_arrange.setText(QCoreApplication.translate("MainWindow", u"\uc624\ub984\ucc28\uc21c", None))
        self.btn_analysis.setText(QCoreApplication.translate("MainWindow", u"\ubd84\uc11d", None))
    # retranslateUi

