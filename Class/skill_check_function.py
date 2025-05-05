import numpy as np
import cv2
from data import cooltime_check_s_data, cooltime_check_m_data, stack_zero_check_data, stack_one_check_data, stack_two_check_data
from data import skill_speed, rune_speed

def General_skill_check_function(img, skill_check_data, skill_table, frame):
    for name, skill in skill_check_data.items():
        #s로 쿨타임
        if name in ['q', 'w', 'e', 'r', 'a', 's', 'd', 'f', 't', 'v']:
            sroi=img[skill['y']:skill['y']+skill['sizey'], skill['x']:skill['x']+skill['sizex']]
            if skill['type'] == 'normal':
                skill_state = skill_check_function(sroi, skill['state'])
                skill_check_data[name]['state'] = skill_state
            elif skill['type'] == 'stack zero' or skill['type'] == 'stack one' or skill['type'] == 'stack two':
                skill_state, skill_type = stack_check_function(sroi, skill['state'], skill['type'])
                skill_check_data[name]['state'] = skill_state
                skill_check_data[name]['type'] = skill_type
        
        # 스킬 테이블에 추가
        if skill['state']=='clicked':
            skill_table.append([frame['current'], name])

    return 

def General_analysis_function(filtered_skill_table, identity, default_speed, rune_combo_table, skill_speed_data, speed_veff_data, fps):
    # 공속 버프 타임라인
    speed_veff_table = []  # 버프 [시작, 끝, 공속]
    # 스킬 버프 추가
    for skill_start, skill_name in filtered_skill_table: # filtered_skill_table = [시작, 스킬명]
        try:
            if speed_veff_data[skill_name][0] != 0:  # speed_veff_data = {스킬명 : [공속, 유지시간]}
                speed_veff_table.append([   int(skill_start), int(skill_start) + speed_veff_data[skill_name][1] , speed_veff_data[skill_name][0] ])
        except:
            continue

    speed_veff_table = sorted(speed_veff_table, key=lambda x: int(x[0])) #오름차순 정리

    # 스킬 타임 테이블 --> 직업별 아이텐티티 적용 점화 캐스팅
    skill_time_table=[] # 스킬 [시작, 시전시간, 스킬명]
    for skill_start, skill_name in filtered_skill_table:
        try:
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


def custom_skill_check_function(ssroi1, ssroi2, skill_state, s_data, zero_mean_ref, one_mean_ref, zero_ratio_ref ):
    #일의 자리 쿨
    prev_roi1 =  cv2.Laplacian(cv2.cvtColor(ssroi1, cv2.COLOR_BGR2GRAY),-1)
    prev_roi1 = np.array(prev_roi1)
    zero_values1 = prev_roi1[s_data == 0]; one_values1 = prev_roi1[s_data == 1]
    zero_mean1 = np.mean(zero_values1); one_mean1 = np.mean(one_values1)
    zero_ratio1 = np.sum(zero_values1 < zero_mean_ref) / len(zero_values1)

    #십의 자리 쿨
    prev_roi2 =  cv2.Laplacian(cv2.cvtColor(ssroi2, cv2.COLOR_BGR2GRAY),-1)
    prev_roi2 = np.array(prev_roi2)
    zero_values2 = prev_roi2[s_data == 0]; one_values2 = prev_roi2[s_data == 1]
    zero_mean2 = np.mean(zero_values2); one_mean2 = np.mean(one_values2)
    zero_ratio2 = np.sum(zero_values2 < zero_mean_ref) / len(zero_values2)

    if zero_mean1 < zero_mean_ref and one_mean1 > one_mean_ref and zero_ratio1 > zero_ratio_ref :
        if skill_state == 'ready' : skill_state='clicked'
        elif skill_state == 'clicked' : skill_state='cooltime'
    elif zero_mean2 < zero_mean_ref and one_mean2 > one_mean_ref and zero_ratio2 > zero_ratio_ref :
        if skill_state == 'ready' : skill_state='clicked'
        elif skill_state == 'clicked' : skill_state='cooltime'
    else: skill_state='ready'
    return skill_state

def skill_check_function(sroi,skill_state):     
    #일의 자리 쿨       
    zero_mean_ref = 10
    one_mean_ref = 30
    zero_ratio_ref = 0.8
    ssroi=sroi[19:19+9,25:25+6]
    prev_roi1 =  cv2.Laplacian(cv2.cvtColor(ssroi, cv2.COLOR_BGR2GRAY),-1)
    prev_roi1 = np.array(prev_roi1)
    zero_values1 = prev_roi1[cooltime_check_s_data == 0]; one_values1 = prev_roi1[cooltime_check_s_data == 1]
    zero_mean1 = np.mean(zero_values1); one_mean1 = np.mean(one_values1)
    zero_ratio1 = np.sum(zero_values1 < zero_mean_ref) / len(zero_values1)

    #십의 자리 쿨
    ssroi=sroi[19:19+9,25+5:25+5+6]
    prev_roi2 =  cv2.Laplacian(cv2.cvtColor(ssroi, cv2.COLOR_BGR2GRAY),-1)
    prev_roi2 = np.array(prev_roi2)
    zero_values2 = prev_roi2[cooltime_check_s_data == 0]; one_values2 = prev_roi2[cooltime_check_s_data == 1]
    zero_mean2 = np.mean(zero_values2); one_mean2 = np.mean(one_values2)
    zero_ratio2 = np.sum(zero_values2 < zero_mean_ref) / len(zero_values2)

    #분단위 자리 쿨
    ssroi=sroi[19:19+9,22:25+9]
    prev_roi3 =  cv2.Laplacian(cv2.cvtColor(ssroi, cv2.COLOR_BGR2GRAY),-1)
    prev_roi3 = np.array(prev_roi3)
    zero_values3 = prev_roi3[cooltime_check_m_data == 0]; one_values3 = prev_roi3[cooltime_check_m_data == 1]
    zero_mean3 = np.mean(zero_values3); one_mean3 = np.mean(one_values3)
    zero_ratio3 = np.sum(zero_values3 < zero_mean_ref) / len(zero_values3)

    if zero_mean1 < zero_mean_ref and one_mean1 > one_mean_ref and zero_ratio1 > zero_ratio_ref :
        if skill_state == 'ready' : skill_state='clicked'
        elif skill_state == 'clicked' : skill_state='cooltime'
    elif zero_mean2 < zero_mean_ref and one_mean2 > one_mean_ref and zero_ratio2 > zero_ratio_ref :
        if skill_state == 'ready' : skill_state='clicked'
        elif skill_state == 'clicked' : skill_state='cooltime'
    elif zero_mean3 < zero_mean_ref and one_mean3 > one_mean_ref and zero_ratio3 > zero_ratio_ref :
        if skill_state == 'ready' : skill_state='clicked'
        elif skill_state == 'clicked' : skill_state='cooltime'
    else: skill_state='ready'
    return skill_state

def stack_check_function(sroi, skill_state, skill_type): # skill_state  == type혹은  state
    ssroi=sroi[29:29+11,36:36+7]
    prev_roi =  cv2.Laplacian(cv2.cvtColor(ssroi, cv2.COLOR_BGR2GRAY),-1)
    prev_roi = np.array(prev_roi)

    zero_values0 = prev_roi[stack_zero_check_data == 0]; one_values0 = prev_roi[stack_zero_check_data == 1]
    zero_mean0 = np.mean(zero_values0); one_mean0 = np.mean(one_values0)

    zero_values1 = prev_roi[stack_one_check_data == 0]; one_values1 = prev_roi[stack_one_check_data == 1]
    zero_mean1 = np.mean(zero_values1); one_mean1 = np.mean(one_values1)

    zero_values2 = prev_roi[stack_two_check_data == 0]; one_values2 = prev_roi[stack_two_check_data == 1]
    zero_mean2 = np.mean(zero_values2); one_mean2 = np.mean(one_values2)

    #stack 0 일때
    if zero_mean0 < 3 and one_mean0 > 20 :
        if skill_type == 'normal': skill_type = 'stack zero' #처음 확인시 stack으로 바뀜 
        elif skill_type == 'stack zero': skill_state = 'cooltime' #0유지
        elif skill_type == 'stack one': skill_state = 'clicked'; skill_type = 'stack zero' #1에서 0됨
    #stack 1 일때
    if zero_mean1 < 3 and one_mean1 > 20 :
        if skill_type == 'normal': skill_type = 'stack one' #처음 확인시 stack으로 바뀜 
        elif skill_type == 'stack zero': skill_type = 'stack one' #스택 +1
        elif skill_type == 'stack one': skill_state = 'cooltime' #1유지
        elif skill_type == 'stack two': skill_state = 'clicked'; skill_type = 'stack one' #2에서 1됨
    #stack 2 일때
    if zero_mean2 < 3 and one_mean2 > 20 :
        if skill_type == 'normal': skill_type = 'stack two' #처음 확인시 stack으로 바뀜 
        elif skill_type == 'stack zero': skill_state = 'ready'; skill_type = 'stack two' #스킬 사용 가능
        elif skill_type == 'stack one': skill_state = 'ready'; skill_type = 'stack two' #스킬 사용 가능
        elif skill_type == 'stack two': skill_state = 'ready' #스킬 사용 가능

    return skill_state, skill_type
