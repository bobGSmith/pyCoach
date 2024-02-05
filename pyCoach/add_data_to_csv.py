import pandas as pd 
import os 

def add_data_to_csv (new_data,path):
    if os.path.isfile(path):
        data = pd.read_csv(path,index_col=False)
    else:
        data = {col:[] for col in new_data.keys()}
        data = pd.DataFrame(data)      
        
    data = pd.concat([data,pd.DataFrame(new_data)])
    data.to_csv(path,index=False)
    
    