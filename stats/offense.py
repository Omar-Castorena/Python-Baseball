import pandas as pd
import matplotlib.pyplot as plt
from data import games

# select all plays
plays = games[games['type'] == 'play']
plays.columns = ['type', 'inning', 'team', 'player', 'count', 'pitches', 'event', 'game_id', 'year']

# select only hits
hits = plays.loc[plays['event'].str.contains('^(?:S(?!B)|D|T|HR)'), ['inning', 'event']]

# convert to numeric
hits.loc[:, 'inning'] = pd.to_numeric(hits.loc[:, 'inning'])

# replace dictionary
replacements = {r'^S(.*)': 'single', r'^D(.*)': 'double', r'^T(.*)': 'triple', r'^HR(.*)': 'hr'}

#r eplace function
hit_type = hits['event'].replace(replacements, regex=True)

# add a new column
hits = hits.assign(hit_type=hit_type)

# group by inning and hit type
hits = hits.groupby(['inning', 'hit_type']).size().reset_index(name='count')

# convert hit type to categorical
hits['hit_type'] = pd.Categorical(hits['hit_type'], ['single', 'double', 'triple', 'hr'])

# sort values
hits = hits.sort_values(['inning', 'hit_type'])

# reshape with pivot
hits = hits.pivot(index='inning', columns='hit_type', values='count')

# stacked bar plot
hits.plot.bar(stacked=True)
plt.show()