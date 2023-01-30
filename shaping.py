import pandas as pd
from math import sqrt

map_data = pd.read_csv('map_data.csv')
master_data = pd.read_csv('mm_master_demos.csv')
master_data = master_data[master_data['att_side'] != 'None']
master_data = master_data[master_data['wp_type'] != 'Unkown']
master_data['att_vic_x'] = abs(master_data['att_pos_x'] - master_data['vic_pos_x'])
master_data['att_vic_y'] = abs(master_data['att_pos_y'] - master_data['vic_pos_y'])
distance = []
for k, n in zip(master_data['att_vic_x'], master_data['att_vic_y']):
    a = sqrt(k**2 + n**2)
    distance.append(a)


master_data['distance'] = distance

df = pd.DataFrame().assign(round=master_data['round'], distance=master_data['distance'], att_side=master_data['att_side'],
                         hp_dmg=master_data['hp_dmg'], wp_type=master_data['wp_type'], seconds=master_data['seconds'],
                            round_type=master_data['round_type'], winner_side=master_data['winner_side'])

att_eq_val = []
for x, y, z in zip(master_data['att_side'], master_data['t_eq_val'], master_data['ct_eq_val']):
    if x == 'Terrorist':
        att_eq_val.append(y)
    else:
        att_eq_val.append(z)
df['att_eq_val'] = att_eq_val
