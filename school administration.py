import csv
def write_into_csv(info_list):
    with open('student_info.csv','a',newline='')as csv_file:
        writer= csv.writer(csv_file)
        
        if csv_file.tell()==0:
            writer.wrterow(["name","age","contact.no","email.id"])
            
        writer.writerow(info_list)
if __name__=='__main__':
    a=True
    student_num=1
while (a):
    student_info=input("enter student information in following format(Name Age Contact.no Email.id): ".format(student_num)
    
    student_info_list = student_info_.split(' ')
    print("\nEntered student information is :\nName{}\nAge{}\nContact.no{}\nEmail.id{}.format(stiudent_info_list[0]),student_info_list[1],student_info_list[2],student_info_list[3]))
          
    choice=input("is enetered info are correct?(yes/no): ")
    if choice =="yes":
        write_into_csv(student_info_list)
        
condition=input("enter (yes/no) if you want to add the other student information:")
        if condition=="yes":
    a=True
    student_num=student_num+1
        elif condition=="no":
    a=False
elif choice=="no":
    print("/n Please reenter the values")