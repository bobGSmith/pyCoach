import pandas as pd

def is_pb (effort,pb_data,exclude_circuits=True):
    if effort.amount_units == "circuits":
        return False
    pbs = pb_data.loc[pb_data.exercise == effort.exercise]
    pbs = pbs.loc[pbs.amount >= effort.amount]
    if len(pbs) == 0:
        return True
    range_pb = pbs.intensity.max()
    return effort.intensity > range_pb 

if __name__ == "__main__":

    import sys
    session_data_path = sys.argv[1]
    pb_data_path = sys.argv[2]
    
    # Load data    
    session_data = pd.read_csv(session_data_path,index_col=False)
    session_data["date"] = pd.to_datetime(session_data["date"],dayfirst=True)

    pb_data = pd.read_csv(pb_data_path,index_col=False)
    pb_data["date"]= pd.to_datetime(pb_data["date"])#,dayfirst=True)

    # Crop to relevant session data 
    session_data = session_data.loc[session_data.date > pb_data.date.max()]
    
    for i in range(len(session_data)):
        effort = session_data.iloc[i]
        if is_pb(effort,pb_data):
            print("PB found")
            print(f"Exercise: {effort.exercise} - {effort.amount} {effort.amount_units} @ {effort.intensity} {effort.intensity_units}")
            pb_data = pd.concat([pb_data,pd.DataFrame({
                "exercise":[effort.exercise],
                "amount_units":[effort.amount_units],
                "amount":[effort.amount],
                "date":[effort.date],
                "intensity_units":[effort.intensity_units],
                "intensity":[effort.intensity],
                "RPE":[effort.RPE],
                "notes":[effort.notes]
            })])
            
    pb_data.to_csv(pb_data_path,index=False)

