import pandas as pd
import numpy as np


df = pd.read_csv('isl_player_final.csv')
df.columns
df = df[['name', 'team_name', 'position', 'position_short', 'dob', 'events.goals', 'events.assists',
         'events.chances_created', 'events.goals_conceded', 'events.clean_sheet', 'events.penalties_saved',
         'events.blocked_shots',
         'touches.tackles', 'touches.blocks', 'touches.successful_tackles', 'overall']]

df.head(11)
df['position'] = df['position'].str.split().str[0]


def get_best_squad(position):
    df_copy = df.copy()
    store = []
    for i in position:
        store.append([i,
                      df_copy.loc[[df_copy[df_copy['position'] == i]['overall'].idxmax()]]['name'].to_string(
                          index=False), df_copy[df_copy['position'] == i]['overall'].max()])
        df_copy.drop(df_copy[df_copy['position'] == i]['overall'].idxmax(), inplace=True)
    return pd.DataFrame(np.array(store).reshape(11, 3), columns=['position', 'name', 'overall']).to_string(
        index=False)


squad_433 = ['Forward', 'Forward', 'Forward', 'Midfielder', 'Midfielder', 'Midfielder', 'Midfielder', 'Defender',
             'Defender',
             'Defender', 'Goalkeeper']
print('3-4-3')
print(get_best_squad(squad_433))
