import numpy as np
import cv2
from Class.skill_check_function import skill_check_function, stack_check_function, custom_skill_check_function
from data import skill_speed, rune_speed, cooltime_check_Glaivier_s_data

def Glaivier_skill_check_function(img, skill_check_data, skill_table, frame):
    #stance 먼저 확인
    skill = skill_check_data['stance']
    
    #stance 스킵 프레임
    if skill['state'] > 0 and skill['state'] <= 13:
        skill['state'] = skill['state'] - 1
        if skill['state'] < 13:
            return
    
    # stance 체크
    sroi1=img[skill['y']:skill['y']+skill['sizey'], skill['x']:skill['x']+skill['sizex']]
    sum_frame = cv2.mean(sroi1[4:6,0:22])[:3] #frame
    prev_type = skill['type']
    p=[None, None, None, None, None, None, None, None]
    if sum_frame[0] < 25 and sum_frame[1] < 25 and sum_frame[2] < 25:
        index = 0
        for i in [0, 6]:
            for j in [0, 6, 12, 18]:
                proi = sroi1[i:i+4, j:j+4]
                mean = cv2.mean(proi)[:3]
                if all(abs(c - t) < 25 for c, t in zip(mean, (50, 90, 245))):
                    p[index] = 'red'
                if all(abs(c - t) < 25 for c, t in zip(mean, (250, 150, 0))):
                    p[index] = 'blue'
                if all(abs(c - t) < 25 for c, t in zip(mean, (100, 100, 100))):
                    p[index] = 'gray'
                index += 1
    if None not in p:
        bubble_pass = False
        if 'blue' in p: new_type = 'pinnacle'
        elif 'red' in p: new_type = 'control'
        else: new_type = prev_type
    else: new_type = prev_type; bubble_pass = True

    #stance 변경시 스킵 프레임
    if prev_type != new_type and frame['start'] + 1 != frame['current'] :
        skill['state'] = 13
    
    #stance 변경시 바뀐 스킬 초기화
    if frame['start'] + 1 == frame['current'] or prev_type != new_type:
        skill['type'] = new_type
        skill_table.append([frame['current'], new_type])
        for key in ['q', 'w', 'e', 'r', 'a', 's', 'd', 'f']:
            skill_check_data[key]['state'] = 'cooltime'

    #버블  확인
    if bubble_pass != True:
        skill = skill_check_data['bubble']
        broi1=img[skill['y'][0]:skill['y'][0]+skill['sizey'][0], skill['x'][0]:skill['x'][0]+skill['sizex'][0]]
        broi2=img[skill['y'][1]:skill['y'][1]+skill['sizey'][1], skill['x'][1]:skill['x'][1]+skill['sizex'][1]]
        broi3=img[skill['y'][2]:skill['y'][2]+skill['sizey'][2], skill['x'][2]:skill['x'][2]+skill['sizex'][2]]
        if np.mean(broi3) < 100:
            if np.mean(broi2) < 100:
                if np.mean(broi1) < 100:
                    skill_state = 0
                elif np.mean(broi1) > 150:
                    skill_state = 1
                else: skill_state = skill['state']
            elif np.mean(broi2) > 150:
                skill_state = 2
            else: skill_state = skill['state']
        elif np.mean(broi3) > 150:
            skill_state = 3
        else: skill_state = skill['state']
        if skill_state != skill['state']:
            if skill_state < skill['state']: # and prev_type != new_type:
                skill_table.append([frame['current'], 'bubble'])
            skill['state'] = skill_state

    #스킬 확인
    for name, skill in skill_check_data.items():
        #s로 쿨타임
        #if name in ['a']:
        if name in ['q', 'w', 'e', 'r', 'a', 's', 'd', 'f', 't', 'v']:
            sroi=img[skill['y']:skill['y']+skill['sizey'], skill['x']:skill['x']+skill['sizex']]
            if skill['type'] == 'normal':
                skill_state = skill_check_function(sroi, skill['state'])
                skill_check_data[name]['state'] = skill_state # ready cooltime clicked
            elif skill['type'] == 'stack zero' or skill['type'] == 'stack one' or skill['type'] == 'stack two':
                skill_state, skill_type = stack_check_function(sroi, skill['state'], skill['type'])
                skill_check_data[name]['state'] = skill_state
                skill_check_data[name]['type'] = skill_type
                
        elif name in ['x']:
            sroi=img[skill['y']:skill['y']+skill['sizey'], skill['x']:skill['x']+skill['sizex']]
            zero_mean_ref = 10; one_mean_ref = 35; zero_ratio_ref = 0.8
            ssroi1=sroi[12:12+7,21:21+4] #일의 자리 쿨  y, x
            ssroi2=sroi[12:12+7,17:17+4] #십의 자리 쿨  y, x
            skill_state = custom_skill_check_function(ssroi1, ssroi2, skill['state'], cooltime_check_Glaivier_s_data, zero_mean_ref, one_mean_ref, zero_ratio_ref )
            skill['state'] = skill_state

        # 스킬 테이블에 추가
        if skill['state']=='clicked':
            skill_table.append([frame['current'], name])

    return

def Glaivier_analysis_function(filtered_skill_table, identity, default_speed, rune_combo_table, skill_speed_data, speed_veff_data, fps):
    # identity = [ self.ui.identity1_check.isChecked(), self.ui.identity1_line.text() ,self.ui.identity2_check.isChecked(), self.ui.identity2_line.text()]
    identity_table=[]
    selected_class ='창술사'

    speed_veff_data['z'] = skill_speed[selected_class]['z']['공속버프']
    skill_speed_data['z'] = skill_speed[selected_class]['z']['시전시간']
    rune_combo_table['z'] = '-'

    speed_veff_data['x'] = skill_speed[selected_class]['x']['공속버프']
    skill_speed_data['x'] = skill_speed[selected_class]['x']['시전시간']
    rune_combo_table['x'] = '-'  

    #stance_table = [row for row in filtered_skill_table if row[1] == 'control' or row[1] == 'pinnacle']
    bubble_table = [row for row in filtered_skill_table if row[1] == 'bubble']

    # 공속 버프 타임라인
    speed_veff_table = []  # 버프 [시작, 끝, 공속]
    # 스킬 버프 추가
    for skill_start, skill_name in filtered_skill_table: # filtered_skill_table = [시작, 스킬명]
        try:  # stance는 speed_veff_data 없음
            if speed_veff_data[skill_name][0] != 0:  # speed_veff_data = {스킬명 : [공속, 유지시간]}
                speed_veff_table.append([   int(skill_start), int(skill_start) + speed_veff_data[skill_name][1] , speed_veff_data[skill_name][0] ])
        except:
            continue


    speed_veff_table = sorted(speed_veff_table, key=lambda x: int(x[0])) #오름차순 정리

    # 스킬 타임 테이블 --> 직업별 아이텐티티 적용 점화 캐스팅
    skill_time_table=[] # 스킬 [시작, 시전시간, 스킬명]


    filtered_skill_table_stance = []

    for time, action in filtered_skill_table:
        if action == 'pinnacle':
            add_slash = True
            filtered_skill_table_stance.append([time, action])
        elif action == 'control':
            filtered_skill_table_stance.append([time, action])
            add_slash = False
        elif action in ['q', 'w', 'e', 'r', 'a', 's', 'd', 'f'] and add_slash:
            filtered_skill_table_stance.append([time, '/' + action])
        else:
            filtered_skill_table_stance.append([time, action])
        

    for skill_start, skill_name in filtered_skill_table_stance:
        try:  # stance는 skill_speed_data 없음
            add_speed = 0
            # 버프 테이블로 추가 공속 계산
            for speed_start, speed_ene, speed_veff in speed_veff_table: # speed_veff_table [시작, 끝, 공속]
                if  speed_start <= int(skill_start) and  int(skill_start) <= speed_ene:
                    add_speed = add_speed + speed_veff
            if skill_name in rune_combo_table: #룬 공속 추가
                add_speed += rune_speed[rune_combo_table[skill_name]]
            speed = default_speed + add_speed
            # 스킬 테이블 작성, 아이텐티티 때 시전시간이 변경되는 스킬 /  시전시간이 [선딜, 후딜, 아이텐티티선딜, 아이텐티티후딜]로 정의됨
            if skill_name == 'bubble' :
                skill_time_table.append([int(skill_start) - int(skill_speed_data['z'][0]/speed*100),  #skill_speed_data = {스킬명: [선시전시간, 후시전시간 ]} 
                                    int(skill_start) + int(skill_speed_data['z'][1]/speed*100), 'z' ] )
            else:
                skill_time_table.append([int(skill_start) - int(skill_speed_data[skill_name][0]/speed*100),  #skill_speed_data = {스킬명: [선시전시간, 후시전시간 ]} 
                                    int(skill_start) + int(skill_speed_data[skill_name][1]/speed*100), skill_name ] )
        except:
            continue

    return skill_time_table