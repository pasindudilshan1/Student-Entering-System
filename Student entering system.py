mport pandas as pd
try:
    df_read = pd.read_csv(r'C:\Users\pasindu\Documents\entering.CSV' , index_col=0)
    Student_Dtata = df_read.to_dict(orient='records')
except FileNotFoundError:
    Student_Dtata=[]
    student_id=0

while True:
    student_id+=1
   
   
    Name=input("Enter Student Name=  ")
    B_day=input("Birth day(yyyy/mmmm/dddd)=   ")
    Intake_Date=input("Enterring date(yyyy/mmmm/dddd)=  ")
    Age=int(input("Enter Student Age=  "))
    Gender=input("Enter Gender(MALE/FEMALE)=  ")
    M_name=input("Mothers name=   ")
    F_name=input("Father name=  ")
   
   

 
    Student_Dtata.append({'Stuent ID':student_id,'Name':Name,'BrithDay':B_day,'Intake_Date':Intake_Date, 'Gender': Gender, 'Age': Age,'Mother name':M_name,'Father name':F_name})
    another_record = input("Enter another record? (yes/no): ").strip().lower()
    if another_record != 'yes':
        break


df=pd.DataFrame(Student_Dtata)
df.to_csv(r'C:\Users\pasindu\Documents\entering.CSV' , index=False)

df_read = pd.read_csv(r'C:\Users\pasindu\Documents\entering.CSV' , index_col=0)

print(df_read)

