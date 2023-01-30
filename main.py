import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import itertools
import matplotlib.patches as mpatches
from shaping import df

#Which team wins the most
df_t_wins = df[df['winner_side'] == 'Terrorist']
df_ct_wins = df[df['winner_side'] != 'Terrorist']
print(df_t_wins['round'].count()/df['round'].count(), df_ct_wins['round'].count()/df['round'].count())



#timelapse damage
# fig_1, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(10, 5))
# sns.kdeplot(df['hp_dmg'], ax=ax1)
# #Round spending average
# sns.kdeplot(df['att_eq_val'], ax=ax2)
# plt.show()

#Correlation
#sns.heatmap(df.corr(), vmin=-1, vmax=1,cmap=sns.diverging_palette(20, 220, as_cmap=True))
#
# # avg damage dealt/round depending on the side
# fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1)
# plot = df.groupby(["round", 'att_side'])['hp_dmg'].mean().reset_index()
# sns.lineplot(plot, x='round', y='hp_dmg', hue='att_side', ax=ax1)
# # The avg damage dealt seems to be more and more heterogen as the game goes on.
#
# #avg distance damage/round depending on the side
# plot_2 = df.groupby(["round", 'att_side'])['distance'].mean().reset_index()
# sns.lineplot(plot_2, x='round', y='distance', hue='att_side', ax=ax2)
#
# # # #Spending evolution through game  ?
# plot_3 = df.groupby(["round", 'att_side'])['att_eq_val'].mean().reset_index()
# sns.lineplot(df, x='round', y='att_eq_val', hue='att_side', ax=ax3)
#
# blue_patch = mpatches.Patch(color='blue', label='CT')
# red_patch = mpatches.Patch(color='orange', label='Terrorists')
# plt.legend(handles=[blue_patch, red_patch])

#spending one weapon
# df = df[df['round_type'] != 'PISTOL_ROUND']
# fg = sns.FacetGrid(data=df, col='wp_type', col_wrap=4, hue='att_side')
# fg.map(sns.kdeplot, 'att_eq_val')
# blue_patch = mpatches.Patch(color='blue', label='CT')
# red_patch = mpatches.Patch(color='orange', label='Terrorists')
# plt.legend(handles=[blue_patch, red_patch])









