#import numpy as np
import cv2
from Class.skill_check_function import skill_check_function, stack_check_function, custom_skill_check_function
from data import skill_speed, rune_speed, cooltime_check_Gunslinger_s_data

def Gunslinger_skill_check_function(img, skill_check_data, skill_table, frame):
    #stance 먼저 확인
    skill = skill_check_data['stance']

    sroi1=img[skill['y'][0]:skill['y'][0]+skill['sizey'][0], skill['x'][0]:skill['x'][0]+skill['sizex'][0]]
    sroi2=img[skill['y'][1]:skill['y'][1]+skill['sizey'][1], skill['x'][1]:skill['x'][1]+skill['sizex'][1]]

    prev_type = skill['type']

    mean1 = cv2.mean(sroi1)[:3]
    mean2 = cv2.mean(sroi2)[:3]
    mean = [mean1,mean2]#,mean3]
    mean_list = [item for tup in mean for item in tup]
    hand_ref = 15; shot_ref = 10; rifle_ref = 10
    hand  = [105,  67,  33,  31, 180, 234 ]#,  82,  31,  85]
    shot  = [ 86,  31,  86, 243, 204,  45 ]#,  31,  59,  91]
    rifle = [ 32,  59,  90, 248,  19, 197 ]#, 108,  71,  33]
    hand2  = [ 81,  31,  85,  30, 180, 235 ]

    if all(abs(m - h) < hand_ref for m, h in zip(mean_list, hand)) :
        new_type='hand'
    elif all(abs(m - h) < shot_ref for m, h in zip(mean_list, shot)) :
        new_type='shot'
    elif all(abs(m - h) < rifle_ref for m, h in zip(mean_list, rifle)) :
        new_type='rifle'
    elif all(abs(m - h) < hand_ref for m, h in zip(mean_list, hand2)) : # 사시에서 hand 면 1프레임 늦음
        new_type='hand'
        if prev_type != new_type and frame['start'] + 1 != frame['current'] : # 이전 스킬 사용된거 제거
            while skill_table and skill_table[-1][0] == frame['current'] - 1 :
                skill_table.pop()
    else:
        new_type = prev_type

    if prev_type != new_type or frame['start'] + 1 == frame['current'] : # 1프레임, 스탠스 바뀌는 경우
        skill['type'] = new_type
        skill_table.append([frame['current'], new_type])
        for key in ['q', 'w', 'e', 'r', 'a', 's', 'd', 'f']:
            skill_check_data[key]['state'] = 'cooltime'

    if prev_type != new_type and frame['start'] + 1 != frame['current'] : # 1프레임 아니고 스탠스 바뀌는 경우
        skill['state'] = 9

    if skill['state'] > 0 and skill['state'] <= 9:
        skill['state'] = skill['state'] - 1
        if skill['state'] < 9:
            return
        
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
        elif name in ['x']:
            sroi=img[skill['y']:skill['y']+skill['sizey'], skill['x']:skill['x']+skill['sizex']]
            zero_mean_ref = 10; one_mean_ref = 40; zero_ratio_ref = 0.8
            ssroi1=sroi[11:11+8, 18:18+4] #일의 자리 쿨  y, x
            ssroi2=sroi[11:11+8, 23:23+4] #십의 자리 쿨  y, x
            skill_state = custom_skill_check_function(ssroi1, ssroi2, skill['state'], cooltime_check_Gunslinger_s_data, zero_mean_ref, one_mean_ref, zero_ratio_ref )
            skill['state'] = skill_state

        # 스킬 테이블에 추가
        if skill['state']=='clicked':
            skill_table.append([frame['current'], name])

    return

def Gunslinger_analysis_function(filtered_skill_table, identity, default_speed, rune_combo_table, skill_speed_data, speed_veff_data, fps):
    identity_table = []
    identity_speed = int(identity[1]) # identity1
    identity_time = int(9*fps) # identity1
    selected_class ='건슬링어'

    speed_veff_data['x'] = skill_speed[selected_class]['x']['공속버프']
    skill_speed_data['x'] = skill_speed[selected_class]['x']['시전시간']
    rune_combo_table['x'] = '-'  

    if identity[0] == True:
        identity_skill = [row for row in filtered_skill_table if row[1] == 'hand' or row[1] == 'shot' or row[1] == 'rifle']
    else:
        identity_skill = [row for row in filtered_skill_table if row[1] == 'hand']

    # 공속 버프 타임라인 
    speed_veff_table = []  # 버프 [시작, 끝, 공속]
    # 스킬 버프 추가
    for skill_start, skill_name in filtered_skill_table: # filtered_skill_table = [시작, 스킬명]
        try:  # stance는 speed_veff_data 없음
            if speed_veff_data[skill_name][0] != 0:  # speed_veff_data = {스킬명 : [공속, 유지시간]}
                speed_veff_table.append([   int(skill_start), int(skill_start) + speed_veff_data[skill_name][1] , speed_veff_data[skill_name][0] ])
        except:
            continue

    for i in range(len(identity_skill)): #스탠스 변경 후 공속 추가
        identity_table.append([int(identity_skill[i][0]), int(identity_skill[i][0]) + identity_time, identity_speed])

    identity_table.sort(key=lambda x: x[0])
    results = []
    for start, end, value in identity_table:
        if not results:
            results.append([start, end, value])
        else:
            last_end = results[-1][1]
            if start <= last_end:
                results[-1][1] = max(last_end, end)
            else:
                results.append([start, end, value])

    for result in results:
        speed_veff_table.append(result)

    speed_veff_table = sorted(speed_veff_table, key=lambda x: int(x[0])) #오름차순 정리

    # 스킬 타임 테이블 
    skill_time_table=[] # 스킬 [시작, 시전시간, 스킬명]

    filtered_skill_table_stance = []

    for time, action in filtered_skill_table:
        if action in ['shot', 'rifle']:
            add_slash = True
            filtered_skill_table_stance.append([time, action])
        elif action == 'hand':
            add_slash = False
            filtered_skill_table_stance.append([time, action])
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
            #직업 별 스킬 테이블 작성
            skill_time_table.append([int(skill_start) - int(skill_speed_data[skill_name][0]/speed*100),  #skill_speed_data = {스킬명: [선시전시간, 후시전시간 ]} 
                                int(skill_start) + int(skill_speed_data[skill_name][1]/speed*100), skill_name ] )
        except:
            continue

    return skill_time_table


