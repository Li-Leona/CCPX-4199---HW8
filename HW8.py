import pandas as pd

# navigate to the directory
data=pd.read_csv("https://raw.githubusercontent.com/CaitlinLloyd/Psychology_Programming2025/refs/heads/main/Data/DelayDisc_example.csv")
data  #choice =1 := left

# figure out whether left or right column is delayed (1 is left, 2 is right)
data['delayed_opt']= "none"
data.loc[data['delay_left'] < data['delay_right'],'delayed_opt'] =2
data.loc[data['delay_left'] > data['delay_right'],'delayed_opt'] =1
data

#check if chose delayed
data['delayed_opt_chose']= "none"
data.loc[data['delayed_opt'] == data['choice'],'delayed_opt_chose'] = 1
data.loc[data['delayed_opt'] != data['choice'],'delayed_opt_chose'] = 0
data

results = []  

for participant in sorted(data['participant'].unique()):

    sub_data = data[data['participant'] == participant].copy()

    sub_data = sub_data.dropna(subset=['choice'])

    sub_data.loc[sub_data['choice'] == 1, 'earning'] = sub_data['money_left']
    sub_data.loc[sub_data['choice'] == 2, 'earning'] = sub_data['money_right']

    average_earning = sub_data['earning'].mean()

    delayed_count = (sub_data['delayed_opt_chose'] == 1).sum()
    sooner_count = (sub_data['delayed_opt_chose'] == 0).sum()
    delayed_vs_sooner = delayed_count / sooner_count

    results.append({
        'participant': participant,
        'average_earning': average_earning,
        'delayed_count': delayed_count,
        'sooner_count': sooner_count,
        'delayed_vs_sooner': delayed_vs_sooner
    })

summary_df = pd.DataFrame(results)

print(summary_df)