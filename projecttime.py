import pandas as pd
import requests
import os
class TIMETABLE:
    def __init__(self,Excel,Sheet,Today):
        self.Excel=Excel
        self.Sheet=Sheet
        self.Today=Today
    def group(self):
        if self.Today=="SUNDAY":
            print("Today is a holiday.")
        else:
            sheet=self.Excel[self.Sheet]
            sheet = sheet.fillna("No Class")
            sheet["Day"] = sheet["Day"].str.strip().str.replace("\n", "", regex=True)
            subjects=sheet.loc[sheet["Day"]==self.Today[:3]]
            clean_cols=[
                col
                for col in subjects.columns
                if not str(col).startswith("Unnamed")
            ]
            subjects=subjects[clean_cols]
            print(subjects)
            return subjects.to_string(index=False)
excel=pd.read_excel(r"AIML-II-1- SEM TIME TABLE_ II year_17-07-2026 _final (1) (1) (2).xlsx",sheet_name=None,skiprows=6)
#grp=print("CivilEngineering\nEEE\nMechanical\nECE-(A,B,C,D,E,F,G)\nCSE-(A,B,C,D,E,F,G,H,I)\nIT-(A,B,C,D)\nCS\nAIML-(A,B,C,D,E)\nDS-(A,B,C)")
grp_input="AIML-B"
from datetime import datetime
now = datetime.now()
day= now.strftime("%A").upper()
get=TIMETABLE(excel,grp_input,day) 
output=get.group()
webhook_url=os.environ.get("DISCORD_WEBHOOK_URL")
if webhook_url:
    message=f"**Daily Timetable ({day})**\n```\n{output}\n```"
    requests.post(webhook_url,json={"content":message})
    
