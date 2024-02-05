import pandas as pd 

def load_session (path, date) :
    data = pd.read_csv(path,index_col=False)
    return data[data.date == date]