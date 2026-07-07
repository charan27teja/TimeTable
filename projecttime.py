import pandas as pd
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
            subjects=sheet.loc[sheet["Day"]==self.Today]
            print(subjects)
excel=pd.read_excel(r"C:\Users\sai\OneDrive\Documents\R1 I B.Tech-II Sem Time Table 2025-26.xlsx",sheet_name=None,skiprows=4)
grp=print("CivilEngineering\nEEE\nMechanical\nECE-(A,B,C,D,E,F,G)\nCSE-(A,B,C,D,E,F,G,H,I)\nIT-(A,B,C,D)\nCS\nAIML-(A,B,C,D,E)\nDS-(A,B,C)")
grp_input=input("Enter your group: ").upper()
from datetime import datetime
now = datetime.now()
day= now.strftime("%A").upper()
get=TIMETABLE(excel,grp_input,day) 
get.group()
