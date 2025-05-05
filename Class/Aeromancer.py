import numpy as np
import cv2
from Class.skill_check_function import skill_check_function, stack_check_function, custom_skill_check_function
from data import skill_speed, rune_speed, cooltime_check_Aeromancer_s_data

def Aeromancer_skill_check_function(img, skill_check_data, skill_table, frame):
    for name, skill in skill_check_data.items():
        #s로 쿨타임
        if name in ['q', 'w', 'e', 'r', 'a', 's', 'd', 'f', 't', 'v']:
            sroi=img[skill['y']:skill['y']+skill['sizey'], skill['x']:skill['x']+skill['sizex']]
            if skill['type'] == 'normal':
                skill_state = skill_check_function(sroi, skill['state'])
                skill['state'] = skill_state # ready cooltime clicked
            elif skill['type'] == 'stack zero' or skill['type'] == 'stack one' or skill['type'] == 'stack two':
                skill_state, skill_type = stack_check_function(sroi, skill['state'], skill['type'])
                skill['state'] = skill_state
                skill['type'] = skill_type

        elif name in ['x']:
            sroi=img[skill['y']:skill['y']+skill['sizey'], skill['x']:skill['x']+skill['sizex']]
            zero_mean_ref = 10; one_mean_ref = 30; zero_ratio_ref = 0.8
            ssroi1=sroi[13:13+6,20:20+3]  #일의 자리 쿨  y, x 
            ssroi2=sroi[13:13+6,17:17+3]  #십의 자리 쿨  y, x
            skill_state = custom_skill_check_function(ssroi1, ssroi2, skill['state'], cooltime_check_Aeromancer_s_data, zero_mean_ref, one_mean_ref, zero_ratio_ref )
            skill['state'] = skill_state

        elif name in ['z']:
            sroi1=img[skill['y'][0]:skill['y'][0]+skill['sizey'][0], skill['x'][0]:skill['x'][0]+skill['sizex'][0]]
            sroi2=img[skill['y'][1]:skill['y'][1]+skill['sizey'][1], skill['x'][1]:skill['x'][1]+skill['sizex'][1]]

            mean1 = cv2.mean(sroi1)[:3]
            #if all(abs(c - t) < 25 for c, t in zip(mean1, (145, 165, 200))) and skill['state'] == 'ready':
            if mean1[1]-mean1[0] > 10 and mean1[2] > 180 and skill['state'] == 'ready'  :
                skill_table.append([frame['current'], name])
                skill['state'] = 'cooltime'

            gray_sroi = cv2.cvtColor(sroi2, cv2.COLOR_BGR2GRAY)
            mean2 = np.mean(gray_sroi)
            if abs(mean2 - 45) < 10 and skill['state'] == 'cooltime':
                skill['state'] = 'ready'
                skill_table.append([frame['current'], name])

        # 스킬 테이블에 추가
        if skill['state'] == 'clicked':
            skill_table.append([frame['current'], name])

    return 

def Aeromancer_analysis_function(filtered_skill_table, identity, default_speed, rune_combo_table, skill_speed_data, speed_veff_data, fps):
    # identity = [ self.ui.identity1_check.isChecked(), self.ui.identity1_line.text() ,self.ui.identity2_check.isChecked(), self.ui.identity2_line.text()]
    identity_table=[]
    selected_class ='기상술사'

    speed_veff_data['z'] = skill_speed[selected_class]['z']['공속버프']
    skill_speed_data['z'] = skill_speed[selected_class]['z']['시전시간']
    rune_combo_table['z'] = '-'

    speed_veff_data['x'] = skill_speed[selected_class]['x']['공속버프']
    skill_speed_data['x'] = skill_speed[selected_class]['x']['시전시간']
    rune_combo_table['x'] = '-'  

    identity_skill = [row for row in filtered_skill_table if row[1] == 'z']

    #이슬비 온오프
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
    speed_veff_table = sorted(speed_veff_table, key=lambda x: int(x[0])) #오름차순 정리

    # 스킬 타임 테이블 --> 직업별 아이텐티티 적용 점화 캐스팅
    skill_time_table=[] # 스킬 [시작, 시전시간, 스킬명]
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
        if skill_name != 'z':
            skill_time_table.append([int(skill_start) - int(skill_speed_data[skill_name][0]/speed*100),  #skill_speed_data = {스킬명: [선시전시간, 후시전시간 ]} 
                            int(skill_start) + int(skill_speed_data[skill_name][1]/speed*100), skill_name ] )
        else:
            for identity_start, identity_end in identity_table:
                if identity_start == int(skill_start):
                    skill_time_table.append([identity_start, identity_end, skill_name] )  #skill_speed_data = {스킬명: [선시전시간, 후시전시간 ]} 

    return skill_time_table