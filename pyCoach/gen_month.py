if __name__ == "__main__":
    import sys
    from pandas import to_datetime    
    from datetime import timedelta 
    
    with open(sys.argv[1]) as infile:     
        s1 = []
        s2 = []
        
        processing_s1 = True
        for l in infile.readlines():
            if processing_s1:
                if l[0] == "#" and l[6] == "2":
                    processing_s1 = False
                    s2.append(l)
                else:
                    s1.append(l)
            else:
                s2.append(l)  
                
    s1_date_start = to_datetime(s1[0][8:].rstrip(),dayfirst=True,format="mixed")
    s2_date_start = to_datetime(s2[0][8:].rstrip(),dayfirst=True,format="mixed")
        
    full_month = []
    for i in range(4): 
        s1_title = f"# m{i+1} s1 {(s1_date_start + timedelta(days = 7 * i)).date().strftime('%d/%m/%Y')}"
        s2_title = f"# m{i+1} s2 {(s2_date_start + timedelta(days = 7 * i)).date().strftime('%d/%m/%Y')}"
        full_month += [s1_title,"\n"] + s1[1:] + ["\n"]
        full_month += [s2_title,"\n"] + s2[1:] + ["\n"]
        
    with open(sys.argv[2],"w") as outfile:
        outfile.writelines(full_month)    
