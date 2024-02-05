import pandas as pd 
import re 

def log_session (session_path) :
    data = {
        "exercise":[],
        "amount_units":[],
        "amount":[],
        "intensity_units":[],
        "intensity":[],
        "date":[],
        "RPE":[],
        "notes":[]
    }
    p = r"\[(.*?)\]"
    with open(session_path,"r") as infile: 
        lines = infile.readlines() 
    session_date = (lines.pop(0).rstrip())[-10:]
    exercise_found = False
    for i,l in enumerate(lines): 

        if l.rstrip().replace(" ","") == "":
            exercise_found = False 
        else: 
            if not exercise_found:
                exercise_found = True
                amount = re.findall(p,lines[i+2])[0]
                if not amount == "":
                    data["date"].append(session_date)
                    data["exercise"].append(l.rstrip())
                    data["amount_units"].append(((lines[i+2].rstrip()).replace("    * ","")).split(" ")[0])
                    data["amount"].append(amount)
                    data["intensity_units"].append(((lines[i+3].rstrip()).replace("    * ","")).split(" ")[0])
                    data["intensity"].append(re.findall(p,lines[i+3])[0])
                    data["RPE"].append(re.findall(p,lines[i+4])[0])
                    data["notes"].append(re.findall(p,lines[i+5])[0])
                
    return data
if __name__ == "__main__":
    import sys 
    import os 
    
    session_path = sys.argv[1]
    session_log = sys.argv[2]
    
    session_data = log_session(session_path)
    
    if os.path.isfile(session_log):
        data = pd.read_csv(session_log,index_col=False)
    else:
        data = pd.DataFrame({
            "exercise":[],
            "amount_units":[],
            "amount":[],
            "intensity_units":[],
            "intensity":[],
            "date":[],
            "RPE":[],
            "notes":[]
        })      
        
    data = pd.concat([data,pd.DataFrame(session_data)])
    data.to_csv(session_log,index=False)
    
    