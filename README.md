# CSGO-winning-side-analysis
Counter Strike: Global Offensive is a first-person shooter video game in which two teams play as terrorists and counter-terrorists, respectively, and compete to blow up 
or defend an objective. Teams are five people per side, with players acquiring new weapons and items using points earned during the rounds in between rounds of play. 
Whichever team wins enough rounds, either by killing the entire enemy team or by successfully planting or defusing the bomb, wins the match.

Is there a side (terrorists or counter-terrorists) that has more chances to win the game ? If so, why ? That is what we are trying to figure out.

The original dataset named 'mm_master_demos' is available on kaggle at the following adress : 'https://www.kaggle.com/datasets/skihikingkevin/csgo-matchmaking-damage?select=mm_master_demos.csv'.
We don't need all the data in the dataset, so I decided to shape it into a smaller one that will be enough for or case study. You can find the latter dataset at 
the following adress : https://www.kaggle.com/datasets/sewawilson/csgo-data.

I added two columns that are not in the original dataset:
  - 'distance' which stores the distance between a shooter and the victim. It was calculated using the following formula : √((xB - xA)^2 + (yB - yA)^2), where x and y are
  two points on a orthonormal coordinate system. The measure is the same as on the original dataset, but we do not have the info on what it is.
  
  - 'att_eq_val' which stores the shooter's equipment value.
 
 Bellow you'll find the code used in order to create the 'csgo_data' dataframe from 'mm_master_demos'.
 
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
 
 
  
  
