import pandas as pd
import matplotlib.pyplot as plt
from data import games

# select all plays
plays = games[games['type'] == 'play']

# select all strike outs
strike_outs = plays[plays['event'].str.contains('K')]

# group by year and game
strike_outs = strike_outs.groupby(['year', 'game_id']).size()

# reset index
strike_outs = strike_outs.reset_index(name='strike_outs')

# change values to numeric
strike_outs = strike_outs.loc[:, ['year', 'strike_outs']].apply(pd.to_numeric)

# create plot
strike_outs.plot(x='year', y='strike_outs', figsize=(15, 7), kind='scatter').legend(['Strike Outs'])
plt.show()
