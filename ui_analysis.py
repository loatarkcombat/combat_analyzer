# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_analysisPALctm.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_analysis(object):
    def setupUi(self, analysis):
        if not analysis.objectName():
            analysis.setObjectName(u"analysis")
        analysis.resize(1260, 860)
        self.verticalLayout_21 = QVBoxLayout(analysis)
        self.verticalLayout_21.setSpacing(2)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(-1, 2, -1, 2)
        self.widget_33 = QWidget(analysis)
        self.widget_33.setObjectName(u"widget_33")
        self.horizontalLayout_24 = QHBoxLayout(self.widget_33)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(-1, 0, -1, 0)
        self.widget_5 = QWidget(self.widget_33)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_7 = QVBoxLayout(self.widget_5)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(2, 2, 2, 2)
        self.widget_30 = QWidget(self.widget_5)
        self.widget_30.setObjectName(u"widget_30")
        self.horizontalLayout_29 = QHBoxLayout(self.widget_30)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(-1, 2, -1, 2)
        self.label_27 = QLabel(self.widget_30)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_29.addWidget(self.label_27)

        self.class_combo = QComboBox(self.widget_30)
        self.class_combo.setObjectName(u"class_combo")

        self.horizontalLayout_29.addWidget(self.class_combo)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_2)

        self.btn_save = QPushButton(self.widget_30)
        self.btn_save.setObjectName(u"btn_save")

        self.horizontalLayout_29.addWidget(self.btn_save)

        self.btn_load = QPushButton(self.widget_30)
        self.btn_load.setObjectName(u"btn_load")

        self.horizontalLayout_29.addWidget(self.btn_load)

        self.horizontalLayout_29.setStretch(0, 1)
        self.horizontalLayout_29.setStretch(1, 1)
        self.horizontalLayout_29.setStretch(2, 2)
        self.horizontalLayout_29.setStretch(3, 1)
        self.horizontalLayout_29.setStretch(4, 1)

        self.verticalLayout_7.addWidget(self.widget_30)

        self.line_7 = QFrame(self.widget_5)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_7.addWidget(self.line_7)

        self.widget_48 = QWidget(self.widget_5)
        self.widget_48.setObjectName(u"widget_48")
        self.verticalLayout_11 = QVBoxLayout(self.widget_48)
        self.verticalLayout_11.setSpacing(2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 2, -1, 2)
        self.widget_49 = QWidget(self.widget_48)
        self.widget_49.setObjectName(u"widget_49")
        self.horizontalLayout_40 = QHBoxLayout(self.widget_49)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(-1, 0, -1, 0)
        self.widget_50 = QWidget(self.widget_49)
        self.widget_50.setObjectName(u"widget_50")
        self.horizontalLayout_43 = QHBoxLayout(self.widget_50)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(-1, 0, -1, 0)
        self.label_48 = QLabel(self.widget_50)
        self.label_48.setObjectName(u"label_48")

        self.horizontalLayout_43.addWidget(self.label_48)

        self.v_combo = QComboBox(self.widget_50)
        self.v_combo.setObjectName(u"v_combo")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.v_combo.sizePolicy().hasHeightForWidth())
        self.v_combo.setSizePolicy(sizePolicy)
        self.v_combo.setMinimumSize(QSize(50, 0))
        self.v_combo.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_43.addWidget(self.v_combo)


        self.horizontalLayout_40.addWidget(self.widget_50)

        self.widget_57 = QWidget(self.widget_49)
        self.widget_57.setObjectName(u"widget_57")
        self.horizontalLayout_44 = QHBoxLayout(self.widget_57)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(-1, 0, -1, 0)
        self.label_50 = QLabel(self.widget_57)
        self.label_50.setObjectName(u"label_50")

        self.horizontalLayout_44.addWidget(self.label_50)

        self.q_combo = QComboBox(self.widget_57)
        self.q_combo.setObjectName(u"q_combo")
        sizePolicy.setHeightForWidth(self.q_combo.sizePolicy().hasHeightForWidth())
        self.q_combo.setSizePolicy(sizePolicy)
        self.q_combo.setMinimumSize(QSize(50, 0))
        self.q_combo.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_44.addWidget(self.q_combo)

        self.q_rune_combo = QComboBox(self.widget_57)
        self.q_rune_combo.setObjectName(u"q_rune_combo")
        sizePolicy.setHeightForWidth(self.q_rune_combo.sizePolicy().hasHeightForWidth())
        self.q_rune_combo.setSizePolicy(sizePolicy)
        self.q_rune_combo.setMinimumSize(QSize(40, 0))
        self.q_rune_combo.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_44.addWidget(self.q_rune_combo)

        self.horizontalLayout_44.setStretch(1, 3)
        self.horizontalLayout_44.setStretch(2, 2)

        self.horizontalLayout_40.addWidget(self.widget_57)

        self.widget_58 = QWidget(self.widget_49)
        self.widget_58.setObjectName(u"widget_58")
        self.horizontalLayout_45 = QHBoxLayout(self.widget_58)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(-1, 0, -1, 0)
        self.label_51 = QLabel(self.widget_58)
        self.label_51.setObjectName(u"label_51")

        self.horizontalLayout_45.addWidget(self.label_51)

        self.w_combo = QComboBox(self.widget_58)
        self.w_combo.setObjectName(u"w_combo")
        sizePolicy.setHeightForWidth(self.w_combo.sizePolicy().hasHeightForWidth())
        self.w_combo.setSizePolicy(sizePolicy)
        self.w_combo.setMinimumSize(QSize(50, 0))
        self.w_combo.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_45.addWidget(self.w_combo)

        self.w_rune_combo = QComboBox(self.widget_58)
        self.w_rune_combo.setObjectName(u"w_rune_combo")
        sizePolicy.setHeightForWidth(self.w_rune_combo.sizePolicy().hasHeightForWidth())
        self.w_rune_combo.setSizePolicy(sizePolicy)
        self.w_rune_combo.setMinimumSize(QSize(40, 0))
        self.w_rune_combo.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_45.addWidget(self.w_rune_combo)


        self.horizontalLayout_40.addWidget(self.widget_58)

        self.widget_59 = QWidget(self.widget_49)
        self.widget_59.setObjectName(u"widget_59")
        self.horizontalLayout_50 = QHBoxLayout(self.widget_59)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(-1, 0, -1, 0)
        self.label_52 = QLabel(self.widget_59)
        self.label_52.setObjectName(u"label_52")

        self.horizontalLayout_50.addWidget(self.label_52)

        self.e_combo = QComboBox(self.widget_59)
        self.e_combo.setObjectName(u"e_combo")
        sizePolicy.setHeightForWidth(self.e_combo.sizePolicy().hasHeightForWidth())
        self.e_combo.setSizePolicy(sizePolicy)
        self.e_combo.setMinimumSize(QSize(50, 0))
        self.e_combo.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_50.addWidget(self.e_combo)

        self.e_rune_combo = QComboBox(self.widget_59)
        self.e_rune_combo.setObjectName(u"e_rune_combo")
        sizePolicy.setHeightForWidth(self.e_rune_combo.sizePolicy().hasHeightForWidth())
        self.e_rune_combo.setSizePolicy(sizePolicy)
        self.e_rune_combo.setMinimumSize(QSize(40, 0))
        self.e_rune_combo.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_50.addWidget(self.e_rune_combo)


        self.horizontalLayout_40.addWidget(self.widget_59)

        self.frame_3 = QFrame(self.widget_49)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(-1, 0, -1, 0)
        self.label_53 = QLabel(self.frame_3)
        self.label_53.setObjectName(u"label_53")

        self.horizontalLayout_51.addWidget(self.label_53)

        self.r_combo = QComboBox(self.frame_3)
        self.r_combo.setObjectName(u"r_combo")
        sizePolicy.setHeightForWidth(self.r_combo.sizePolicy().hasHeightForWidth())
        self.r_combo.setSizePolicy(sizePolicy)
        self.r_combo.setMinimumSize(QSize(50, 0))
        self.r_combo.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_51.addWidget(self.r_combo)

        self.r_rune_combo = QComboBox(self.frame_3)
        self.r_rune_combo.setObjectName(u"r_rune_combo")
        sizePolicy.setHeightForWidth(self.r_rune_combo.sizePolicy().hasHeightForWidth())
        self.r_rune_combo.setSizePolicy(sizePolicy)
        self.r_rune_combo.setMinimumSize(QSize(40, 0))
        self.r_rune_combo.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_51.addWidget(self.r_rune_combo)


        self.horizontalLayout_40.addWidget(self.frame_3)

        self.horizontalLayout_40.setStretch(0, 2)
        self.horizontalLayout_40.setStretch(1, 3)
        self.horizontalLayout_40.setStretch(2, 3)
        self.horizontalLayout_40.setStretch(3, 3)
        self.horizontalLayout_40.setStretch(4, 3)

        self.verticalLayout_11.addWidget(self.widget_49)

        self.widget_60 = QWidget(self.widget_48)
        self.widget_60.setObjectName(u"widget_60")
        self.horizontalLayout_52 = QHBoxLayout(self.widget_60)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(-1, 0, -1, 0)
        self.widget_61 = QWidget(self.widget_60)
        self.widget_61.setObjectName(u"widget_61")
        self.horizontalLayout_53 = QHBoxLayout(self.widget_61)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(-1, 0, -1, 0)
        self.label_54 = QLabel(self.widget_61)
        self.label_54.setObjectName(u"label_54")

        self.horizontalLayout_53.addWidget(self.label_54)

        self.t_combo = QComboBox(self.widget_61)
        self.t_combo.setObjectName(u"t_combo")
        sizePolicy.setHeightForWidth(self.t_combo.sizePolicy().hasHeightForWidth())
        self.t_combo.setSizePolicy(sizePolicy)
        self.t_combo.setMinimumSize(QSize(50, 0))
        self.t_combo.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_53.addWidget(self.t_combo)


        self.horizontalLayout_52.addWidget(self.widget_61)

        self.widget_62 = QWidget(self.widget_60)
        self.widget_62.setObjectName(u"widget_62")
        self.horizontalLayout_54 = QHBoxLayout(self.widget_62)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(-1, 0, -1, 0)
        self.label_55 = QLabel(self.widget_62)
        self.label_55.setObjectName(u"label_55")

        self.horizontalLayout_54.addWidget(self.label_55)

        self.a_combo = QComboBox(self.widget_62)
        self.a_combo.setObjectName(u"a_combo")
        sizePolicy.setHeightForWidth(self.a_combo.sizePolicy().hasHeightForWidth())
        self.a_combo.setSizePolicy(sizePolicy)
        self.a_combo.setMinimumSize(QSize(50, 0))
        self.a_combo.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_54.addWidget(self.a_combo)

        self.a_rune_combo = QComboBox(self.widget_62)
        self.a_rune_combo.setObjectName(u"a_rune_combo")
        sizePolicy.setHeightForWidth(self.a_rune_combo.sizePolicy().hasHeightForWidth())
        self.a_rune_combo.setSizePolicy(sizePolicy)
        self.a_rune_combo.setMinimumSize(QSize(40, 0))
        self.a_rune_combo.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_54.addWidget(self.a_rune_combo)


        self.horizontalLayout_52.addWidget(self.widget_62)

        self.widget_63 = QWidget(self.widget_60)
        self.widget_63.setObjectName(u"widget_63")
        self.horizontalLayout_55 = QHBoxLayout(self.widget_63)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(-1, 0, -1, 0)
        self.label_56 = QLabel(self.widget_63)
        self.label_56.setObjectName(u"label_56")

        self.horizontalLayout_55.addWidget(self.label_56)

        self.s_combo = QComboBox(self.widget_63)
        self.s_combo.setObjectName(u"s_combo")
        sizePolicy.setHeightForWidth(self.s_combo.sizePolicy().hasHeightForWidth())
        self.s_combo.setSizePolicy(sizePolicy)
        self.s_combo.setMinimumSize(QSize(50, 0))
        self.s_combo.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_55.addWidget(self.s_combo)

        self.s_rune_combo = QComboBox(self.widget_63)
        self.s_rune_combo.setObjectName(u"s_rune_combo")
        sizePolicy.setHeightForWidth(self.s_rune_combo.sizePolicy().hasHeightForWidth())
        self.s_rune_combo.setSizePolicy(sizePolicy)
        self.s_rune_combo.setMinimumSize(QSize(40, 0))
        self.s_rune_combo.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_55.addWidget(self.s_rune_combo)


        self.horizontalLayout_52.addWidget(self.widget_63)

        self.widget_64 = QWidget(self.widget_60)
        self.widget_64.setObjectName(u"widget_64")
        self.horizontalLayout_56 = QHBoxLayout(self.widget_64)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(-1, 0, -1, 0)
        self.label_57 = QLabel(self.widget_64)
        self.label_57.setObjectName(u"label_57")

        self.horizontalLayout_56.addWidget(self.label_57)

        self.d_combo = QComboBox(self.widget_64)
        self.d_combo.setObjectName(u"d_combo")
        sizePolicy.setHeightForWidth(self.d_combo.sizePolicy().hasHeightForWidth())
        self.d_combo.setSizePolicy(sizePolicy)
        self.d_combo.setMinimumSize(QSize(50, 0))
        self.d_combo.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_56.addWidget(self.d_combo)

        self.d_rune_combo = QComboBox(self.widget_64)
        self.d_rune_combo.setObjectName(u"d_rune_combo")
        sizePolicy.setHeightForWidth(self.d_rune_combo.sizePolicy().hasHeightForWidth())
        self.d_rune_combo.setSizePolicy(sizePolicy)
        self.d_rune_combo.setMinimumSize(QSize(40, 0))
        self.d_rune_combo.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_56.addWidget(self.d_rune_combo)


        self.horizontalLayout_52.addWidget(self.widget_64)

        self.widget_65 = QWidget(self.widget_60)
        self.widget_65.setObjectName(u"widget_65")
        self.horizontalLayout_57 = QHBoxLayout(self.widget_65)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(-1, 0, -1, 0)
        self.label_58 = QLabel(self.widget_65)
        self.label_58.setObjectName(u"label_58")

        self.horizontalLayout_57.addWidget(self.label_58)

        self.f_combo = QComboBox(self.widget_65)
        self.f_combo.setObjectName(u"f_combo")
        sizePolicy.setHeightForWidth(self.f_combo.sizePolicy().hasHeightForWidth())
        self.f_combo.setSizePolicy(sizePolicy)
        self.f_combo.setMinimumSize(QSize(50, 0))
        self.f_combo.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_57.addWidget(self.f_combo)

        self.f_rune_combo = QComboBox(self.widget_65)
        self.f_rune_combo.setObjectName(u"f_rune_combo")
        sizePolicy.setHeightForWidth(self.f_rune_combo.sizePolicy().hasHeightForWidth())
        self.f_rune_combo.setSizePolicy(sizePolicy)
        self.f_rune_combo.setMinimumSize(QSize(40, 0))
        self.f_rune_combo.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_57.addWidget(self.f_rune_combo)


        self.horizontalLayout_52.addWidget(self.widget_65)

        self.horizontalLayout_52.setStretch(0, 2)
        self.horizontalLayout_52.setStretch(1, 3)
        self.horizontalLayout_52.setStretch(2, 3)
        self.horizontalLayout_52.setStretch(3, 3)
        self.horizontalLayout_52.setStretch(4, 3)

        self.verticalLayout_11.addWidget(self.widget_60)

        self.line_8 = QFrame(self.widget_48)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_11.addWidget(self.line_8)

        self.frame = QFrame(self.widget_48)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.widget_2 = QWidget(self.frame)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.widget_66 = QWidget(self.widget_2)
        self.widget_66.setObjectName(u"widget_66")
        self.horizontalLayout_58 = QHBoxLayout(self.widget_66)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(2, 2, 2, 2)
        self.label_59 = QLabel(self.widget_66)
        self.label_59.setObjectName(u"label_59")

        self.horizontalLayout_58.addWidget(self.label_59)

        self.identity1_check = QCheckBox(self.widget_66)
        self.identity1_check.setObjectName(u"identity1_check")

        self.horizontalLayout_58.addWidget(self.identity1_check)

        self.identity1_line = QLineEdit(self.widget_66)
        self.identity1_line.setObjectName(u"identity1_line")

        self.horizontalLayout_58.addWidget(self.identity1_line)

        self.identity1_label = QLabel(self.widget_66)
        self.identity1_label.setObjectName(u"identity1_label")
        font = QFont()
        font.setPointSize(7)
        self.identity1_label.setFont(font)

        self.horizontalLayout_58.addWidget(self.identity1_label)

        self.horizontalLayout_58.setStretch(0, 1)
        self.horizontalLayout_58.setStretch(2, 1)
        self.horizontalLayout_58.setStretch(3, 10)

        self.verticalLayout.addWidget(self.widget_66)

        self.widget_67 = QWidget(self.widget_2)
        self.widget_67.setObjectName(u"widget_67")
        self.horizontalLayout_59 = QHBoxLayout(self.widget_67)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_59.setContentsMargins(2, 2, 2, 2)
        self.label_60 = QLabel(self.widget_67)
        self.label_60.setObjectName(u"label_60")

        self.horizontalLayout_59.addWidget(self.label_60)

        self.identity2_check = QCheckBox(self.widget_67)
        self.identity2_check.setObjectName(u"identity2_check")

        self.horizontalLayout_59.addWidget(self.identity2_check)

        self.identity2_line = QLineEdit(self.widget_67)
        self.identity2_line.setObjectName(u"identity2_line")

        self.horizontalLayout_59.addWidget(self.identity2_line)

        self.identity2_label = QLabel(self.widget_67)
        self.identity2_label.setObjectName(u"identity2_label")
        self.identity2_label.setFont(font)

        self.horizontalLayout_59.addWidget(self.identity2_label)

        self.horizontalLayout_59.setStretch(0, 1)
        self.horizontalLayout_59.setStretch(2, 1)
        self.horizontalLayout_59.setStretch(3, 10)

        self.verticalLayout.addWidget(self.widget_67)


        self.horizontalLayout.addWidget(self.widget_2)

        self.stance_widget = QWidget(self.frame)
        self.stance_widget.setObjectName(u"stance_widget")
        self.verticalLayout_2 = QVBoxLayout(self.stance_widget)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.stance1_check = QCheckBox(self.stance_widget)
        self.stance1_check.setObjectName(u"stance1_check")
        self.stance1_check.setEnabled(True)

        self.verticalLayout_2.addWidget(self.stance1_check)

        self.stance2_check = QCheckBox(self.stance_widget)
        self.stance2_check.setObjectName(u"stance2_check")

        self.verticalLayout_2.addWidget(self.stance2_check)


        self.horizontalLayout.addWidget(self.stance_widget)

        self.horizontalLayout.setStretch(0, 5)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout_11.addWidget(self.frame)


        self.verticalLayout_7.addWidget(self.widget_48)

        self.verticalLayout_7.setStretch(0, 1)
        self.verticalLayout_7.setStretch(2, 3)

        self.horizontalLayout_24.addWidget(self.widget_5)

        self.line_10 = QFrame(self.widget_33)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.VLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_24.addWidget(self.line_10)

        self.widget_68 = QWidget(self.widget_33)
        self.widget_68.setObjectName(u"widget_68")
        self.verticalLayout_5 = QVBoxLayout(self.widget_68)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 2, -1, 2)
        self.widget_69 = QWidget(self.widget_68)
        self.widget_69.setObjectName(u"widget_69")
        self.verticalLayout_13 = QVBoxLayout(self.widget_69)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(-1, 0, -1, 0)
        self.widget_70 = QWidget(self.widget_69)
        self.widget_70.setObjectName(u"widget_70")
        self.horizontalLayout_61 = QHBoxLayout(self.widget_70)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(2, 2, 2, 2)
        self.label_61 = QLabel(self.widget_70)
        self.label_61.setObjectName(u"label_61")

        self.horizontalLayout_61.addWidget(self.label_61)

        self.widget_17 = QWidget(self.widget_70)
        self.widget_17.setObjectName(u"widget_17")
        self.verticalLayout_6 = QVBoxLayout(self.widget_17)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 2, -1, 2)
        self.widget_15 = QWidget(self.widget_17)
        self.widget_15.setObjectName(u"widget_15")
        self.horizontalLayout_16 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(-1, 0, -1, 0)
        self.nak1_combo = QComboBox(self.widget_15)
        self.nak1_combo.setObjectName(u"nak1_combo")

        self.horizontalLayout_16.addWidget(self.nak1_combo)

        self.nak1_line = QLineEdit(self.widget_15)
        self.nak1_line.setObjectName(u"nak1_line")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.nak1_line.sizePolicy().hasHeightForWidth())
        self.nak1_line.setSizePolicy(sizePolicy1)

        self.horizontalLayout_16.addWidget(self.nak1_line)

        self.label_62 = QLabel(self.widget_15)
        self.label_62.setObjectName(u"label_62")

        self.horizontalLayout_16.addWidget(self.label_62)


        self.verticalLayout_6.addWidget(self.widget_15)

        self.widget_16 = QWidget(self.widget_17)
        self.widget_16.setObjectName(u"widget_16")
        self.horizontalLayout_17 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(-1, 0, -1, 0)
        self.nak2_combo = QComboBox(self.widget_16)
        self.nak2_combo.setObjectName(u"nak2_combo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.nak2_combo.sizePolicy().hasHeightForWidth())
        self.nak2_combo.setSizePolicy(sizePolicy2)

        self.horizontalLayout_17.addWidget(self.nak2_combo)

        self.nak2_line = QLineEdit(self.widget_16)
        self.nak2_line.setObjectName(u"nak2_line")
        sizePolicy1.setHeightForWidth(self.nak2_line.sizePolicy().hasHeightForWidth())
        self.nak2_line.setSizePolicy(sizePolicy1)

        self.horizontalLayout_17.addWidget(self.nak2_line)

        self.label_63 = QLabel(self.widget_16)
        self.label_63.setObjectName(u"label_63")

        self.horizontalLayout_17.addWidget(self.label_63)


        self.verticalLayout_6.addWidget(self.widget_16)


        self.horizontalLayout_61.addWidget(self.widget_17)


        self.verticalLayout_13.addWidget(self.widget_70)

        self.widget_71 = QWidget(self.widget_69)
        self.widget_71.setObjectName(u"widget_71")
        self.horizontalLayout_62 = QHBoxLayout(self.widget_71)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setContentsMargins(2, 2, 2, 2)
        self.label_64 = QLabel(self.widget_71)
        self.label_64.setObjectName(u"label_64")

        self.horizontalLayout_62.addWidget(self.label_64)

        self.widget_20 = QWidget(self.widget_71)
        self.widget_20.setObjectName(u"widget_20")
        self.verticalLayout_3 = QVBoxLayout(self.widget_20)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.widget_18 = QWidget(self.widget_20)
        self.widget_18.setObjectName(u"widget_18")
        self.horizontalLayout_18 = QHBoxLayout(self.widget_18)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(-1, 0, -1, 0)
        self.veff1_combo = QComboBox(self.widget_18)
        self.veff1_combo.setObjectName(u"veff1_combo")

        self.horizontalLayout_18.addWidget(self.veff1_combo)

        self.veff1_line = QLineEdit(self.widget_18)
        self.veff1_line.setObjectName(u"veff1_line")
        sizePolicy1.setHeightForWidth(self.veff1_line.sizePolicy().hasHeightForWidth())
        self.veff1_line.setSizePolicy(sizePolicy1)

        self.horizontalLayout_18.addWidget(self.veff1_line)

        self.label_65 = QLabel(self.widget_18)
        self.label_65.setObjectName(u"label_65")

        self.horizontalLayout_18.addWidget(self.label_65)


        self.verticalLayout_3.addWidget(self.widget_18)

        self.widget_19 = QWidget(self.widget_20)
        self.widget_19.setObjectName(u"widget_19")
        self.horizontalLayout_19 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(-1, 0, -1, 0)
        self.veff2_combo = QComboBox(self.widget_19)
        self.veff2_combo.setObjectName(u"veff2_combo")

        self.horizontalLayout_19.addWidget(self.veff2_combo)

        self.veff2_line = QLineEdit(self.widget_19)
        self.veff2_line.setObjectName(u"veff2_line")
        sizePolicy1.setHeightForWidth(self.veff2_line.sizePolicy().hasHeightForWidth())
        self.veff2_line.setSizePolicy(sizePolicy1)

        self.horizontalLayout_19.addWidget(self.veff2_line)

        self.label_66 = QLabel(self.widget_19)
        self.label_66.setObjectName(u"label_66")

        self.horizontalLayout_19.addWidget(self.label_66)


        self.verticalLayout_3.addWidget(self.widget_19)


        self.horizontalLayout_62.addWidget(self.widget_20)


        self.verticalLayout_13.addWidget(self.widget_71)


        self.verticalLayout_5.addWidget(self.widget_69)

        self.widget_73 = QWidget(self.widget_68)
        self.widget_73.setObjectName(u"widget_73")
        self.horizontalLayout_63 = QHBoxLayout(self.widget_73)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(-1, 2, -1, 2)
        self.label_67 = QLabel(self.widget_73)
        self.label_67.setObjectName(u"label_67")

        self.horizontalLayout_63.addWidget(self.label_67)

        self.speed_line = QLineEdit(self.widget_73)
        self.speed_line.setObjectName(u"speed_line")
        sizePolicy1.setHeightForWidth(self.speed_line.sizePolicy().hasHeightForWidth())
        self.speed_line.setSizePolicy(sizePolicy1)

        self.horizontalLayout_63.addWidget(self.speed_line)

        self.label_68 = QLabel(self.widget_73)
        self.label_68.setObjectName(u"label_68")

        self.horizontalLayout_63.addWidget(self.label_68)


        self.verticalLayout_5.addWidget(self.widget_73)

        self.btn_analysis = QPushButton(self.widget_68)
        self.btn_analysis.setObjectName(u"btn_analysis")

        self.verticalLayout_5.addWidget(self.btn_analysis)


        self.horizontalLayout_24.addWidget(self.widget_68)

        self.horizontalLayout_24.setStretch(0, 3)
        self.horizontalLayout_24.setStretch(2, 1)

        self.verticalLayout_21.addWidget(self.widget_33)

        self.line_3 = QFrame(analysis)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_21.addWidget(self.line_3)

        self.widget_74 = QWidget(analysis)
        self.widget_74.setObjectName(u"widget_74")
        self.verticalLayout_15 = QVBoxLayout(self.widget_74)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(-1, 0, -1, 0)
        self.widget_22 = QWidget(self.widget_74)
        self.widget_22.setObjectName(u"widget_22")
        self.horizontalLayout_21 = QHBoxLayout(self.widget_22)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(-1, 2, -1, 2)
        self.label_69 = QLabel(self.widget_22)
        self.label_69.setObjectName(u"label_69")

        self.horizontalLayout_21.addWidget(self.label_69)

        self.total_time_text = QLabel(self.widget_22)
        self.total_time_text.setObjectName(u"total_time_text")

        self.horizontalLayout_21.addWidget(self.total_time_text)

        self.horizontalLayout_21.setStretch(1, 1)

        self.verticalLayout_15.addWidget(self.widget_22)

        self.widget_76 = QWidget(self.widget_74)
        self.widget_76.setObjectName(u"widget_76")
        self.horizontalLayout_15 = QHBoxLayout(self.widget_76)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, 0, -1, 0)
        self.widget_78 = QWidget(self.widget_76)
        self.widget_78.setObjectName(u"widget_78")
        self.verticalLayout_4 = QVBoxLayout(self.widget_78)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.nak_time_text = QLabel(self.widget_78)
        self.nak_time_text.setObjectName(u"nak_time_text")

        self.verticalLayout_4.addWidget(self.nak_time_text)

        self.veff_time_text = QLabel(self.widget_78)
        self.veff_time_text.setObjectName(u"veff_time_text")

        self.verticalLayout_4.addWidget(self.veff_time_text)

        self.ad_time_text = QLabel(self.widget_78)
        self.ad_time_text.setObjectName(u"ad_time_text")

        self.verticalLayout_4.addWidget(self.ad_time_text)


        self.horizontalLayout_15.addWidget(self.widget_78)

        self.line_2 = QFrame(self.widget_76)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_15.addWidget(self.line_2)

        self.widget_79 = QWidget(self.widget_76)
        self.widget_79.setObjectName(u"widget_79")
        self.horizontalLayout_20 = QHBoxLayout(self.widget_79)
        self.horizontalLayout_20.setSpacing(2)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(-1, 2, -1, 2)
        self.label_70 = QLabel(self.widget_79)
        self.label_70.setObjectName(u"label_70")

        self.horizontalLayout_20.addWidget(self.label_70)

        self.widget_21 = QWidget(self.widget_79)
        self.widget_21.setObjectName(u"widget_21")
        self.verticalLayout_8 = QVBoxLayout(self.widget_21)
        self.verticalLayout_8.setSpacing(2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.widget_81 = QWidget(self.widget_21)
        self.widget_81.setObjectName(u"widget_81")
        self.horizontalLayout_68 = QHBoxLayout(self.widget_81)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.horizontalLayout_68.setContentsMargins(-1, 2, -1, 2)
        self.no_v_text = QLabel(self.widget_81)
        self.no_v_text.setObjectName(u"no_v_text")

        self.horizontalLayout_68.addWidget(self.no_v_text)

        self.no_q_text = QLabel(self.widget_81)
        self.no_q_text.setObjectName(u"no_q_text")

        self.horizontalLayout_68.addWidget(self.no_q_text)

        self.no_w_text = QLabel(self.widget_81)
        self.no_w_text.setObjectName(u"no_w_text")

        self.horizontalLayout_68.addWidget(self.no_w_text)

        self.no_e_text = QLabel(self.widget_81)
        self.no_e_text.setObjectName(u"no_e_text")

        self.horizontalLayout_68.addWidget(self.no_e_text)

        self.no_r_text = QLabel(self.widget_81)
        self.no_r_text.setObjectName(u"no_r_text")

        self.horizontalLayout_68.addWidget(self.no_r_text)

        self.no_z_text = QLabel(self.widget_81)
        self.no_z_text.setObjectName(u"no_z_text")

        self.horizontalLayout_68.addWidget(self.no_z_text)

        self.no_z1_text = QLabel(self.widget_81)
        self.no_z1_text.setObjectName(u"no_z1_text")

        self.horizontalLayout_68.addWidget(self.no_z1_text)

        self.no_z2_text = QLabel(self.widget_81)
        self.no_z2_text.setObjectName(u"no_z2_text")

        self.horizontalLayout_68.addWidget(self.no_z2_text)

        self.no_z3_text = QLabel(self.widget_81)
        self.no_z3_text.setObjectName(u"no_z3_text")

        self.horizontalLayout_68.addWidget(self.no_z3_text)


        self.verticalLayout_8.addWidget(self.widget_81)

        self.widget_80 = QWidget(self.widget_21)
        self.widget_80.setObjectName(u"widget_80")
        self.horizontalLayout_67 = QHBoxLayout(self.widget_80)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_67.setContentsMargins(-1, 2, -1, 2)
        self.no_t_text = QLabel(self.widget_80)
        self.no_t_text.setObjectName(u"no_t_text")

        self.horizontalLayout_67.addWidget(self.no_t_text)

        self.no_a_text = QLabel(self.widget_80)
        self.no_a_text.setObjectName(u"no_a_text")

        self.horizontalLayout_67.addWidget(self.no_a_text)

        self.no_s_text = QLabel(self.widget_80)
        self.no_s_text.setObjectName(u"no_s_text")

        self.horizontalLayout_67.addWidget(self.no_s_text)

        self.no_d_text = QLabel(self.widget_80)
        self.no_d_text.setObjectName(u"no_d_text")

        self.horizontalLayout_67.addWidget(self.no_d_text)

        self.no_f_text = QLabel(self.widget_80)
        self.no_f_text.setObjectName(u"no_f_text")

        self.horizontalLayout_67.addWidget(self.no_f_text)

        self.no_x_text = QLabel(self.widget_80)
        self.no_x_text.setObjectName(u"no_x_text")

        self.horizontalLayout_67.addWidget(self.no_x_text)

        self.no_x1_text = QLabel(self.widget_80)
        self.no_x1_text.setObjectName(u"no_x1_text")

        self.horizontalLayout_67.addWidget(self.no_x1_text)

        self.no_x2_text = QLabel(self.widget_80)
        self.no_x2_text.setObjectName(u"no_x2_text")

        self.horizontalLayout_67.addWidget(self.no_x2_text)

        self.no_x3_text = QLabel(self.widget_80)
        self.no_x3_text.setObjectName(u"no_x3_text")

        self.horizontalLayout_67.addWidget(self.no_x3_text)


        self.verticalLayout_8.addWidget(self.widget_80)


        self.horizontalLayout_20.addWidget(self.widget_21)

        self.horizontalLayout_20.setStretch(0, 1)
        self.horizontalLayout_20.setStretch(1, 20)

        self.horizontalLayout_15.addWidget(self.widget_79)

        self.horizontalLayout_15.setStretch(0, 1)
        self.horizontalLayout_15.setStretch(2, 5)

        self.verticalLayout_15.addWidget(self.widget_76)


        self.verticalLayout_21.addWidget(self.widget_74)

        self.line_11 = QFrame(analysis)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_21.addWidget(self.line_11)

        self.widget_102 = QWidget(analysis)
        self.widget_102.setObjectName(u"widget_102")
        self.horizontalLayout_87 = QHBoxLayout(self.widget_102)
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.horizontalLayout_87.setContentsMargins(-1, 2, -1, 2)
        self.label_95 = QLabel(self.widget_102)
        self.label_95.setObjectName(u"label_95")

        self.horizontalLayout_87.addWidget(self.label_95)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_87.addItem(self.horizontalSpacer)


        self.verticalLayout_21.addWidget(self.widget_102)

        self.Result_Widget = QWidget(analysis)
        self.Result_Widget.setObjectName(u"Result_Widget")
        self.Result_Widget.setStyleSheet(u"#Result_Widget {\n"
"	background-color: white; \n"
"	border: 1px solid block;  \n"
"}")
        self.Result_Layout = QVBoxLayout(self.Result_Widget)
        self.Result_Layout.setObjectName(u"Result_Layout")

        self.verticalLayout_21.addWidget(self.Result_Widget)

        self.line_9 = QFrame(analysis)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_21.addWidget(self.line_9)

        self.widget_7 = QWidget(analysis)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.widget_84 = QWidget(self.widget_7)
        self.widget_84.setObjectName(u"widget_84")
        self.verticalLayout_19 = QVBoxLayout(self.widget_84)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(-1, 0, -1, 0)
        self.label_71 = QLabel(self.widget_84)
        self.label_71.setObjectName(u"label_71")

        self.verticalLayout_19.addWidget(self.label_71)

        self.widget = QWidget(self.widget_84)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_6 = QHBoxLayout(self.widget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 0)

        self.verticalLayout_19.addWidget(self.widget)

        self.widget_88 = QWidget(self.widget_84)
        self.widget_88.setObjectName(u"widget_88")
        self.horizontalLayout_73 = QHBoxLayout(self.widget_88)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.horizontalLayout_73.setContentsMargins(-1, 0, -1, 0)
        self.widget_89 = QWidget(self.widget_88)
        self.widget_89.setObjectName(u"widget_89")
        self.horizontalLayout_74 = QHBoxLayout(self.widget_89)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.horizontalLayout_74.setContentsMargins(-1, 2, -1, 2)
        self.dmg_q_label = QLabel(self.widget_89)
        self.dmg_q_label.setObjectName(u"dmg_q_label")

        self.horizontalLayout_74.addWidget(self.dmg_q_label)

        self.dmg_q_line = QLineEdit(self.widget_89)
        self.dmg_q_line.setObjectName(u"dmg_q_line")

        self.horizontalLayout_74.addWidget(self.dmg_q_line)

        self.horizontalLayout_74.setStretch(0, 1)
        self.horizontalLayout_74.setStretch(1, 5)

        self.horizontalLayout_73.addWidget(self.widget_89)

        self.widget_92 = QWidget(self.widget_88)
        self.widget_92.setObjectName(u"widget_92")
        self.horizontalLayout_77 = QHBoxLayout(self.widget_92)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.horizontalLayout_77.setContentsMargins(-1, 2, -1, 2)
        self.dmg_w_label = QLabel(self.widget_92)
        self.dmg_w_label.setObjectName(u"dmg_w_label")

        self.horizontalLayout_77.addWidget(self.dmg_w_label)

        self.dmg_w_line = QLineEdit(self.widget_92)
        self.dmg_w_line.setObjectName(u"dmg_w_line")

        self.horizontalLayout_77.addWidget(self.dmg_w_line)

        self.horizontalLayout_77.setStretch(0, 1)
        self.horizontalLayout_77.setStretch(1, 5)

        self.horizontalLayout_73.addWidget(self.widget_92)

        self.widget_95 = QWidget(self.widget_88)
        self.widget_95.setObjectName(u"widget_95")
        self.horizontalLayout_80 = QHBoxLayout(self.widget_95)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.horizontalLayout_80.setContentsMargins(-1, 2, -1, 2)
        self.dmg_e_label = QLabel(self.widget_95)
        self.dmg_e_label.setObjectName(u"dmg_e_label")

        self.horizontalLayout_80.addWidget(self.dmg_e_label)

        self.dmg_e_line = QLineEdit(self.widget_95)
        self.dmg_e_line.setObjectName(u"dmg_e_line")

        self.horizontalLayout_80.addWidget(self.dmg_e_line)

        self.horizontalLayout_80.setStretch(0, 1)
        self.horizontalLayout_80.setStretch(1, 5)

        self.horizontalLayout_73.addWidget(self.widget_95)

        self.widget_98 = QWidget(self.widget_88)
        self.widget_98.setObjectName(u"widget_98")
        self.horizontalLayout_83 = QHBoxLayout(self.widget_98)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.horizontalLayout_83.setContentsMargins(-1, 2, -1, 2)
        self.dmg_r_label = QLabel(self.widget_98)
        self.dmg_r_label.setObjectName(u"dmg_r_label")

        self.horizontalLayout_83.addWidget(self.dmg_r_label)

        self.dmg_r_line = QLineEdit(self.widget_98)
        self.dmg_r_line.setObjectName(u"dmg_r_line")

        self.horizontalLayout_83.addWidget(self.dmg_r_line)

        self.horizontalLayout_83.setStretch(0, 1)
        self.horizontalLayout_83.setStretch(1, 5)

        self.horizontalLayout_73.addWidget(self.widget_98)

        self.horizontalLayout_73.setStretch(0, 1)
        self.horizontalLayout_73.setStretch(1, 1)
        self.horizontalLayout_73.setStretch(2, 1)
        self.horizontalLayout_73.setStretch(3, 1)

        self.verticalLayout_19.addWidget(self.widget_88)

        self.widget_91 = QWidget(self.widget_84)
        self.widget_91.setObjectName(u"widget_91")
        self.horizontalLayout_76 = QHBoxLayout(self.widget_91)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.horizontalLayout_76.setContentsMargins(-1, 0, -1, 0)
        self.widget_90 = QWidget(self.widget_91)
        self.widget_90.setObjectName(u"widget_90")
        self.horizontalLayout_75 = QHBoxLayout(self.widget_90)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.horizontalLayout_75.setContentsMargins(-1, 2, -1, 2)
        self.dmg_a_label = QLabel(self.widget_90)
        self.dmg_a_label.setObjectName(u"dmg_a_label")

        self.horizontalLayout_75.addWidget(self.dmg_a_label)

        self.dmg_a_line = QLineEdit(self.widget_90)
        self.dmg_a_line.setObjectName(u"dmg_a_line")

        self.horizontalLayout_75.addWidget(self.dmg_a_line)

        self.horizontalLayout_75.setStretch(0, 1)
        self.horizontalLayout_75.setStretch(1, 5)

        self.horizontalLayout_76.addWidget(self.widget_90)

        self.widget_93 = QWidget(self.widget_91)
        self.widget_93.setObjectName(u"widget_93")
        self.horizontalLayout_78 = QHBoxLayout(self.widget_93)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.horizontalLayout_78.setContentsMargins(-1, 2, -1, 2)
        self.dmg_s_label = QLabel(self.widget_93)
        self.dmg_s_label.setObjectName(u"dmg_s_label")

        self.horizontalLayout_78.addWidget(self.dmg_s_label)

        self.dmg_s_line = QLineEdit(self.widget_93)
        self.dmg_s_line.setObjectName(u"dmg_s_line")

        self.horizontalLayout_78.addWidget(self.dmg_s_line)

        self.horizontalLayout_78.setStretch(0, 1)
        self.horizontalLayout_78.setStretch(1, 5)

        self.horizontalLayout_76.addWidget(self.widget_93)

        self.widget_96 = QWidget(self.widget_91)
        self.widget_96.setObjectName(u"widget_96")
        self.horizontalLayout_81 = QHBoxLayout(self.widget_96)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.horizontalLayout_81.setContentsMargins(-1, 2, -1, 2)
        self.dmg_d_label = QLabel(self.widget_96)
        self.dmg_d_label.setObjectName(u"dmg_d_label")

        self.horizontalLayout_81.addWidget(self.dmg_d_label)

        self.dmg_d_line = QLineEdit(self.widget_96)
        self.dmg_d_line.setObjectName(u"dmg_d_line")

        self.horizontalLayout_81.addWidget(self.dmg_d_line)

        self.horizontalLayout_81.setStretch(0, 1)
        self.horizontalLayout_81.setStretch(1, 5)

        self.horizontalLayout_76.addWidget(self.widget_96)

        self.widget_99 = QWidget(self.widget_91)
        self.widget_99.setObjectName(u"widget_99")
        self.horizontalLayout_84 = QHBoxLayout(self.widget_99)
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.horizontalLayout_84.setContentsMargins(-1, 2, -1, 2)
        self.dmg_f_label = QLabel(self.widget_99)
        self.dmg_f_label.setObjectName(u"dmg_f_label")

        self.horizontalLayout_84.addWidget(self.dmg_f_label)

        self.dmg_f_line = QLineEdit(self.widget_99)
        self.dmg_f_line.setObjectName(u"dmg_f_line")

        self.horizontalLayout_84.addWidget(self.dmg_f_line)

        self.horizontalLayout_84.setStretch(0, 1)
        self.horizontalLayout_84.setStretch(1, 5)

        self.horizontalLayout_76.addWidget(self.widget_99)

        self.horizontalLayout_76.setStretch(0, 1)
        self.horizontalLayout_76.setStretch(1, 1)
        self.horizontalLayout_76.setStretch(2, 1)
        self.horizontalLayout_76.setStretch(3, 1)

        self.verticalLayout_19.addWidget(self.widget_91)

        self.widget_94 = QWidget(self.widget_84)
        self.widget_94.setObjectName(u"widget_94")
        self.horizontalLayout_79 = QHBoxLayout(self.widget_94)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.horizontalLayout_79.setContentsMargins(-1, 0, -1, 0)
        self.widget_8 = QWidget(self.widget_94)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 2, -1, 2)
        self.label = QLabel(self.widget_8)
        self.label.setObjectName(u"label")

        self.horizontalLayout_8.addWidget(self.label)

        self.dmg_z_line = QLineEdit(self.widget_8)
        self.dmg_z_line.setObjectName(u"dmg_z_line")

        self.horizontalLayout_8.addWidget(self.dmg_z_line)

        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 5)

        self.horizontalLayout_79.addWidget(self.widget_8)

        self.widget_9 = QWidget(self.widget_94)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 2, -1, 2)
        self.label_3 = QLabel(self.widget_9)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_9.addWidget(self.label_3)

        self.dmg_z1_line = QLineEdit(self.widget_9)
        self.dmg_z1_line.setObjectName(u"dmg_z1_line")

        self.horizontalLayout_9.addWidget(self.dmg_z1_line)

        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 5)

        self.horizontalLayout_79.addWidget(self.widget_9)

        self.widget_10 = QWidget(self.widget_94)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 2, -1, 2)
        self.label_4 = QLabel(self.widget_10)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_10.addWidget(self.label_4)

        self.dmg_z2_line = QLineEdit(self.widget_10)
        self.dmg_z2_line.setObjectName(u"dmg_z2_line")

        self.horizontalLayout_10.addWidget(self.dmg_z2_line)

        self.horizontalLayout_10.setStretch(0, 1)
        self.horizontalLayout_10.setStretch(1, 5)

        self.horizontalLayout_79.addWidget(self.widget_10)

        self.widget_11 = QWidget(self.widget_94)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, 2, -1, 2)
        self.label_5 = QLabel(self.widget_11)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_11.addWidget(self.label_5)

        self.dmg_z3_line = QLineEdit(self.widget_11)
        self.dmg_z3_line.setObjectName(u"dmg_z3_line")

        self.horizontalLayout_11.addWidget(self.dmg_z3_line)

        self.horizontalLayout_11.setStretch(0, 1)
        self.horizontalLayout_11.setStretch(1, 5)

        self.horizontalLayout_79.addWidget(self.widget_11)

        self.horizontalLayout_79.setStretch(0, 1)
        self.horizontalLayout_79.setStretch(1, 1)
        self.horizontalLayout_79.setStretch(2, 1)
        self.horizontalLayout_79.setStretch(3, 1)

        self.verticalLayout_19.addWidget(self.widget_94)

        self.widget_97 = QWidget(self.widget_84)
        self.widget_97.setObjectName(u"widget_97")
        self.horizontalLayout_82 = QHBoxLayout(self.widget_97)
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.horizontalLayout_82.setContentsMargins(-1, 0, -1, 0)
        self.widget_3 = QWidget(self.widget_97)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 2, -1, 2)
        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_7.addWidget(self.label_2)

        self.dmg_x_line = QLineEdit(self.widget_3)
        self.dmg_x_line.setObjectName(u"dmg_x_line")

        self.horizontalLayout_7.addWidget(self.dmg_x_line)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 5)

        self.horizontalLayout_82.addWidget(self.widget_3)

        self.widget_12 = QWidget(self.widget_97)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, 2, -1, 2)
        self.label_6 = QLabel(self.widget_12)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_12.addWidget(self.label_6)

        self.dmg_x1_line = QLineEdit(self.widget_12)
        self.dmg_x1_line.setObjectName(u"dmg_x1_line")

        self.horizontalLayout_12.addWidget(self.dmg_x1_line)

        self.horizontalLayout_12.setStretch(0, 1)
        self.horizontalLayout_12.setStretch(1, 5)

        self.horizontalLayout_82.addWidget(self.widget_12)

        self.widget_13 = QWidget(self.widget_97)
        self.widget_13.setObjectName(u"widget_13")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(-1, 2, -1, 2)
        self.label_7 = QLabel(self.widget_13)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_13.addWidget(self.label_7)

        self.dmg_x2_line = QLineEdit(self.widget_13)
        self.dmg_x2_line.setObjectName(u"dmg_x2_line")

        self.horizontalLayout_13.addWidget(self.dmg_x2_line)

        self.horizontalLayout_13.setStretch(0, 1)
        self.horizontalLayout_13.setStretch(1, 5)

        self.horizontalLayout_82.addWidget(self.widget_13)

        self.widget_14 = QWidget(self.widget_97)
        self.widget_14.setObjectName(u"widget_14")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, 2, -1, 2)
        self.label_8 = QLabel(self.widget_14)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_14.addWidget(self.label_8)

        self.dmg_x3_line = QLineEdit(self.widget_14)
        self.dmg_x3_line.setObjectName(u"dmg_x3_line")

        self.horizontalLayout_14.addWidget(self.dmg_x3_line)

        self.horizontalLayout_14.setStretch(0, 1)
        self.horizontalLayout_14.setStretch(1, 5)

        self.horizontalLayout_82.addWidget(self.widget_14)

        self.horizontalLayout_82.setStretch(0, 1)
        self.horizontalLayout_82.setStretch(1, 1)
        self.horizontalLayout_82.setStretch(2, 1)
        self.horizontalLayout_82.setStretch(3, 1)

        self.verticalLayout_19.addWidget(self.widget_97)

        self.widget_85 = QWidget(self.widget_84)
        self.widget_85.setObjectName(u"widget_85")
        self.horizontalLayout_70 = QHBoxLayout(self.widget_85)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.horizontalLayout_70.setContentsMargins(-1, 0, -1, 0)
        self.widget_86 = QWidget(self.widget_85)
        self.widget_86.setObjectName(u"widget_86")
        self.horizontalLayout_71 = QHBoxLayout(self.widget_86)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.horizontalLayout_71.setContentsMargins(-1, 2, -1, 2)
        self.label_72 = QLabel(self.widget_86)
        self.label_72.setObjectName(u"label_72")

        self.horizontalLayout_71.addWidget(self.label_72)

        self.dmg_v_line = QLineEdit(self.widget_86)
        self.dmg_v_line.setObjectName(u"dmg_v_line")

        self.horizontalLayout_71.addWidget(self.dmg_v_line)

        self.horizontalLayout_71.setStretch(0, 1)
        self.horizontalLayout_71.setStretch(1, 5)

        self.horizontalLayout_70.addWidget(self.widget_86)

        self.widget_87 = QWidget(self.widget_85)
        self.widget_87.setObjectName(u"widget_87")
        self.horizontalLayout_72 = QHBoxLayout(self.widget_87)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.horizontalLayout_72.setContentsMargins(-1, 2, -1, 2)
        self.label_73 = QLabel(self.widget_87)
        self.label_73.setObjectName(u"label_73")

        self.horizontalLayout_72.addWidget(self.label_73)

        self.dmg_t_line = QLineEdit(self.widget_87)
        self.dmg_t_line.setObjectName(u"dmg_t_line")

        self.horizontalLayout_72.addWidget(self.dmg_t_line)

        self.horizontalLayout_72.setStretch(0, 1)
        self.horizontalLayout_72.setStretch(1, 5)

        self.horizontalLayout_70.addWidget(self.widget_87)

        self.btn_damage = QPushButton(self.widget_85)
        self.btn_damage.setObjectName(u"btn_damage")

        self.horizontalLayout_70.addWidget(self.btn_damage)

        self.horizontalLayout_70.setStretch(0, 1)
        self.horizontalLayout_70.setStretch(1, 1)
        self.horizontalLayout_70.setStretch(2, 2)

        self.verticalLayout_19.addWidget(self.widget_85)


        self.horizontalLayout_5.addWidget(self.widget_84)

        self.line = QFrame(self.widget_7)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_5.addWidget(self.line)

        self.widget_82 = QWidget(self.widget_7)
        self.widget_82.setObjectName(u"widget_82")
        self.verticalLayout_18 = QVBoxLayout(self.widget_82)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(2, 2, 2, 2)
        self.widget_100 = QWidget(self.widget_82)
        self.widget_100.setObjectName(u"widget_100")
        self.verticalLayout_20 = QVBoxLayout(self.widget_100)
        self.verticalLayout_20.setSpacing(2)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(2, 2, 2, 2)
        self.label_82 = QLabel(self.widget_100)
        self.label_82.setObjectName(u"label_82")

        self.verticalLayout_20.addWidget(self.label_82)

        self.widget_101 = QWidget(self.widget_100)
        self.widget_101.setObjectName(u"widget_101")
        self.horizontalLayout_86 = QHBoxLayout(self.widget_101)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.horizontalLayout_86.setContentsMargins(-1, 0, -1, 0)
        self.dmg_q_text = QLabel(self.widget_101)
        self.dmg_q_text.setObjectName(u"dmg_q_text")

        self.horizontalLayout_86.addWidget(self.dmg_q_text)

        self.dmg_w_text = QLabel(self.widget_101)
        self.dmg_w_text.setObjectName(u"dmg_w_text")

        self.horizontalLayout_86.addWidget(self.dmg_w_text)

        self.dmg_e_text = QLabel(self.widget_101)
        self.dmg_e_text.setObjectName(u"dmg_e_text")

        self.horizontalLayout_86.addWidget(self.dmg_e_text)

        self.dmg_r_text = QLabel(self.widget_101)
        self.dmg_r_text.setObjectName(u"dmg_r_text")

        self.horizontalLayout_86.addWidget(self.dmg_r_text)

        self.horizontalLayout_86.setStretch(0, 1)
        self.horizontalLayout_86.setStretch(1, 1)
        self.horizontalLayout_86.setStretch(2, 1)
        self.horizontalLayout_86.setStretch(3, 1)

        self.verticalLayout_20.addWidget(self.widget_101)

        self.widget_23 = QWidget(self.widget_100)
        self.widget_23.setObjectName(u"widget_23")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_23)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.dmg_a_text = QLabel(self.widget_23)
        self.dmg_a_text.setObjectName(u"dmg_a_text")

        self.horizontalLayout_2.addWidget(self.dmg_a_text)

        self.dmg_s_text = QLabel(self.widget_23)
        self.dmg_s_text.setObjectName(u"dmg_s_text")

        self.horizontalLayout_2.addWidget(self.dmg_s_text)

        self.dmg_d_text = QLabel(self.widget_23)
        self.dmg_d_text.setObjectName(u"dmg_d_text")

        self.horizontalLayout_2.addWidget(self.dmg_d_text)

        self.dmg_f_text = QLabel(self.widget_23)
        self.dmg_f_text.setObjectName(u"dmg_f_text")

        self.horizontalLayout_2.addWidget(self.dmg_f_text)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 1)
        self.horizontalLayout_2.setStretch(3, 1)

        self.verticalLayout_20.addWidget(self.widget_23)

        self.widget_51 = QWidget(self.widget_100)
        self.widget_51.setObjectName(u"widget_51")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_51)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.dmg_z_text = QLabel(self.widget_51)
        self.dmg_z_text.setObjectName(u"dmg_z_text")

        self.horizontalLayout_3.addWidget(self.dmg_z_text)

        self.dmg_z1_text = QLabel(self.widget_51)
        self.dmg_z1_text.setObjectName(u"dmg_z1_text")

        self.horizontalLayout_3.addWidget(self.dmg_z1_text)

        self.dmg_z2_text = QLabel(self.widget_51)
        self.dmg_z2_text.setObjectName(u"dmg_z2_text")

        self.horizontalLayout_3.addWidget(self.dmg_z2_text)

        self.dmg_z3_text = QLabel(self.widget_51)
        self.dmg_z3_text.setObjectName(u"dmg_z3_text")

        self.horizontalLayout_3.addWidget(self.dmg_z3_text)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 1)
        self.horizontalLayout_3.setStretch(3, 1)

        self.verticalLayout_20.addWidget(self.widget_51)

        self.widget_6 = QWidget(self.widget_100)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.dmg_x_text = QLabel(self.widget_6)
        self.dmg_x_text.setObjectName(u"dmg_x_text")

        self.horizontalLayout_4.addWidget(self.dmg_x_text)

        self.dmg_x1_text = QLabel(self.widget_6)
        self.dmg_x1_text.setObjectName(u"dmg_x1_text")

        self.horizontalLayout_4.addWidget(self.dmg_x1_text)

        self.dmg_x2_text = QLabel(self.widget_6)
        self.dmg_x2_text.setObjectName(u"dmg_x2_text")

        self.horizontalLayout_4.addWidget(self.dmg_x2_text)

        self.dmg_x3_text = QLabel(self.widget_6)
        self.dmg_x3_text.setObjectName(u"dmg_x3_text")

        self.horizontalLayout_4.addWidget(self.dmg_x3_text)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout_4.setStretch(2, 1)
        self.horizontalLayout_4.setStretch(3, 1)

        self.verticalLayout_20.addWidget(self.widget_6)

        self.widget_4 = QWidget(self.widget_100)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_85 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.horizontalLayout_85.setContentsMargins(-1, 0, -1, 0)
        self.dmg_v_text = QLabel(self.widget_4)
        self.dmg_v_text.setObjectName(u"dmg_v_text")

        self.horizontalLayout_85.addWidget(self.dmg_v_text)

        self.dmg_t_text = QLabel(self.widget_4)
        self.dmg_t_text.setObjectName(u"dmg_t_text")

        self.horizontalLayout_85.addWidget(self.dmg_t_text)

        self.dmg_total_text = QLabel(self.widget_4)
        self.dmg_total_text.setObjectName(u"dmg_total_text")

        self.horizontalLayout_85.addWidget(self.dmg_total_text)

        self.horizontalLayout_85.setStretch(0, 1)
        self.horizontalLayout_85.setStretch(1, 1)
        self.horizontalLayout_85.setStretch(2, 2)

        self.verticalLayout_20.addWidget(self.widget_4)


        self.verticalLayout_18.addWidget(self.widget_100)

        self.verticalLayout_18.setStretch(0, 4)

        self.horizontalLayout_5.addWidget(self.widget_82)

        self.horizontalLayout_5.setStretch(0, 3)
        self.horizontalLayout_5.setStretch(2, 2)

        self.verticalLayout_21.addWidget(self.widget_7)

        self.verticalLayout_21.setStretch(5, 10)

        self.retranslateUi(analysis)

        QMetaObject.connectSlotsByName(analysis)
    # setupUi

    def retranslateUi(self, analysis):
        analysis.setWindowTitle(QCoreApplication.translate("analysis", u"\ubd84\uc11d", None))
        self.label_27.setText(QCoreApplication.translate("analysis", u"Class", None))
        self.btn_save.setText(QCoreApplication.translate("analysis", u"save", None))
        self.btn_load.setText(QCoreApplication.translate("analysis", u"load", None))
        self.label_48.setText(QCoreApplication.translate("analysis", u"v", None))
        self.label_50.setText(QCoreApplication.translate("analysis", u"q", None))
        self.label_51.setText(QCoreApplication.translate("analysis", u"w", None))
        self.label_52.setText(QCoreApplication.translate("analysis", u"e", None))
        self.label_53.setText(QCoreApplication.translate("analysis", u"r", None))
        self.label_54.setText(QCoreApplication.translate("analysis", u"t", None))
        self.label_55.setText(QCoreApplication.translate("analysis", u"a", None))
        self.label_56.setText(QCoreApplication.translate("analysis", u"s", None))
        self.label_57.setText(QCoreApplication.translate("analysis", u"d", None))
        self.label_58.setText(QCoreApplication.translate("analysis", u"f", None))
        self.label_59.setText(QCoreApplication.translate("analysis", u"\uc5d0\uc774\ud150\ud2f0\ud2f01", None))
        self.identity1_check.setText("")
        self.identity1_label.setText(QCoreApplication.translate("analysis", u"\uc544\uc774\ud150\ud2f0\ud2f01 \uc124\uba85", None))
        self.label_60.setText(QCoreApplication.translate("analysis", u"\uc544\uc774\ud150\ud2f0\ud2f02", None))
        self.identity2_check.setText("")
        self.identity2_label.setText(QCoreApplication.translate("analysis", u"\uc544\ub2c8\ud150\ud2f0\ud2f02 \uc124\uba85", None))
        self.stance1_check.setText(QCoreApplication.translate("analysis", u"stance1", None))
        self.stance2_check.setText(QCoreApplication.translate("analysis", u"stance2", None))
        self.label_61.setText(QCoreApplication.translate("analysis", u"\ub099\uc778\uc2a4\ud0ac", None))
        self.label_62.setText(QCoreApplication.translate("analysis", u"\ucd08", None))
        self.label_63.setText(QCoreApplication.translate("analysis", u"\ucd08", None))
        self.label_64.setText(QCoreApplication.translate("analysis", u"\uacf5\uc99d\uc2a4\ud0ac", None))
        self.label_65.setText(QCoreApplication.translate("analysis", u"\ucd08", None))
        self.label_66.setText(QCoreApplication.translate("analysis", u"\ucd08", None))
        self.label_67.setText(QCoreApplication.translate("analysis", u"\uacf5\uaca9\uc18d\ub3c4", None))
        self.label_68.setText(QCoreApplication.translate("analysis", u"%", None))
        self.btn_analysis.setText(QCoreApplication.translate("analysis", u"Analysis", None))
        self.label_69.setText(QCoreApplication.translate("analysis", u"\ubd84\uc11d \uacb0\uacfc", None))
        self.total_time_text.setText(QCoreApplication.translate("analysis", u"(\ucd1d\uc2dc\uac04 : \ucd08)", None))
        self.nak_time_text.setText(QCoreApplication.translate("analysis", u"\ub099\uc778\uc720\uc9c0 : \ucd08", None))
        self.veff_time_text.setText(QCoreApplication.translate("analysis", u"\uacf5\uc99d\uc720\uc9c0 : \ucd08", None))
        self.ad_time_text.setText(QCoreApplication.translate("analysis", u"\uc544\ub4dc\uc720\uc9c0 : \ucd08", None))
        self.label_70.setText(QCoreApplication.translate("analysis", u"\uc0ac\uc6a9 \ud69f\uc218", None))
        self.no_v_text.setText(QCoreApplication.translate("analysis", u"v", None))
        self.no_q_text.setText(QCoreApplication.translate("analysis", u"q", None))
        self.no_w_text.setText(QCoreApplication.translate("analysis", u"w", None))
        self.no_e_text.setText(QCoreApplication.translate("analysis", u"e", None))
        self.no_r_text.setText(QCoreApplication.translate("analysis", u"r", None))
        self.no_z_text.setText(QCoreApplication.translate("analysis", u"z", None))
        self.no_z1_text.setText(QCoreApplication.translate("analysis", u"z1", None))
        self.no_z2_text.setText(QCoreApplication.translate("analysis", u"z2", None))
        self.no_z3_text.setText(QCoreApplication.translate("analysis", u"z3", None))
        self.no_t_text.setText(QCoreApplication.translate("analysis", u"t", None))
        self.no_a_text.setText(QCoreApplication.translate("analysis", u"a", None))
        self.no_s_text.setText(QCoreApplication.translate("analysis", u"s", None))
        self.no_d_text.setText(QCoreApplication.translate("analysis", u"d", None))
        self.no_f_text.setText(QCoreApplication.translate("analysis", u"f", None))
        self.no_x_text.setText(QCoreApplication.translate("analysis", u"x", None))
        self.no_x1_text.setText(QCoreApplication.translate("analysis", u"x1", None))
        self.no_x2_text.setText(QCoreApplication.translate("analysis", u"x2", None))
        self.no_x3_text.setText(QCoreApplication.translate("analysis", u"x3", None))
        self.label_95.setText(QCoreApplication.translate("analysis", u"Time Table", None))
        self.label_71.setText(QCoreApplication.translate("analysis", u"\uc2a4\ud0ac \ub370\ubbf8\uc9c0", None))
        self.dmg_q_label.setText(QCoreApplication.translate("analysis", u"q", None))
        self.dmg_w_label.setText(QCoreApplication.translate("analysis", u"w", None))
        self.dmg_e_label.setText(QCoreApplication.translate("analysis", u"e", None))
        self.dmg_r_label.setText(QCoreApplication.translate("analysis", u"r", None))
        self.dmg_a_label.setText(QCoreApplication.translate("analysis", u"a", None))
        self.dmg_s_label.setText(QCoreApplication.translate("analysis", u"s", None))
        self.dmg_d_label.setText(QCoreApplication.translate("analysis", u"d", None))
        self.dmg_f_label.setText(QCoreApplication.translate("analysis", u"f", None))
        self.label.setText(QCoreApplication.translate("analysis", u"z", None))
        self.label_3.setText(QCoreApplication.translate("analysis", u"z1", None))
        self.label_4.setText(QCoreApplication.translate("analysis", u"z2", None))
        self.label_5.setText(QCoreApplication.translate("analysis", u"z3", None))
        self.label_2.setText(QCoreApplication.translate("analysis", u"x", None))
        self.label_6.setText(QCoreApplication.translate("analysis", u"x1", None))
        self.label_7.setText(QCoreApplication.translate("analysis", u"x2", None))
        self.label_8.setText(QCoreApplication.translate("analysis", u"x3", None))
        self.label_72.setText(QCoreApplication.translate("analysis", u"v", None))
        self.label_73.setText(QCoreApplication.translate("analysis", u"t", None))
        self.btn_damage.setText(QCoreApplication.translate("analysis", u"\ub370\ubbf8\uc9c0 \uacc4\uc0b0", None))
        self.label_82.setText(QCoreApplication.translate("analysis", u"Total Damage : (\ucd08\uac01\uc131\uae30 \uc81c\uc678)", None))
        self.dmg_q_text.setText(QCoreApplication.translate("analysis", u"q", None))
        self.dmg_w_text.setText(QCoreApplication.translate("analysis", u"w", None))
        self.dmg_e_text.setText(QCoreApplication.translate("analysis", u"e", None))
        self.dmg_r_text.setText(QCoreApplication.translate("analysis", u"r", None))
        self.dmg_a_text.setText(QCoreApplication.translate("analysis", u"a", None))
        self.dmg_s_text.setText(QCoreApplication.translate("analysis", u"s", None))
        self.dmg_d_text.setText(QCoreApplication.translate("analysis", u"d", None))
        self.dmg_f_text.setText(QCoreApplication.translate("analysis", u"f", None))
        self.dmg_z_text.setText(QCoreApplication.translate("analysis", u"z", None))
        self.dmg_z1_text.setText(QCoreApplication.translate("analysis", u"z1", None))
        self.dmg_z2_text.setText(QCoreApplication.translate("analysis", u"z2", None))
        self.dmg_z3_text.setText(QCoreApplication.translate("analysis", u"z3", None))
        self.dmg_x_text.setText(QCoreApplication.translate("analysis", u"x", None))
        self.dmg_x1_text.setText(QCoreApplication.translate("analysis", u"x1", None))
        self.dmg_x2_text.setText(QCoreApplication.translate("analysis", u"x2", None))
        self.dmg_x3_text.setText(QCoreApplication.translate("analysis", u"x3", None))
        self.dmg_v_text.setText(QCoreApplication.translate("analysis", u"v", None))
        self.dmg_t_text.setText(QCoreApplication.translate("analysis", u"t", None))
        self.dmg_total_text.setText(QCoreApplication.translate("analysis", u"Total : ", None))
    # retranslateUi

