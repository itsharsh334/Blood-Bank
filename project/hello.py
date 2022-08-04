from datetime import date, datetime
from tkinter import *
import tkinter.messagebox as MessageBox
from turtle import color
import mysql.connector as mysql
from tkinter import *
from PIL import ImageTk,Image
from mysqlx import Column
from tkcalendar import *
root=Tk()
root.title('BLOOD BANK') 
root.iconbitmap('images.ico')
root.geometry("500x200")
bg = ImageTk.PhotoImage(file="bb.jpg")
# Create a canvas
my_canvas = Canvas(root, width=500, height=200)
my_canvas.pack(fill="both", expand=True)
# Set image in canvas
my_canvas.create_image(0,0, image=bg, anchor="nw")
# Add a label
my_canvas.create_text(50,20,text="HS BLOOD BANK", font=("Helvetica", 20), fill="white")
#root.configure(bg="#249C13")
# Drop Down Boxes 
def date_selected():
    global date_picked
    date_picked=cal.get_date()
    pick.destroy()
def grab_date():
    global pick
    pick=Toplevel()
    pick.title('BLOOD BANK') 
    pick.iconbitmap('images.ico')
    pick.geometry("300x300")
    choose=Label(pick,text="Select a date",font=('bold',10),bg="white",fg="green")
    choose.pack(pady=(0,5))
    global cal
    cal = Calendar(pick, selectmode="day", year=2022, month=5, day=22,date_pattern="yyyy-mm-dd")
    cal.pack(pady=10,fill="both",expand=True)
    done=Button(pick,text="OK",bg="white",command=date_selected)
    done.pack(pady=10)
def resizer(e):
    global bg1, resized_bg, new_bg
    # Open our image
    bg1 = Image.open("bb.jpg")
    # Resize the image
    resized_bg = bg1.resize((e.width, e.height), Image.ANTIALIAS)
    # Define our image again
    new_bg = ImageTk.PhotoImage(resized_bg)
    # Add it back to the canvas
    my_canvas.create_image(0,0, image=new_bg, anchor="nw")
    my_canvas.create_text(200,20,text="HS BLOOD BANK", font=("Helvetica", 20), fill="white")
def update():
    name_p=e_name.get()
    bmi=e_bmi.get()
    phone=e_phone.get()
    hg_count=e_hg_count.get()
    blood=bloodt.get()
    city=cityt.get()
    di=MessageBox.askyesno("Disease","Are you suffering from Cancer,cardiac disease,hepatitis,HIV or have you suffered from acute fever,flu or had a surgery in past month?")
    if(di==True):
        disease=1
    elif(di==False):
        disease=0
     
     
    #ENTER PASSWORD HERE    
    con=mysql.connect(host="localhost",user="root",password="Sherlock@tbbt_got",database="blood_bank") #ENTER PASSWORD HERE 
    
    
    c=con.cursor()
    c.execute(f"UPDATE person SET name_p ='{name_p}',city ='{city}',BMI ='{bmi}',phone ='{phone}',disease='{disease}',hg_count ='{hg_count}',blood_type ='{blood}' WHERE aadhar ='{str(aadhar)}'")
    c.execute("commit");
    MessageBox.showinfo("Update Status","Request Updated successfully")
    up.destroy()

    return
def edit():
    global aadhar
    aadhar=e_id.get()
    print(f"\n{aadhar}\n")
    global up
    up=Toplevel()
    up.title('BLOOD BANK')
    up.iconbitmap('images.ico')
    up.geometry("600x600")
    up.configure(bg="#249C13")
    
    
    #ENTER PASSWORD HERE 
    con=mysql.connect(host="localhost",user="root",password="Sherlock@tbbt_got",database="blood_bank") #ENTER PASSWORD HERE 
    
    
    c=con.cursor()
    c.execute("SELECT * FROM person")
    records=c.fetchall()
    flag=0
    for record in records:
        if(aadhar==record[0]):
            flag=1
            myLabel = Label(up, text=(clicked.get()).upper())
            myLabel.grid(column=0,row=0,columnspan=2,pady=5)
            id=Label(up,text="Aadhar ID:- "+aadhar,font=('bold',10),bg="white",fg="green")
            id.grid(row=1,column=0,pady=5)
            name=Label(up,text="Name:- ",font=('bold',10),bg="white",fg="green")
            name.grid(row=2,column=0,pady=5)
            blood=Label(up,text="Blood Type",font=('bold',10),bg="white",fg="green")
            blood.grid(row=3,column=0,pady=5)
            city=Label(up,text="City/Branch",font=('bold',10),bg="white",fg="green")
            city.grid(row=4,column=0,pady=5)
            bmi=Label(up,text="BMI:- ",font=('bold',10),bg="white",fg="green")
            bmi.grid(row=5,column=0,pady=5)
            phone=Label(up,text="Phone number",font=('bold',10),bg="white",fg="green")
            phone.grid(row=6,column=0,pady=5)
            hg_count=Label(up,text="haemoglobin count ",font=('bold',10),bg="white",fg="green")
            hg_count.grid(row=7,column=0,pady=5)
            # e_id=Entry(top)
            # e_id.insert(0,record[0])
            # e_id.grid(row=1,column=1,pady=5)
            global e_name
            global e_address
            global e_blood
            global e_height
            global e_weight
            global e_phone
            global e_hg_count
            e_name=Entry(up)
            e_name.insert(0,record[1])
            e_name.grid(row=2,column=1,pady=5)
            blood_chart = [
                                "A+", 
                                "B+", 
                                "A-", 
                                "B-",
                                "AB+", 
                                "AB-",
                                "O+",
                                "O-"
                            ]	
            global bloodt
            index=blood_chart.index(record[7])
            bloodt = StringVar()
            bloodt.set(blood_chart[index])
            global droped
            droped = OptionMenu(up, bloodt, *blood_chart)
            droped.grid(row=3,column=1,pady=5)
            
            
            #ENTER PASSWORD HERE 
            con=mysql.connect(host="localhost",user="root",password="Sherlock@tbbt_got",database="blood_bank") #ENTER PASSWORD HERE 
            
            
            c=con.cursor()
            c.execute("SELECT city as city FROM branch")
            branches=c.fetchall() 
            global branch
            branch=[""]
            branch.clear()
            for branche in branches:
                branch.append(branche[0])
            global cityt
            ind=branch.index(record[2])
            cityt= StringVar()
            cityt.set(branch[ind])
            global drops
            drops = OptionMenu(up, cityt, *branch)
            drops.grid(row=4,column=1,pady=5)
            global e_bmi
            e_bmi=Entry(up)
            e_bmi.insert(0,record[3])
            e_bmi.grid(row=5,column=1,pady=5)
            e_phone=Entry(up)
            e_phone.insert(0,record[4])
            e_phone.grid(row=6,column=1,pady=5)
            e_hg_count=Entry(up)
            e_hg_count.insert(0,record[6])
            e_hg_count.grid(row=7,column=1,pady=5)
            updateb=Button(up,text="Update Record",bg="white",command=update)
            updateb.grid(row=8,column=0,columnspan=2,pady=10)

    if(flag==0):
        MessageBox.showerror("Update Status","No Such person exists")
    top.destroy()
    return
def insertR():
    di=MessageBox.askyesno("Disease","Are you suffering from Cancer,cardiac disease,hepatitis,HIV or have you suffered from acute fever,flu or had a surgery in past month?")
    id=e_id.get()
    if(di==True):
        disease=1
    elif(di==False):
        disease=0
    name=e_name.get()
    address=e_address.get()
    blood=bloodt.get()
    city=cityt.get()
    phone=e_phone.get()
    height=e_height.get()
    weight=e_weight.get()
    # bmi=weight/(height*height)
    hg_count=e_hg_count.get()
    if(id.strip()==""or name.strip()=="" or address.strip()=="" or blood.strip()=="" or city.strip()=="" or height.strip=="" or weight.strip=="" or hg_count.strip()=="" or phone.strip()==""):
        MessageBox.showerror("Insert Status","All field are required")
    else:
        height=float(height)/100
        weight=float(weight)
        bmi=weight/(height*height)
        # hg_count=float(hg_count)
        
        
        #ENTER PASSWORD HERE 
        con=mysql.connect(host="localhost",user="root",password="Sherlock@tbbt_got",database="blood_bank") #ENTER PASSWORD HERE 
        
        
        c=con.cursor()
        c.execute("SELECT * FROM person")
        records=c.fetchall()
        flag=0
        for record in records:
            if(record[0]==id):
                flag=1
                break
        if(flag==1):
            MessageBox.showerror("Insert Status","Record already exists, Please update it")
        else:
            c.execute("insert into person values ('"+id+"','"+name+"','"+city+"','"+str(bmi)+"','"+phone+"','"+str(disease)+"','"+hg_count+"','"+blood+"')")
            c.execute("commit");
            MessageBox.showinfo("Insert Status","Insertion Successful")
        con.close();
        top.destroy()
    return 
def request():
    id=e_id.get()
    amount=e_amount.get()
    
    
    #ENTER PASSWORD HERE 
    con=mysql.connect(host="localhost",user="root",password="Sherlock@tbbt_got",database="blood_bank") #ENTER PASSWORD HERE 
    
    
    c=con.cursor()
    c.execute("SELECT * FROM person")
    records=c.fetchall()
    flag=0
    for record in records:
        if(record[0]==id):
            flag=1
            report_id=str(id)+str(date_picked)      
            city=record[2]
            blood=record[7]
            bmi=float(record[3])
            hg_count=float(record[6])
            disease=int(record[5])
            print(f"\ng{blood}g\n")
            if(blood=="A-" or blood=="B-"):
                c.execute("SELECT * FROM donor as d, person as p  where (d.blood_type='"+blood+"' or d.blood_type='O-') AND p.city='"+city+"' and d.D_ID=p.aadhar order by date1")
                chords=c.fetchall()
            elif(blood=="O-"):
                c.execute("SELECT * FROM donor as d, person as p  where d.blood_type='O-' AND p.city='"+city+"' and d.D_ID=p.aadhar order by date1")
                chords=c.fetchall()
            elif(blood=="O+"):
                c.execute("SELECT * FROM donor as d, person as p  where (d.blood_type='O-' or d.blood_type='O+') AND p.city='"+city+"' and d.D_ID=p.aadhar order by date1")
                chords=c.fetchall()
            elif(blood=="AB+"):
                c.execute("SELECT * FROM donor as d, person as p where p.city='"+city+"' and d.D_ID=p.aadhar order by date1")
                chords=c.fetchall()
            elif(blood=="AB-"):
                c.execute("SELECT * FROM donor as d, person as p  where (d.blood_type='O-' or d.blood_type='B-' or d.blood_type='A-' or d.blood_type='AB-') AND p.city='"+city+"' and d.D_ID=p.aadhar order by date1")
                chords=c.fetchall()
            elif(blood=="A+"):
                print("\ncheck1\n")
                c.execute("SELECT * FROM donor as d, person as p  where (d.blood_type='O-' or d.blood_type='O+' or d.blood_type='A-' or d.blood_type='A+') AND p.city='"+city+"' and d.D_ID=p.aadhar order by date1")
                chords=c.fetchall()
            elif(blood=="B+"):
                c.execute("SELECT * FROM donor as d, person as p  where (d.blood_type='O-' or d.blood_type='O+' or d.blood_type='B-' or d.blood_type='B+') AND p.city='"+city+"' and d.D_ID=p.aadhar order by date1")
                chords=c.fetchall()
            if (len(chords)==0):
                c.execute("INSERT INTO receiver values ('"+id+"','"+city+"','"+str(amount)+"','"+blood+"','"+str(date_picked)+"')")
                MessageBox.showerror("Request Status","Blood Not Currently Available in this city, Request applied Successfully")

            else:
                sum_blood=0
                i=0
                for chord in chords:
                    sum_blood+=int(chord[2])
                    print(f"{chord[2]}")
                print(f"\n{sum_blood} {amount}\n")
                if(sum_blood>=int(amount)):
                    temp=int(amount)
                    c.execute("SELECT * FROM report")
                    lites=c.fetchall()
                    flag2=0
                    for lite in lites:
                        if(lite[0]==report_id):
                            flag2=1
                    if(flag2==0):
                        c.execute("INSERT INTO report VALUES ('"+report_id+"','"+id+"','"+date_picked+"','"+str(amount)+"','"+blood+"')")
                    for chord in chords:
                        if(temp<int(chord[2])):
                            new_amount=chord[2]-temp
                            c.execute("UPDATE donor SET amount='"+str(new_amount)+"' where D_ID='"+str(chord[0])+"' AND date1='"+str(chord[4])+"'")
                            c.execute("INSERT INTO receiver_donor values ('"+report_id+"','"+str(chord[0])+"','"+str(temp)+"','"+chord[3]+"')")         
                            # c.execute("commit");
                            MessageBox.showinfo("Request status","Blood available, Transfusion successful")
                            break
                        elif(temp==0):
                            MessageBox.showinfo("Request status","Blood available, Transfusion successful")
                            break
                        else:
                            temp=temp-chord[2]
                            c.execute("DELETE FROM donor where D_ID='"+chord[0]+"' AND date1='"+str(chord[4])+"'")
                            c.execute("INSERT INTO receiver_donor values ('"+report_id+"','"+str(chord[0])+"','"+str(chord[2])+"','"+chord[3]+"')")
                            # c.execute("commit");
                elif(sum_blood==0):
                    MessageBox.showerror("Request Status","Sorry No blood available in this city")
                else:
                    t=MessageBox.askyesno("Request Status","Only "+str(sum_blood)+" is available, Do you want to proceed or not? ")
                    if(t==1):
                        #delete initial records and generate report
                        c.execute("SELECT * FROM report")
                        lites=c.fetchall()
                        flag2=0
                        for lite in lites:
                            if(lite[0]==report_id):
                                flag2=1
                        if(flag2==0):
                            c.execute("INSERT INTO report VALUES ('"+report_id+"','"+id+"','"+str(date_picked)+"','"+str(sum_blood)+"','"+blood+"')")
                        s=MessageBox.askyesno("Request Status","Only "+str(sum_blood)+" is available, Do you want to apply request for later for rest of the blood? ")
                        for chord in chords:
                            c.execute("INSERT INTO receiver_donor values ('"+report_id+"','"+str(chord[0])+"','"+str(chord[2])+"')")
                            # c.execute("commit");
                            MessageBox.showinfo("Request Status","Request applied Successfully")
                        if(s==1):
                            amount=int(amount)-int(sum_blood)
                            c.execute("INSERT INTO receiver values ('"+id+"','"+city+"','"+str(amount)+"','"+blood+"','"+str(date_picked)+"')")
                            # c.execute("commit");
            break
    if(flag==0):
        MessageBox.showerror("Request Status","Person not found in database, Please register first")
    c.execute("commit")    
    con.close();
    top.destroy()
    return
def donation():
    id=e_id.get()
    amount=e_amount.get()
    
    
    #ENTER PASSWORD HERE 
    con=mysql.connect(host="localhost",user="root",password="Sherlock@tbbt_got",database="blood_bank") #ENTER PASSWORD HERE 
    
    
    c=con.cursor()
    c.execute("SELECT * FROM person")
    records=c.fetchall()
    flag=0
    for record in records:
        if(record[0]==id):
            flag=1
            name=record[2]
            blood=record[7]
            bmi=float(record[3])
            hg_count=float(record[6])
            disease=int(record[5])
            if(bmi<18):
                MessageBox.showwarning("Donation Status","BMI too low for donation")
                break
            elif(hg_count<12.5):
                MessageBox.showwarning("Donation Status","Haemoglobin too low for donation")    
                break
            elif(disease==1):
                MessageBox.showwarning("Donation Status","Suffering from Disease that prevents donation")
                break
            else:
                #date
                c.execute("INSERT INTO donor values ('"+id+"','"+name+"','"+amount+"','"+blood+"','"+date_picked+"')")
                rep_id=str(id)+str(date_picked)
                c.execute(f"INSERT INTO donor_report values ('{rep_id}','{id}','{date_picked}','{amount}','{blood}')")
                if(blood == 'A+'):
                    c.execute("SELECT * FROM receiver WHERE (receiver.blood_type = 'A+' OR receiver.blood_type = 'AB+') AND receiver.name_r = '"+name+"'")
                elif(blood == 'B+'):
                    c.execute("SELECT * FROM receiver WHERE (receiver.blood_type = 'B+' OR receiver.blood_type = 'AB+') AND receiver.name_r = '"+name+"'")
                elif(blood == 'A-'):
                    c.execute("SELECT * FROM receiver WHERE (receiver.blood_type = 'A-' OR receiver.blood_type = 'AB-') AND receiver.name_r = '"+name+"'")
                elif(blood == 'B-'):
                    c.execute("SELECT * FROM receiver WHERE (receiver.blood_type = 'B-' OR receiver.blood_type = 'AB-') AND receiver.name_r = '"+name+"'")
                elif(blood == 'O+'):
                    c.execute("SELECT * FROM receiver WHERE (receiver.blood_type = 'O+' OR receiver.blood_type = 'A+' OR receiver.blood_type = 'B+' OR receiver.blood_type = 'AB+') AND receiver.name_r = '"+name+"'")
                elif(blood == 'O-'):
                    c.execute("SELECT * FROM receiver WHERE (receiver.blood_type = 'O+' OR receiver.blood_type = 'A+' OR receiver.blood_type = 'B+' OR receiver.blood_type = 'AB+' OR receiver.blood_type = 'O-' OR receiver.blood_type = 'A-' OR receiver.blood_type = 'B-' OR receiver.blood_type = 'AB-') AND receiver.name_r = '"+name+"'")
                elif(blood == 'AB+'):
                    c.execute("SELECT * FROM receiver WHERE (receiver.blood_type = 'AB+') AND receiver.name_r = '"+name+"'")
                else:
                    c.execute("SELECT * FROM receiver WHERE (receiver.blood_type = 'A-' OR receiver.blood_type = 'O-' OR receiver.blood_type = 'B-' OR receiver.blood_type = 'AB-') AND receiver.name_r = '"+name+"'")
                hits = c.fetchall()
                flag_1 = 0
                if(len(hits) == 0):
                    flag_1 = 1
                if(flag_1==0):
                    for hit in hits:
                        if(int(amount)==0):
                            break
                        elif(hit[2]>int(amount)):
                            r_id = hit[0]
                            report_id = r_id + str(date_picked)
                            left = hit[2]
                            left = left - int(amount)
                            c.execute("SELECT * FROM report")
                            lites=c.fetchall()
                            flag2=0
                            for lite in lites:
                                if(lite[0]==report_id):
                                    flag2=1
                            if(flag2==0):
                                c.execute("INSERT INTO report values ('"+report_id+"','"+r_id+"','"+date_picked+"','"+amount+"','"+blood+"')")
                            c.execute("INSERT INTO receiver_donor values ('"+report_id+"','"+id+"','"+str(amount)+"','"+str(hit[3])+"')")
                            c.execute("DELETE FROM donor WHERE D_ID ='"+id+"'")
                            c.execute("UPDATE receiver SET amount ='"+str(left)+"' WHERE R_ID='"+r_id+"' and date1='"+hit[4]+"'")
                            break
                        elif(hit[2] <= int(amount)):
                            r_id = hit[0]
                            report_id = r_id + str(date_picked)
                            amount_left = int(amount) - hit[2]
                            c.execute("SELECT * FROM report")
                            lites=c.fetchall()
                            flag2=0
                            for lite in lites:
                                if(lite[0]==report_id):
                                    flag2=1
                            if(flag2==0):
                                c.execute("INSERT INTO report values ('"+report_id+"','"+r_id+"','"+date_picked+"','"+str(hit[2])+"','"+str(hit[3])+"')")
                            c.execute("INSERT INTO receiver_donor values ('"+report_id+"','"+id+"','"+str(hit[2])+"','"+blood+"')")
                            #Delete the receiver
                            c.execute("DELETE FROM receiver WHERE R_ID='"+r_id+"' and date1='"+str(hit[4])+"'")
                            #Reduce the value of blood left
                            c.execute("UPDATE donor SET amount ='"+str(amount_left)+"' WHERE D_ID='"+id+"' and date1='"+str(date_picked)+"'" )
                            amount=str(int(amount)-hit[2])
                
                MessageBox.showinfo("Donation Status","Donation Successful")
                break
    if(flag==0):
        print("\nno blood\n")
        MessageBox.showerror("Donation Status","Person not found in database, Please register first")
    c.execute("commit");
    con.close();
    top.destroy()
    return
def exitRepShow():
    repshow.destroy()
    return
def delet():
    aadhar=e_id.get()
    
    
    #ENTER PASSWORD HERE 
    con=mysql.connect(host="localhost",user="root",password="Sherlock@tbbt_got",database="blood_bank") #ENTER PASSWORD HERE 
    
    
    c=con.cursor()
    c.execute("Delete from person where aadhar ='"+aadhar+"'")
    c.execute("commit");
    MessageBox.showinfo("Deletion status","Record Succesfully deleted")
    top.destroy()
    return
def report_donate():
    global rep
    rep=e_id.get()+str(date_picked)
    
    
    #ENTER PASSWORD HERE 
    con=mysql.connect(host="localhost",user="root",password="Sherlock@tbbt_got",database="blood_bank") #ENTER PASSWORD HERE 
    
    
    c=con.cursor()
    c.execute("SELECT * FROM donor_report")
    records=c.fetchall()
    flag=0
    for record in records:
        if(record[0]==rep):
            flag=1
            d_id=record[1]
            date1=record[2]
            amount_r=record[3]
            blood=record[4]
            global repshow
            repshow=Toplevel()
            repshow.title('BLOOD BANK report')
            repshow.iconbitmap('images.ico')
            repshow.geometry("500x700")
            # repshow.configure(bg="#EF4EDB")
            c.execute("SELECT * FROM person WHERE aadhar='"+d_id+"'")
            name=c.fetchone()
            global nam
            global city
            nam=name[1]
            city=name[2]
            l_bb=Label(repshow,text="HS BLOOD BANK",font=('bold',30),bg="white",fg="green")
            l_bb.grid(row=0,column=0,sticky=W+E,columnspan=3)
            r_name="Name: "+nam
            l_name=Label(repshow,text=r_name,font=('bold',10),bg="white",fg="green")
            l_name.grid(row=1,column=0,pady=10,columnspan=3)
            r_rep="Report ID: "+rep
            l_rep=Label(repshow,text=r_rep,font=('bold',10),bg="white",fg="green")
            l_rep.grid(row=2,column=0,pady=10,columnspan=3)
            r_rid="Donor ID: "+d_id
            l_rid=Label(repshow,text=r_rid,font=('bold',10),bg="white",fg="green")
            l_rid.grid(row=3,column=0,pady=10,columnspan=3)
            r_date="Date of Donation: "+str(date1)
            l_date=Label(repshow,text=r_date,font=('bold',10),bg="white",fg="green")
            l_date.grid(row=4,column=0,pady=10,columnspan=3)
            r_amount="Amount of blood : "+str(amount_r)
            l_amount=Label(repshow,text=r_amount,font=('bold',10),bg="white",fg="green")
            l_amount.grid(row=5,column=0,pady=10,columnspan=3)
            r_blood="Blood type: "+blood
            l_blood=Label(repshow,text=r_blood,font=('bold',10),bg="white",fg="green")
            l_blood.grid(row=6,column=0,pady=10,columnspan=3)
            r_city="City/Branch: "+city
            l_city=Label(repshow,text=r_city,font=('bold',10),bg="white",fg="green")
            l_city.grid(row=7,column=0,pady=10,columnspan=3)
    return
def deleteB():
    bno=e_id.get()
    # t=MessageBox.askyesno("Close Branch","Do you also want to delete the data pertaining to this branch? This includes persons,donors, receivers and reports.")
    
    
    #ENTER PASSWORD HERE 
    con=mysql.connect(host="localhost",user="root",password="Sherlock@tbbt_got",database="blood_bank") #ENTER PASSWORD HERE 
    
    
    c=con.cursor()
    c.execute("Delete from branch where branch_no='"+bno+"'")
    # if(t==True):
    #     c.execute("select * from branch where branch_no='"+bno+"'")
    #     mods=c.fetchall()
    #     for mod in mods:
    #         city=mod[1]
    #     c.execute("Delete from person where city='"+city+"'")
    #     c.execute("Delete from donor where city='"+city+"'")
    c.execute("commit");
    MessageBox.showinfo("Deletion status","Branch closed down")
    top.destroy()
    return
def insertBranch():
    bno=e_id.get()
    cityb=e_city.get()
    
    
    #ENTER PASSWORD HERE 
    con=mysql.connect(host="localhost",user="root",password="Sherlock@tbbt_got",database="blood_bank") #ENTER PASSWORD HERE 
    
    
    c=con.cursor()
    c.execute("Select * from branch")
    bros=c.fetchall()
    flag=0
    for bro in bros:
        if(bro[0]==bno or bro[1]==cityb):
            flag=1
            break
    if(flag==0):
        c.execute(f"Insert into branch values ('{bno}','{cityb}','DBS_Project')")
        MessageBox.showinfo("Insertion status","Branch Succesfully created")
    elif(flag==1):
        MessageBox.showerror("Insertion status","Branch already exists")
    c.execute("commit");
    top.destroy()
    return
def report_delete_d():
    did=str(e_id.get())+str(date_picked)
    
    
    #ENTER PASSWORD HERE 
    con=mysql.connect(host="localhost",user="root",password="Sherlock@tbbt_got",database="blood_bank") #ENTER PASSWORD HERE 
    
    
    c=con.cursor()
    c.execute("Select * from donor_report")
    bros=c.fetchall()
    flag=0
    for bro in bros:
        if(bro[0]==did):
            flag=1
            break
    if(flag==1):
        c.execute("Delete from donor_report where report_id='"+did+"'")
        MessageBox.showinfo("Deletion status","Report Succesfully deleted")
    elif(flag==0):
        MessageBox.showerror("Deletion status","No such report")
    c.execute("commit");
    top.destroy()
    return
def report_transfusion():
    global rep
    rep=e_id.get()+str(date_picked)
    
    
    #ENTER PASSWORD HERE 
    con=mysql.connect(host="localhost",user="root",password="Sherlock@tbbt_got",database="blood_bank") #ENTER PASSWORD HERE 
    
    
    c=con.cursor()
    c.execute("SELECT * FROM report")
    records=c.fetchall()
    flag=0
    for record in records:
        if(record[0]==rep):
            flag=1
            r_id=record[1]
            date1=record[2]
            amount_r=record[3]
            blood=record[4]
            c.execute("SELECT * FROM receiver_donor where report_id='"+str(rep)+"'")
            chords=c.fetchall()
            global repshow
            repshow=Toplevel()
            repshow.title('BLOOD BANK report')
            repshow.iconbitmap('images.ico')
            repshow.geometry("500x700")
            # repshow.configure(bg="#EF4EDB")
            c.execute("SELECT * FROM person WHERE aadhar='"+r_id+"'")
            name=c.fetchone()
            global nam
            global city
            nam=name[1]
            city=name[2]
            l_bb=Label(repshow,text="HS BLOOD BANK",font=('bold',30),bg="white",fg="green")
            l_bb.grid(row=0,column=0,sticky=W+E,columnspan=3)
            r_name="Name: "+nam
            l_name=Label(repshow,text=r_name,font=('bold',10),bg="white",fg="green")
            l_name.grid(row=1,column=0,pady=10,columnspan=3)
            r_rep="Report ID: "+rep
            l_rep=Label(repshow,text=r_rep,font=('bold',10),bg="white",fg="green")
            l_rep.grid(row=2,column=0,pady=10,columnspan=3)
            r_rid="Receiver ID: "+r_id
            l_rid=Label(repshow,text=r_rid,font=('bold',10),bg="white",fg="green")
            l_rid.grid(row=3,column=0,pady=10,columnspan=3)
            r_date="Date of transfusion: "+str(date1)
            l_date=Label(repshow,text=r_date,font=('bold',10),bg="white",fg="green")
            l_date.grid(row=4,column=0,pady=10,columnspan=3)
            r_amount="Amount of blood : "+str(amount_r)
            l_amount=Label(repshow,text=r_amount,font=('bold',10),bg="white",fg="green")
            l_amount.grid(row=5,column=0,pady=10,columnspan=3)
            r_blood="Blood type: "+blood
            l_blood=Label(repshow,text=r_blood,font=('bold',10),bg="white",fg="green")
            l_blood.grid(row=6,column=0,pady=10,columnspan=3)
            r_city="City/Branch: "+city
            l_city=Label(repshow,text=r_city,font=('bold',10),bg="white",fg="green")
            l_city.grid(row=7,column=0,pady=10,columnspan=3)
            l_donor=Label(repshow,text="DONOR(S)",font=('bold',10),bg="white",fg="green")
            l_donor.grid(row=8,column=0,pady=10,columnspan=3)
            l_did=Label(repshow,text="Donor ID",font=('bold',10),bg="white",fg="green")
            l_did.grid(row=9,column=0,pady=10)
            l_amount=Label(repshow,text="Amount they donated",font=('bold',10),bg="white",fg="green")
            l_amount.grid(row=9,column=1,pady=10)
            l_bloodg=Label(repshow,text="Type Donated",font=('bold',10),bg="white",fg="green")
            l_bloodg.grid(row=9,column=2,pady=10)
            i=9
            for chord in chords:
                i+=1
                l_did=Label(repshow,text=chord[1],font=('bold',10),bg="white",fg="green")
                l_did.grid(row=i,column=0,pady=10)
                l_amount=Label(repshow,text=str(chord[2]),font=('bold',10),bg="white",fg="green")
                l_amount.grid(row=i,column=1,pady=10)
                l_bloodg=Label(repshow,text=chord[3],font=('bold',10),bg="white",fg="green")
                l_bloodg.grid(row=i,column=2,pady=10)
            i+=1
            exitb=Button(top,text="Exit",bg="white",command=exitRepShow)
            exitb.grid(row=i,column=0,columnspan=3)
    if(flag==0):
        MessageBox.showerror("Donation Status","Person not found in database, Please register first")
    c.execute("commit");
    con.close();
    top.destroy()
    return
def report_delete():
    rid=str(e_id.get())+str(date_picked)
    
    
    #ENTER PASSWORD HERE 
    con=mysql.connect(host="localhost",user="root",password="Sherlock@tbbt_got",database="blood_bank") #ENTER PASSWORD HERE 
    
    
    c=con.cursor()
    c.execute("Select * from report")
    bros=c.fetchall()
    flag=0
    for bro in bros:
        if(bro[0]==rid):
            flag=1
            break
    if(flag==1):
        c.execute("Delete from report where report_id='"+rid+"'")
        MessageBox.showinfo("Deletion status","Report Succesfully deleted")
    elif(flag==0):
        MessageBox.showerror("Deletion status","No such report")
    c.execute("commit");
    top.destroy()
    return
def show():  
    if clicked.get()=="Insert Person in the database":
        
        #myLabel = Label(root, text=clicked.get()).pack()
        root.geometry("500x200")
        global top
        top=Toplevel()
        top.title('BLOOD BANK')
        top.iconbitmap('images.ico')
        top.geometry("600x600")
        top.configure(bg="#249C13")
        myLabel = Label(top, text=(clicked.get()).upper())
        myLabel.grid(column=0,row=0,columnspan=2,pady=5)
        id=Label(top,text="Enter Aadhar ID",font=('bold',10),bg="white",fg="green")
        id.grid(row=1,column=0,pady=5)
        name=Label(top,text="Enter name",font=('bold',10),bg="white",fg="green")
        name.grid(row=2,column=0,pady=5)
        address=Label(top,text="Enter address",font=('bold',10),bg="white",fg="green")
        address.grid(row=3,column=0,pady=5)
        blood=Label(top,text="Enter Blood Type",font=('bold',10),bg="white",fg="green")
        blood.grid(row=4,column=0,pady=5)
        city=Label(top,text="Enter City/Branch",font=('bold',10),bg="white",fg="green")
        city.grid(row=5,column=0,pady=5)
        height=Label(top,text="Enter height in cm",font=('bold',10),bg="white",fg="green")
        height.grid(row=6,column=0,pady=5)
        weight=Label(top,text="Enter weight in kgs",font=('bold',10),bg="white",fg="green")
        weight.grid(row=7,column=0,pady=5)
        phone=Label(top,text="Enter Phone number",font=('bold',10),bg="white",fg="green")
        phone.grid(row=8,column=0,pady=5)
        hg_count=Label(top,text="Enter haemoglobin count ",font=('bold',10),bg="white",fg="green")
        hg_count.grid(row=9,column=0,pady=5)
        global e_id
        global e_name
        global e_address
        global e_blood
        global e_city
        global e_height
        global e_weight
        global e_phone
        global e_hg_count
        e_id=Entry(top)
        e_id.grid(row=1,column=1,pady=5)
        e_name=Entry(top)
        e_name.grid(row=2,column=1,pady=5)
        e_address=Entry(top)
        e_address.grid(row=3,column=1,pady=5)
        blood_chart = [
                            "A+", 
                            "B+", 
                            "A-", 
                            "B-",
                            "AB+", 
                            "AB-",
                            "O+",
                            "O-"
                        ]	
#title=Label(root,text="HS BLOOD BANK",bg="red",fg="white",font=('bold',40))
#title.pack()   
        global bloodt
        bloodt = StringVar()
        bloodt.set(blood_chart[0])
        global droped
        droped = OptionMenu(top, bloodt, *blood_chart)
        droped.grid(row=4,column=1,pady=5)
        # e_city=Entry(top)
        # e_city.grid(row=5,column=1,pady=5)
        
        
        #ENTER PASSWORD HERE 
        con=mysql.connect(host="localhost",user="root",password="Sherlock@tbbt_got",database="blood_bank") #ENTER PASSWORD HERE 
        
        
        c=con.cursor()
        c.execute("SELECT city as city FROM branch")
        branches=c.fetchall()
        global branch
        branch=[""]
        branch.clear()
        for branche in branches:
            branch.append(branche[0])
        global cityt
        cityt= StringVar()
        cityt.set(branch[0])
        global drops
        drops = OptionMenu(top, cityt, *branch)
        drops.grid(row=5,column=1,pady=5)
        e_height=Entry(top)
        e_height.grid(row=6,column=1,pady=5)
        e_weight=Entry(top)
        e_weight.grid(row=7,column=1,pady=5)
        e_phone=Entry(top)
        e_phone.grid(row=8,column=1,pady=5)
        e_hg_count=Entry(top)
        e_hg_count.grid(row=9,column=1,pady=5)
        insert=Button(top,text="Insert Record",bg="white",command=insertR)
        insert.grid(row=10,column=0,columnspan=2,pady=10)
        return
    elif clicked.get()=="Donate Blood":
        root.geometry("500x200")
        top=Toplevel()
        top.title('BLOOD BANK')
        top.iconbitmap('images.ico')
        top.geometry("600x300")
        top.configure(bg="#249C13")
        myLabel = Label(top, text=(clicked.get()).upper())
        myLabel.grid(row=0,column=0,columnspan=2)
        id=Label(top,text="Enter Aadhar ID",font=('bold',10),bg="white",fg="green")
        id.grid(row=1,column=0)
        e_id=Entry(top)
        e_id.grid(row=1,column=1)
#checks if id is valid or not and registered in person database
#if yes
    #checks from database if the person is allowed to donate or not
    #if allowed
        global e_amount
        global dateButton
        amount=Label(top,text="Enter Amount of blood",font=('bold',10),bg="white",fg="green")
        amount.grid(row=2,column=0)
        e_amount=Entry(top)
        e_amount.grid(row=2,column=1)
        dateButton = Button(top, text="Pick date for donation", command=grab_date,bg="white",fg="green")
        dateButton.grid(row=3,column=0)
        donate=Button(top,text="Donate",bg="white",command=donation)
        donate.grid(row=4,column=0,columnspan=2)
        #updates donate table to fill data
    #else show error as below
        #MessageBox.showerror("Donation Status","Not eligible to donate")
#if id not registered in person database
#   MessageBox.showerror("Donation Status","Please first register in the database")            
        return
    elif clicked.get()=="Request Blood":
        top=Toplevel()
        top.title('BLOOD BANK')
        top.iconbitmap('images.ico')
        top.geometry("600x300")
        top.configure(bg="#249C13")
        myLabel = Label(top, text=clicked.get())
        myLabel.grid(row=0,column=0,columnspan=2)
        id=Label(top,text="Enter Aadhar ID",font=('bold',10),bg="white",fg="green")
        id.grid(row=1,column=0)
        e_id=Entry(top)
        e_id.grid(row=1,column=1)
#checks if id is valid or not and registered in person database
#if yes
        amount=Label(top,text="Enter Amount of blood needed",font=('bold',10),bg="white",fg="green")
        amount.grid(row=2,column=0)
        e_amount=Entry(top)
        e_amount.grid(row=2,column=1)
        dateButton = Button(top, text="Pick date for Request", command=grab_date,bg="white",fg="green")
        dateButton.grid(row=3,column=0)
        req=Button(top,text="Request",bg="white",command=request)
        req.grid(row=4,column=0,columnspan=2)
        #checks availability
        #if available
            #MessageBox.showinfo("Request Status","blood available, Request granted")
        #else
            #MessageBox.showerror("Request Status","Sorry Blood not available")
#if id not registered in person database
#   MessageBox.showerror("Request Status","Please first register in the database")            
        return
    elif clicked.get()=="Get Report for donation":
        top=Toplevel()
        top.title('BLOOD BANK')
        top.iconbitmap('images.ico')
        top.geometry("600x300")
        top.configure(bg="#249C13")
        myLabel = Label(top, text=clicked.get())
        myLabel.grid(row=0,column=0,columnspan=2)
        id=Label(top,text="Enter Aadhar ID",font=('bold',10),bg="white",fg="green")
        id.grid(row=1,column=0)
        e_id=Entry(top)
        e_id.grid(row=1,column=1)
        dateButton = Button(top, text="Pick date on which blood was transfused", command=grab_date,bg="white",fg="green")
        dateButton.grid(row=2,column=0)
        seed=Button(top,text="Show Report",bg="white",command=report_donate)
        seed.grid(row=3,column=0,columnspan=2)
        return
        return
    elif clicked.get()=="Update a Person in the database":
        top=Toplevel()
        top.title('BLOOD BANK')
        top.iconbitmap('images.ico')
        top.geometry("600x300")
        top.configure(bg="#249C13")
        myLabel = Label(top, text=clicked.get())
        myLabel.grid(row=0,column=0,columnspan=2,pady=10)
        id=Label(top,text="Enter Aadhar ID ",font=('bold',10),bg="white",fg="green")
        id.grid(row=1,column=0,pady=10)
        e_id=Entry(top)
        e_id.grid(row=1,column=1,pady=10)
        edits=Button(top,text="Edit Record",bg="white",command=edit)
        edits.grid(row=4,column=0,columnspan=2,pady=10)
        return
    elif clicked.get()=="Delete a registered person":
        top=Toplevel()
        top.title('BLOOD BANK')
        top.iconbitmap('images.ico')
        top.geometry("600x300")
        top.configure(bg="#249C13")
        myLabel = Label(top, text=clicked.get())
        myLabel.grid(row=0,column=0,columnspan=2,pady=10)
        id=Label(top,text="Enter Aadhar ID for person to be deleted ",font=('bold',10),bg="white",fg="green")
        id.grid(row=1,column=0,pady=10)
        e_id=Entry(top)
        e_id.grid(row=1,column=1,pady=10)
        dele=Button(top,text="Delete Record",bg="white",command=delet)
        dele.grid(row=4,column=0,columnspan=2,pady=10)
        return
    elif clicked.get()=="Insert a newly created Branch":
        top=Toplevel()
        top.title('BLOOD BANK')
        top.iconbitmap('images.ico')
        top.geometry("600x300")
        top.configure(bg="#249C13")
        myLabel = Label(top, text=(clicked.get()).upper())
        myLabel.grid(row=0,column=0,columnspan=2,pady=10)
        id=Label(top,text="Enter branch no ",font=('bold',10),bg="white",fg="green")
        id.grid(row=1,column=0,pady=10)
        e_id=Entry(top)
        e_id.grid(row=1,column=1,pady=10)
        cityB=Label(top,text="Enter city ",font=('bold',10),bg="white",fg="green")
        cityB.grid(row=2,column=0,pady=10)
        global e_city
        e_city=Entry(top)
        e_city.grid(row=2,column=1,pady=10)
        insertB=Button(top,text="Create Branch",bg="white",command=insertBranch)
        insertB.grid(row=3,column=0,columnspan=2,pady=10)
        return
    elif clicked.get()=="Close down a branch":
        top=Toplevel()
        top.title('BLOOD BANK')
        top.iconbitmap('images.ico')
        top.geometry("600x300")
        top.configure(bg="#249C13")
        myLabel = Label(top, text=clicked.get())
        myLabel.grid(row=0,column=0,columnspan=2,pady=10)
        id=Label(top,text="Enter branch no ",font=('bold',10),bg="white",fg="green")
        id.grid(row=1,column=0,pady=10)
        e_id=Entry(top)
        e_id.grid(row=1,column=1,pady=10)
        deleB=Button(top,text="Close Branch",bg="white",command=deleteB)
        deleB.grid(row=4,column=0,columnspan=2,pady=10)
        return
    elif clicked.get()=="Get Report for transfusion":
        top=Toplevel()
        top.title('BLOOD BANK')
        top.iconbitmap('images.ico')
        top.geometry("600x300")
        top.configure(bg="#249C13")
        myLabel = Label(top, text=clicked.get())
        myLabel.grid(row=0,column=0,columnspan=2)
        id=Label(top,text="Enter Aadhar ID",font=('bold',10),bg="white",fg="green")
        id.grid(row=1,column=0)
        e_id=Entry(top)
        e_id.grid(row=1,column=1)
        dateButton = Button(top, text="Pick date on which blood was transfused", command=grab_date,bg="white",fg="green")
        dateButton.grid(row=2,column=0)
        see=Button(top,text="Show Report",bg="white",command=report_transfusion)
        see.grid(row=3,column=0,columnspan=2)
        return
    elif clicked.get()=="Delete a report for transfusion":
        top=Toplevel()
        top.title('BLOOD BANK')
        top.iconbitmap('images.ico')
        top.geometry("600x300")
        top.configure(bg="#249C13")
        myLabel = Label(top, text=clicked.get())
        myLabel.grid(row=0,column=0,columnspan=2)
        id=Label(top,text="Enter Aadhar ID",font=('bold',10),bg="white",fg="green")
        id.grid(row=1,column=0)
        e_id=Entry(top)
        e_id.grid(row=1,column=1)
        dateButton = Button(top, text="Pick date on which blood was transfused", command=grab_date,bg="white",fg="green")
        dateButton.grid(row=2,column=0)
        delr=Button(top,text="Delete Report",bg="white",command=report_delete)
        delr.grid(row=3,column=0,columnspan=2)
        return
    elif clicked.get()=="Delete a report for donation":
        top=Toplevel()
        top.title('BLOOD BANK')
        top.iconbitmap('images.ico')
        top.geometry("600x300")
        top.configure(bg="#249C13")
        myLabel = Label(top, text=clicked.get())
        myLabel.grid(row=0,column=0,columnspan=2)
        id=Label(top,text="Enter Aadhar ID",font=('bold',10),bg="white",fg="green")
        id.grid(row=1,column=0)
        e_id=Entry(top)
        e_id.grid(row=1,column=1)
        dateButton = Button(top, text="Pick date on which blood was donated", command=grab_date,bg="white",fg="green")
        dateButton.grid(row=2,column=0)
        delr=Button(top,text="Delete Report",bg="white",command=report_delete_d)
        delr.grid(row=3,column=0,columnspan=2)
        return
    else: 
        root.quit()
        return
def select(e):
    root.bind('<Configure>',select)
    w=e.width+200
    h=e.height+100
    root.geometry(f"{w}x{h}")
    root.bind('<Configure>', resizer)
options = [
    "Insert Person in the database", 
    "Update a Person in the database",
    "Insert a newly created Branch",
    "Delete a registered person",
    "Close down a branch",
    "Delete a report for transfusion",
    "Delete a report for donation",
    "Donate Blood", 
    "Request Blood", 
    "Get Report for donation",
    "Get Report for transfusion", 
    "Exit"
]	
#title=Label(root,text="HS BLOOD BANK",bg="red",fg="white",font=('bold',40))
#title.pack()
clicked = StringVar()
clicked.set(options[0])
global drop
drop = OptionMenu(root, clicked, *options,command=select)
drop.bind('<Button-1>',select)
#drop.pack()
global myButton
myButton = Button(root, text="Proceed", command=show,bg="white",fg="green")
#myButton.pack()
global button1,button2
# my_canvas.create_image(0,0, image=bg, anchor="nw")
# my_canvas.create_text(50,20,text="HS BLOOD BANK", font=("Helvetica", 20), fill="white")
button1=my_canvas.create_window(50,50,anchor="nw",window=drop)
button2=my_canvas.create_window(50,80,anchor="nw",window=myButton)
root.bind('<Configure>', resizer)
root.mainloop()
