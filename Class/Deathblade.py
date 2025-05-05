import numpy as np
import cv2
from Class.skill_check_function import skill_check_function, stack_check_function
from data import skill_speed, rune_speed

def Deathblade_skill_check_function(img, skill_check_data, skill_table, frame):
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
                
        elif name in ['bubble']:
            sroi1=img[skill['y'][0]:skill['y'][0]+skill['sizey'][0], skill['x'][0]:skill['x'][0]+skill['sizex'][0]]
            sroi2=img[skill['y'][1]:skill['y'][1]+skill['sizey'][1], skill['x'][1]:skill['x'][1]+skill['sizex'][1]]
            sroi3=img[skill['y'][2]:skill['y'][2]+skill['sizey'][2], skill['x'][2]:skill['x'][2]+skill['sizex'][2]]
            sroi4=img[skill['y'][3]:skill['y'][3]+skill['sizey'][3], skill['x'][3]:skill['x'][3]+skill['sizex'][3]]
            gray_sroi1 = cv2.cvtColor(sroi1, cv2.COLOR_BGR2GRAY)
            mean1 = np.mean(gray_sroi1)
            gray_sroi2 = cv2.cvtColor(sroi2, cv2.COLOR_BGR2GRAY)
            mean2 = np.mean(gray_sroi2)
            gray_sroi3 = cv2.cvtColor(sroi3, cv2.COLOR_BGR2GRAY)
            mean3 = np.mean(gray_sroi3)
            gray_sroi4 = cv2.cvtColor(sroi4, cv2.COLOR_BGR2GRAY)
            mean4 = np.mean(gray_sroi4)
            if skill['type'] == 'normal':
                if mean1 < 200 and mean2 > 200 and mean4 > 180:
                    skill_table.append([frame['current'], 'Trance'])
                    skill['type'] = 'Trance'
                    skill['state'] = 'cooltime'
                else:
                    if mean4 > 180 and skill['state'] != 0 and skill['state'] != 'cooltime' :
                        skill_table.append([frame['current'], f'surge {skill['state']}'])
                        skill['state'] = 'cooltime'
                    if skill['state'] == 'cooltime' and mean1 < 100 and mean2 < 100 and mean3 < 100:
                        skill['state'] = 0
                    if skill['state'] != 'cooltime':
                        if mean1 > 130 :
                            skill['state'] = 1
                            if mean2 > 150 :
                                skill['state'] = 2
                                if mean3 > 130 :
                                    skill['state'] = 3
                        else:
                            skill['state'] = 0

            if skill['type'] == 'Trance':
                if mean4 < 100 and skill['state'] == 'cooltime' : #Trance 후 바로 ready
                    skill['state'] = 'ready'
                if mean4 > 180 and skill['state'] != 'cooltime' : #surge 후 cooltime
                    skill_table.append([frame['current'], 'surge'])
                    skill['state'] = 'cooltime'
                if  mean1 < 100 and mean2 < 100 and mean3 < 100: # surge 후 Trance 끝   skill['state'] == 'cooltime' and
                    skill_table.append([frame['current'], 'Trance'])
                    skill['state'] = 'ready'
                    skill['type'] = 'normal'

        # 스킬 테이블에 추가
        if skill['state']=='clicked':
            skill_table.append([frame['current'], name])

    return 


def Deathblade_analysis_function(filtered_skill_table, identity, default_speed, rune_combo_table, skill_speed_data, speed_veff_data, fps):
    # identity = [ self.ui.identity1_check.isChecked(), self.ui.identity1_line.text() ,self.ui.identity2_check.isChecked(), self.ui.identity2_line.text()]
    identity_table=[]
    selected_class ='블레이드'

    speed_veff_data['z'] = skill_speed[selected_class]['z']['공속버프']
    skill_speed_data['z'] = skill_speed[selected_class]['z']['시전시간']
    rune_combo_table['z'] = '-'

    speed_veff_data['x'] = skill_speed[selected_class]['x']['공속버프']
    skill_speed_data['x'] = skill_speed[selected_class]['x']['시전시간']
    rune_combo_table['x'] = '-'  

    identity_skill = [row for row in filtered_skill_table if row[1] == 'Trance']

    #Trance 온오프
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
        try:  # skill_speed_data 없는거 패스 ex) 텍스트로 된거 버스트 추가할거면 수정 필요
            if speed_veff_data[skill_name][0] != 0:  # speed_veff_data = {스킬명 : [공속, 유지시간]}
                speed_veff_table.append([   int(skill_start), int(skill_start) + speed_veff_data[skill_name][1] , speed_veff_data[skill_name][0] ])
        except:
            continue
    speed_veff_table = sorted(speed_veff_table, key=lambda x: int(x[0])) #오름차순 정리

    # 스킬 타임 테이블 --> 직업별 아이텐티티 적용 점화 캐스팅
    skill_time_table=[] # 스킬 [시작, 시전시간, 스킬명]
    for skill_start, skill_name in filtered_skill_table:
        add_speed = 0
        # 버프 테이블로 추가 공속 계산
        for speed_start, speed_ene, speed_veff in speed_veff_table: # speed_veff_table [시작, 끝, 공속]
            if  speed_start <= int(skill_start) and  int(skill_start) <= speed_ene:
                add_speed = add_speed + speed_veff
        if skill_name == 'surge' :
            skill_time_table.append([int(skill_start) - int(skill_speed_data['z'][0]/speed*100),  #skill_speed_data = {스킬명: [선시전시간, 후시전시간 ]} 
                        int(skill_start) + int(skill_speed_data['z'][1]/speed*100), 'z' ] )
        elif skill_name == 'surge 1' :
            skill_time_table.append([int(skill_start) - int(skill_speed_data['z'][0]/speed*100),  #skill_speed_data = {스킬명: [선시전시간, 후시전시간 ]} 
                        int(skill_start) + int(skill_speed_data['z'][1]/speed*100), 'z1' ] )  
        elif skill_name == 'surge 2' :
            skill_time_table.append([int(skill_start) - int(skill_speed_data['z'][0]/speed*100),  #skill_speed_data = {스킬명: [선시전시간, 후시전시간 ]} 
                        int(skill_start) + int(skill_speed_data['z'][1]/speed*100), 'z2' ] )  
        elif skill_name == 'surge 3' :
            skill_time_table.append([int(skill_start) - int(skill_speed_data['z'][0]/speed*100),  #skill_speed_data = {스킬명: [선시전시간, 후시전시간 ]} 
                        int(skill_start) + int(skill_speed_data['z'][1]/speed*100), 'z3' ] )  
        elif skill_name == 'Trance' :  
            for identity_start, identity_end in identity_table:
                if identity_start == int(skill_start):
                    skill_time_table.append([identity_start, identity_end, 'x'] )  #skill_speed_data = {스킬명: [선시전시간, 후시전시간 ]} 

        else:
            try:  # skill_speed_data 없는거 패스 ex) 텍스트로 된거
                if skill_name in rune_combo_table: #룬 공속 추가
                    add_speed += rune_speed[rune_combo_table[skill_name]]
                speed = default_speed + add_speed
                # 스킬 테이블 작성, 아이텐티티 때 시전시간이 변경되는 스킬 /  시전시간이 [선딜, 후딜, 아이텐티티선딜, 아이텐티티후딜]로 정의됨

                skill_time_table.append([int(skill_start) - int(skill_speed_data[skill_name][0]/speed*100),  #skill_speed_data = {스킬명: [선시전시간, 후시전시간 ]} 
                                    int(skill_start) + int(skill_speed_data[skill_name][1]/speed*100), skill_name ] )
            except:
                continue
    
    return skill_time_table