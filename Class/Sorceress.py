#import numpy as np
import cv2
from Class.skill_check_function import skill_check_function, stack_check_function
from data import skill_speed, rune_speed

def Sorceress_skill_check_function(img, skill_check_data, skill_table, frame):
    for name, skill in skill_check_data.items():
        #s로 쿨타임
        if name in ['q', 'w', 'e', 'r', 'a', 's', 'd', 'f', 't', 'v']:
            sroi=img[skill['y']:skill['y']+skill['sizey'], skill['x']:skill['x']+skill['sizex']]
            if skill['type'] == 'normal':
                skill_state = skill_check_function(sroi, skill['state'])
                skill_check_data[name]['state'] = skill_state # ready cooltime clicked
            elif skill['type'] == 'stack zero' or skill['type'] == 'stack one' or skill['type'] == 'stack two':
                skill_state, skill_type = stack_check_function(sroi, skill['state'], skill['type'])
                skill_check_data[name]['state'] = skill_state
                skill_check_data[name]['type'] = skill_type

        #Laplacian 밝기 변화
        elif name == 'x': 
            sroi=img[skill['y']:skill['y']+skill['sizey'], skill['x']:skill['x']+skill['sizex']]
            gray_sroi = cv2.cvtColor(sroi, cv2.COLOR_BGR2GRAY)
            if len(skill['prev'])==1:
                frame_diffs = cv2.absdiff(skill['prev'][0], gray_sroi)
                diff_sum = sum(cv2.sumElems(frame_diffs))
                if diff_sum > skill['diffs'][0]:
                    skill_check_data[name]['state']='clicked'
                else:
                    skill_check_data[name]['state']='ready'
                skill['prev'][0] = gray_sroi.copy()
            else:                 
                skill['prev'].append(gray_sroi.copy())
        
        #위치 두군데 밝기
        elif name =='z': 
            sroi1=img[skill['y'][0]:skill['y'][0]+skill['sizey'][0], skill['x'][0]:skill['x'][0]+skill['sizex'][0]]
            sroi2=img[skill['y'][1]:skill['y'][1]+skill['sizey'][1], skill['x'][1]:skill['x'][1]+skill['sizex'][1]]
            gray_sroi1 = cv2.cvtColor(sroi1, cv2.COLOR_BGR2GRAY)
            gray_sroi2 = cv2.cvtColor(sroi2, cv2.COLOR_BGR2GRAY)
            if len(skill['prev'])==2:
                frame_diffs1 = cv2.absdiff(skill['prev'][0], gray_sroi1)
                diff_sum1 = sum(cv2.sumElems(frame_diffs1))
                frame_diffs2 = cv2.absdiff(skill['prev'][1], gray_sroi2)
                diff_sum2 = sum(cv2.sumElems(frame_diffs2))
                if diff_sum1 > skill['diffs'][0] and diff_sum2 > skill['diffs'][1]:
                    skill_check_data[name]['state']='clicked'
                else:
                    skill_check_data[name]['state']='ready'
                skill['prev'][0] = gray_sroi1.copy()
                skill['prev'][1] = gray_sroi2.copy()
            else:                 
                skill['prev'].append(gray_sroi1.copy())
                skill['prev'].append(gray_sroi2.copy())
        
        # 스킬 테이블에 추가
        if skill['state']=='clicked':
            skill_table.append([frame['current'], name])

    return 

def Sorceress_analysis_function(filtered_skill_table, identity, default_speed, rune_combo_table, skill_speed_data, speed_veff_data, fps):
    # identity = [ self.ui.identity1_check.isChecked(), self.ui.identity1_line.text() ,self.ui.identity2_check.isChecked(), self.ui.identity2_line.text()]
    identity_table=[] 
    identity_speed = 8 # identity1
    identity_time = 30*fps # identity1
    selected_class ='소서리스'

    speed_veff_data['z'] = skill_speed[selected_class]['z']['공속버프']
    skill_speed_data['z'] = skill_speed[selected_class]['z']['시전시간']
    rune_combo_table['z'] = '-'

    speed_veff_data['x'] = skill_speed[selected_class]['x']['공속버프']
    skill_speed_data['x'] = skill_speed[selected_class]['x']['시전시간']
    rune_combo_table['x'] = '-'  

    identity_skill = [row for row in filtered_skill_table if row[1] == 'z']

    #점화 온오프
    for i in range(0, len(identity_skill), 2):
        start = identity_skill[i][0]
        try:
            end = identity_skill[i + 1][0]
        except:
            end = filtered_skill_table[-1][0]
            identity_table.append([int(start), int(end)])
            break
        identity_table.append([int(start), int(end)])
    identity_table = sorted(identity_table, key=lambda x: int(x[0])) 

    # 공속 버프 타임라인
    speed_veff_table = []  # 버프 [시작, 끝, 공속]
    # 스킬 버프 추가
    for skill_start, skill_name in filtered_skill_table: # filtered_skill_table = [시작, 스킬명]
        if speed_veff_data[skill_name][0] != 0:  # speed_veff_data = {스킬명 : [공속, 유지시간]}
            speed_veff_table.append([   int(skill_start), int(skill_start) + speed_veff_data[skill_name][1] , speed_veff_data[skill_name][0] ])
    # 소서 아이텐티티 공속 추가 마나순환
    if identity[0] is True:
        for identity_start, identity_end in identity_table: # 점화 끝나고
            speed_veff_table.append([identity_end, identity_end + identity_time, identity_speed])

    if identity[2] is True:
        z_speed = float ( identity[3] )
    else: z_speed = 0

    speed_veff_table = sorted(speed_veff_table, key=lambda x: int(x[0])) #오름차순 정리

    # 스킬 타임 테이블 --> 직업별 아이텐티티 적용 점화 캐스팅
    skill_time_table=[] # 스킬 [시작, 끝, 스킬명]
    for skill_start, skill_name in filtered_skill_table:
        add_speed = 0
        # 버프 테이블로 추가 공속 계산
        for speed_start, speed_ene, speed_veff in speed_veff_table: # speed_veff_table [시작, 끝, 공속]
            if  speed_start <= int(skill_start) and  int(skill_start) <= speed_ene:
                add_speed = add_speed + speed_veff
        if skill_name in rune_combo_table: #룬 공속 추가
            add_speed += rune_speed[rune_combo_table[skill_name]]
        speed = default_speed + add_speed
        # 스킬 테이블 작성, 아이텐티티 때 시전시간이 변경되는 스킬 /  시전시간이 [선딜, 후딜, 아이텐티티선딜, 아이텐티티후딜]로 정의됨
        if len(skill_speed_data[skill_name])==2:
            skill_time_table.append([int(skill_start) - int(skill_speed_data[skill_name][0]/speed*100),  #skill_speed_data = {스킬명: [선시전시간, 후시전시간 ]} 
                                int(skill_start) + int(skill_speed_data[skill_name][1]/speed*100), skill_name ] )
        elif len(skill_speed_data[skill_name])==4:   ## 점화시 공속 달라지는 스킬
            for identity_start, identity_end in identity_table: # 점화 테이블
                if identity_start < int(skill_start) and int(skill_start) <= identity_end: #z 꺼지는거는 0,0 적용됨 = 없어서
                    skill_time_table.append([int(skill_start) - int(skill_speed_data[skill_name][2] / (100 + z_speed) * 100 ),  #skill_speed_data = {스킬명: [선시전시간, 후시전시간 ]} 
                                        int(skill_start) + int(skill_speed_data[skill_name][3] / (100 + z_speed) * 100 ), skill_name ] )
                elif identity_start == int(skill_start) and skill_name == 'z':
                    skill_time_table.append([identity_start, identity_end, skill_name] )  #skill_speed_data = {스킬명: [선시전시간, 후시전시간 ]} 
                elif skill_name != 'z':
                    skill_time_table.append([int(skill_start) - int(skill_speed_data[skill_name][0] / speed * 100),  #skill_speed_data = {스킬명: [선시전시간, 후시전시간 ]} 
                                        int(skill_start) + int(skill_speed_data[skill_name][1] / speed * 100), skill_name ] )
                    
    return skill_time_table