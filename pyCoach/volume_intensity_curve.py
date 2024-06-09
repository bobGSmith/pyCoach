import matplotlib.pyplot as plt 
import pandas as  pd 


def get_volume_intensity_curve (exercise,pb_data):
    exercise_pbs = pb_data.loc[pb_data.exercise == exercise]
    unique_amounts = exercise_pbs.amount.unique() 
    volume_intensity_curve = pd.DataFrame(columns = pb_data.columns) 
    for amount in unique_amounts:
        cur =  exercise_pbs.loc[exercise_pbs.amount == amount]
        cur_max = cur.loc[cur.intensity == cur.intensity.max()]
        volume_intensity_curve = pd.concat([volume_intensity_curve,cur_max])
    return volume_intensity_curve

def plot_volume_intensity_curve (volume_intensity_curve):
    amount_units = volume_intensity_curve.amount_units.iloc[0]
    intensity_units = volume_intensity_curve.intensity_units.iloc[0]
    sorted_df = volume_intensity_curve.sort_values(by=["amount"])
    plt.plot(sorted_df.amount.values,sorted_df.intensity.values)
    plt.xlabel(amount_units)
    plt.ylabel(intensity_units)
    plt.title(f"{volume_intensity_curve.exercise.iloc[0]} volume-intensity curve")
    plt.show()    

if __name__ == "__main__": 
    import sys
    
    exercise = sys.argv[1]
    pb_data_path = sys.argv[2]
    
    pb_data = pd.read_csv(pb_data_path,index_col=False)
    pb_data["date"]= pd.to_datetime(pb_data["date"],format="mixed")
    
    volume_intensity_curve = get_volume_intensity_curve(exercise,pb_data)
    print(volume_intensity_curve.head())
    plot_volume_intensity_curve(volume_intensity_curve)