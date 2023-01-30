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
 
You'll find the code used in order to create the 'csgo_data' dataframe from 'mm_master_demos' in the 'shaping.py' file.

  
  
