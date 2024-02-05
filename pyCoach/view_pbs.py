import sys
import pandas as pd
from pyCoach import is_pb

exercise = sys.argv[1]
pb_data_path = sys.argv[2]

pb_data = pd.read_csv(pb_data_path,index_col=False)
pb_data["date"]= pd.to_datetime(pb_data["date"])#,dayfirst=True)

pbs = pb_data.loc[pb_data.exercise == exercise]
latest_pbs = pd.DataFrame(columns=pbs.columns)

for i in range(len(pbs)-1,0,-1):
    effort = pbs.iloc[i]
    if is_pb(effort,latest_pbs):
        latest_pbs = pd.concat([latest_pbs,pd.DataFrame({
            "exercise":[effort.exercise],
            "amount_units":[effort.amount_units],
            "amount":[effort.amount],
            "date":[effort.date],
            "intensity_units":[effort.intensity_units],
            "intensity":[effort.intensity],
            "RPE":[effort.RPE],
            "notes":[effort.notes]
        })],ignore_index=True)
        
print(latest_pbs)