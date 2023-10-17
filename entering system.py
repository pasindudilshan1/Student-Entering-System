import pandas as pd
try:
    df_read = pd.read_csv(r'C:\Users\pasindu\Documents\entering.CSV')
    Student_Dtata = df_read.to_dict(orient='records')
except FileNotFoundError:
    Student_Dtata=[]

while True:
    Do_You_Run=input("yes" " or ""no=  ").strip().lower()
    if Do_You_Run=="no":
        break

    Name=input("Enter Student Name=  ")
    Intake_Date=input("Enterring date(yyyy/mmmm/dddd)=  ")
    Age=int(input("Enter Student Age=  "))
    Gender=input("Enter Gender(MALE/FEMALE)=  ")

  
    Student_Dtata.append({'Name':Name,'Intake_Date':Intake_Date, 'Gender': Gender, 'Age': Age})
    another_record = input("Enter another record? (yes/no): ").strip().lower()
    if another_record != 'yes':
        break


df=pd.DataFrame(Student_Dtata)
df.to_csv(r'C:\Users\pasindu\Documents\entering.CSV' , index=False)

df_read = pd.read_csv(r'C:\Users\pasindu\Documents\entering.CSV')

print(df_read)