import pandas as pd 
from pyCoach import load_session

def gen_session (session):
    session_plan = f"# {session.session_name.iloc[0]} {session.date.iloc[0]}\n\n"
    for i in range(len(session)):
        cur_set = session.iloc[i]
        set_description = f"\n{cur_set.exercise}\n{cur_set.instruction}"
        set_inputs = f"\n    * {cur_set.amount_units} []\n    * {cur_set.intensity_units} []\n    * RPE []"
        session_plan += set_description
        session_plan += set_inputs
        session_plan += "\n    * Notes: []\n"
    return session_plan

if __name__ == "__main__":
    import sys 
    import os 
    
    path = sys.argv[1]
    date = sys.argv[2]
    out_path = sys.argv[3]
    
    session = load_session(path,date) 
    session_plan = gen_session(session)
    
    with open(out_path,"w") as outfile: 
        outfile.write(session_plan)
    