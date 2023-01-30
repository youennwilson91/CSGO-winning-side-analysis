# Introduction
Counter Strike: Global Offensive is a first-person shooter video game in which two teams play as terrorists and counter-terrorists, respectively, and compete to blow up 
or defend an objective. Teams are five people per side, with players acquiring new weapons and items using points earned during the rounds in between rounds of play. 
Whichever team wins enough rounds, either by killing the entire enemy team or by successfully planting or defusing the bomb, wins the match.

Is there a side (terrorists or counter-terrorists) that has more chances to win the game ? If so, why ? That is what we are trying to figure out.

The original dataset named 'mm_master_demos' is available on kaggle at the following adress : 'https://www.kaggle.com/datasets/skihikingkevin/csgo-matchmaking-damage?select=mm_master_demos.csv'.
We don't need all the data in the dataset, so I decided to shape it into a smaller one that will be enough for or case study. You can find the latter dataset at 
the following adress : https://www.kaggle.com/datasets/sewawilson/csgo-data.

I added two columns that are not in the original dataset:
  - '**distance**' which stores the distance between a shooter and the victim. It was calculated using the following formula : √((xB - xA)^2 + (yB - yA)^2), where x and y are
  two points on a orthonormal coordinate system. The measure is the same as on the original dataset, but we do not have the info on what it is.
  
  - '**att_eq_val**' which stores the shooter's equipment value.
 
You'll find the code used in order to create the 'csgo_data' dataframe from 'mm_master_demos' in the 'shaping.py' file.

  
 
# Side with most wins
Firstly, let's have a look at which side wins the most games:
```
input:

df_t_wins = df[df['winner_side'] == 'Terrorist']
df_ct_wins = df[df['winner_side'] != 'Terrorist']
print(df_t_wins['round'].count()/df['round'].count(), df_ct_wins['round'].count()/df['round'].count())
```
```
output:

0.5168186370996828 0.4831813629003172
```

We may see that the terrorist side have a slighlty higher winning rate. It could be due to multiple factors such as better players or better equipment.
  
# Average match rank
In CSGO, the player level is determined by his rank, whihc goes from 1 to 16. Let's see what is the average match rank when one of the side wins:
```
input:

print(df_t_wins['avg_match_rank'].mean(), df_ct_wins['avg_match_rank'].mean())
```
```
output:

11.190808700136706 11.207660129631616
```

We may say that the average match rank is the same either the terrorist or the counter-terrorist wins. 

# Correlation between HP damage and distance 
However, a player level is also determined by his skill.
The damage he inflicts depends on the weapon he has and the distance he shoots from. The best players logicaly inflicts the more damage. We may see that correlation
on the following heatmap:
```
input:

sns.heatmap(df.corr(), vmin=-1, vmax=1,cmap=sns.diverging_palette(20, 220, as_cmap=True))
plt.show()
```
```
output:
```
![heatmap](https://user-images.githubusercontent.com/117467104/215442650-b077fd9c-1810-4c3e-b35c-e44456a6e1f6.png)


Let's look at the damage dealt from both sides depending on the round and the team. Along side, we'll plot the distance between the shooter and the victim.
```
input:

# avg damage dealt/round depending on the side
fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1)
plot = df.groupby(["round", 'att_side'])['hp_dmg'].mean().reset_index()
sns.lineplot(plot, x='round', y='hp_dmg', hue='att_side', ax=ax1)
#
# avg distance damage/round depending on the side
plot_2 = df.groupby(["round", 'att_side'])['distance'].mean().reset_index()
sns.lineplot(plot_2, x='round', y='distance', hue='att_side', ax=ax2)
#
```
```
output:
```
![plots](https://user-images.githubusercontent.com/117467104/215444608-2bf40611-7795-4261-aa70-806c6d623c2c.png)

Interesting chart ! We may see that the terrorist deal much more damage than the counter-terrorists, as they seem to shoot from a closer range. Terrorist succeed to get closer from their enemy than counter-terrorists. This could imply that terrorsits prefer to play with close range quarter weapons such as knifes, pistols and SMGs.

# Spending tendency depending on each side
In order to evaluate the spending tendency on each side, we have to understand how the earning points system of the game works.
In CS:GO, each match consists of a certain number of rounds. The two teams start with the same number of points in the first round, and from there are provided additional points (dollars) at the beginning of each round: slightly more if the team won the previous round and slightly less if they lost.

These points make up the game's economy. Both teams must purchase weapons, armor, and consumables at the beginning of each round. The amount and quality of the equipment they can bring is limited by how many points they have available and are willing to spend.

There is a well-developed strategy to when and when not to spend points. On average, the better equipped the team, the better its chance of winning the round, but also the worse its cash reserves for future rounds. It's nevertheless obviously possible to beat a much better equipped team with worser weaponry, so sometimes (even often, in competitive games) teams will "bet" on a low equipment rollout and try to "steal" the round. Due to the way the game economy works, winning a round in this manner is highly cost-effective because it also sets your team up for winning future rounds.

Before looking at the spending habits on each weapon type for each side, let's have a look at the spending evolution through time.

```
# sns.lineplot(df, x='round', y='att_eq_val', hue='att_side')
#
# blue_patch = mpatches.Patch(color='blue', label='CT')
# red_patch = mpatches.Patch(color='orange', label='Terrorists')
# plt.legend(handles=[blue_patch, red_patch])
```
```
output:
```
![plot2](https://user-images.githubusercontent.com/117467104/215461071-d2794cdd-a085-49f6-a78d-c7731e582c0e.png)



Apparently, counter-terrorists tend to have a higher equipment value through the 15 first rounds. Then, the equipment value seems pretty much even for both teams. 
Even though counter-terrorists inflict less damage, they are the ones with the higher equipment value, which implies either the counter-terrorist get more wining rounds, or that the terrorist choose not to spend all their money on equipment. Since we saw that the terrorist have a slightly higher wining rate, the second hypothesis is more likely to be true instead of the first one.

Finally, let's have a look at the spending habits depending on the type of weapon.

Note that the first round of each half-time is called 'pistol-round' and players may buy pistols only. We'll filter out these rounds in order to avoid bias in our
analysis.
```
input:
df = df[df['round_type'] != 'PISTOL_ROUND']
fg = sns.FacetGrid(data=df, col='wp_type', col_wrap=4, hue='att_side')
fg.map(sns.kdeplot, 'att_eq_val')
blue_patch = mpatches.Patch(color='blue', label='CT')
red_patch = mpatches.Patch(color='orange', label='Terrorists')
plt.legend(handles=[blue_patch, red_patch])
plt.show()
```
```
output:
```
![plot3](https://user-images.githubusercontent.com/117467104/215450170-ddadecd3-c29d-4579-bdca-4eab4b2f785b.png)

We may see that terrorists spend more money on pistols and equipment, and end up spending money on higher value items for each category. This graph refutes the previously hyposthesis stating that terrorist spend more money on close range weapons. In fact, there are more counter terrorists buying SMG weapons than there are terrorists doing so. We can then say that the terrorists succeed to get close from their enemy in order to make more damage, but do not necesseraly play with closer range weapons.


# Conclusion
It seems that if the terrorists tend to have a slighlty higher wining rate due the to the level of their players. Terrorists do not have a higher rank or better weapons, but they seem to be more skilled and succeed to get closer to their enemy than the counter-terrorrists do, with less equipment value. This fact reflects their higher skill.

At the end of the day, if you are playing CSGO and you find yourself in the terrorist team, know that you are more likely to be on the winning side.









