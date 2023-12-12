import smtplib
from email.mime.text import MIMEText

from flask import *
from werkzeug.utils import secure_filename

from dbconnect import *

app=Flask(__name__)
app.secret_key='abc'
import functools
def login_required(func):
    @functools.wraps(func)
    def secure_function():
        if "login_id" not in session:
            return redirect ("/")
        return func()
    return secure_function

@app.route("/")
def login():
    session.clear()
    return  render_template("index1.html")



@app.route("/new")

def new():

    return  render_template("login.html")

@app.route("/inn")
@login_required
def inn():
    return  render_template("index.html")

@app.route("/adminhome")
@login_required
def adminhome():
    return  render_template("Admin_Home.HTML")
@app.route("/delete_report")
@login_required
def delete_report():
    q="delete from report where Report_id=%s"
    val=request.args.get('id')
    iud(q,val)
    return  '''<script>window.location='/donor_view_report'</script>'''

@app.route("/edit_item")
@login_required
def edit_item():
    id=request.args.get('id')
    session['id']=id
    q="select * from item where Item_id=%s"
    val=str(id)
    result=selectone(q,val)
    print(result)
    return  render_template("edit_item.html",vals=result)


@app.route("/update_item",methods=['post'])
@login_required
def update_item():
    login=session['id']
    item_name=request.form['item_name']
    item_type=request.form['textfield']
    quantity=request.form['textfield2']
    q="update item set Item_type=%s,Item_name=%s,Quantity=%s where Item_id=%s"
    val=(item_name,item_type,str(quantity),str(login))
    print(val)
    iud(q,val)
    return '''<script>alert("Item Edited Successfully!!"); window.location='/view_item';</script>'''


@app.route("/viewdonor")
@login_required
def viewdonor():
    q="select * from donor"
    result=select(q)
    return  render_template("View_Donor.HTML",val=result)

@app.route("/edit_donor")
@login_required
def edit_donor():
    id=request.args.get('id')
    session['id']=id
    q="select * from donor where Login_id = %s"
    val=(id)
    result=selectone(q,val)
    return  render_template("Edit_Donor.html",vals=result)

@app.route("/delete_donor")
@login_required
def delete_donor():
    id = request.args.get('id')
    q="delete from login where Login_id=%s"
    val=id
    iud(q,val)
    q = "delete from donor where Login_id=%s"
    val = id
    iud(q, val)

    return  '''<script>alert("Deleted successfully!");window.location='/viewdonor'</script>'''

@app.route("/delete_item")
@login_required
def delete_item():
    id=request.args.get('id')
    q="delete from item where Item_id=%s"
    val=str(id)
    iud(q,val)
    return '''<script> window.location='/view_item'</script>'''


@app.route("/viewdeliveryagent")
@login_required
def viewdeliveryagent():
    q = "select * from deliveryagent"
    result = select(q)
    return  render_template("View_Delivery_Agent1.html",val=result)


@app.route("/viewuser")
@login_required
def viewuser():
    q="select * from user"
    result=select(q)
    return  render_template("View_User.html",val=result)


@app.route("/viewfeedback")
@login_required
def viewfeedback():
    q="SELECT `user`.`First_Name`,`user`.`Last_Name`,`feedback`.`Feedback`,`feedback`.`Date` FROM `feedback` JOIN `user` ON `feedback`.`Login_id`=`user`.`Login_id`"
    result=select(q)
    return  render_template("View_Feedback.html",val=result)



@app.route("/viewreport")
@login_required
def viewreport():
    q="SELECT `report`.`Date`,`donor`.`First_Name`,`donor`.`Last_Name`,`report`.`Report` FROM `report` JOIN `donor` ON `donor`.`Login_id`=`report`.`Login_id`"
    result=select(q)
    return  render_template("View_Report.html",val=result)


@app.route("/add_donor",methods=['post'])
@login_required
def add_donor():
    return  render_template("Add_Donor.html")

@app.route("/edit_deliveryagent",methods=['get'])
@login_required
def edit_deliveryagent():
    id=request.args.get('id')
    session['id']=id
    q="select * from `deliveryagent` where Login_id=%s"
    val=str(id)

    result=selectone(q,val)

    return  render_template("edit_Delivery_Agent.html",vals=result)

@app.route("/donorindex")
@login_required
def donorindex():
    return  render_template("Donorindex.html")


@app.route("/donor_view_delivery_agent")
@login_required
def donor_view_delivery_agent():
    q="select * from deliveryagent"
    result=select(q)
    return  render_template("Donor_View_Delivery_Agent.html",val=result)


@app.route("/add_item_details",methods=['post'])
@login_required
def add_item_details():
    return  render_template("Add_Item_Details.html")

@app.route("/update_deliveryagent",methods=['post'])
@login_required
def update_deliveryagent():
    id=session['id']
    firstname = request.form['textfield']
    lastname = request.form['textfield2']
    gender = request.form['radiobutton']
    date = request.form['textfield3']
    place = request.form['textfield4']
    email = request.form['textfield7']
    phone = request.form['textfield8']

    q="update deliveryagent set First_Name=%s,Last_Name=%s,Gender=%s,Date=%s,`Place`=%s,`Email`=%s,`Phone`=%s WHERE `Login_id`=%s"
    val=firstname,lastname,gender,date,place,email,phone,str(id)
    iud(q,val)
    return '''<script>alert("Successfully Updated!!"); window.location='/donor_view_delivery_agent';</script>'''

@app.route("/delete_deliveryagent")
@login_required
def delete_deliveryagent():
    q="delete from deliveryagent where Agent_id=%s"
    val=request.args.get('id')
    iud(q,val)
    return  '''<script>window.location='/donor_view_delivery_agent'</script>'''

@app.route("/view_request")
@login_required
def view_request():
    qry="SELECT * FROM item"
    q=select(qry)
    return  render_template("View_Request1.html",val=q,vals=0)

@app.route("/requested_item",methods=['post'])
@login_required
def requested_item():
    type=request.form['select']
    print(type)
    lid = session['login_id']
    q="SELECT `item`.`Item_name`,`user`.`First_Name`,`user`.`Last_Name`,`item`.`Quantity`,`request`.`Request_id` FROM " \
      "request JOIN item ON `request`.`Item_id`=`item`.`Item_id` JOIN `user` ON user.`Login_id`=`request`.`Login_id` " \
      "WHERE `request`.`Item_id`=%s  AND `request`.`Donor_id`=%s"
    valll=(type,str(lid))
    l=selectall(q,valll)
    qry = "SELECT * FROM item"
    qs = select(qry)
    return  render_template("view_request1.html",vals=l,val=qs)

@app.route("/assign_agent",methods=['get'])
@login_required
def assign_agent():
    id = request.args.get('id')
    session['id']=id
    a="SELECT * FROM `deliveryagent`"
    q=select(a)
    return  render_template("Assign_agent1.html",val=q)

@app.route("/assigning_agent",methods=['post'])
@login_required
def assigning_agent():
    id=session['id']
    did=request.form['select']
    lid= session['login_id']
    q="insert into assign values(null,%s,%s,%s,'pending')"
    val=str(lid),str(did),str(id)
    iud(q,val)
    return '''<script>alert("successfully assigned"); window.location='/view_request';</script>'''

@app.route("/view_status")
@login_required
def view_status():
    q="SELECT `deliveryagent`.`First_Name`,`deliveryagent`.`Last_Name`,`item`.*,`user`.`First_Name`,`user`.`Last_Name`,`assign`.`Status` FROM assign JOIN `deliveryagent` ON `deliveryagent`.`Login_id`=`assign`.`Agent_id` JOIN `request` ON `request`.`Request_id`=`assign`.`Request_id` JOIN `user` ON `user`.`Login_id`=`request`.`Login_id` JOIN `item`  ON `item`.`Item_id`=`request`.`Item_id`"
    ps=select(q)
    return  render_template("View_Status.html",val=ps)

@app.route("/report_add",methods=['post'])
@login_required
def report_add():
    id=session['login_id']
    file = request.files['file']
    fname = secure_filename(file.name)
    file.save("static/report/" + fname)
    q="insert into report values(null,%s,curdate(),%s)"
    val=str(id),fname
    fun=iud(q,val)
    return  '''<script>alert("Successfully added");window.location='/report';</script>'''

@app.route("/donor_view_report",methods=['post','get'])
@login_required
def donor_view_report():
    id = session['login_id']
    q="select * from report where Login_id=%s"
    val=str(id)
    fun=selectall(q,val)
    return  render_template("Donor_View_Report.html",vals=fun)


@app.route("/view_item")
@login_required
def view_item():
    q="SELECT `item`.`Item_name`,`item`.`Quantity`,Item_id FROM `item`"
    result=select(q)
    return  render_template("View_Items.html",val=result)



@app.route("/add_delivery_agent",methods=['post'])
@login_required
def add_delivery_agent():
    return  render_template("Add_Delivery_Agent.html")

@app.route("/report")
@login_required
def report():
    user_id=request.args.get('uid')
    session['uid']=user_id
    did=request.args.get('did')
    session['did'] = did
    item=request.args.get('item')
    session['item'] = item
    return  render_template("Report.html")

@app.route("/login_code",methods=['post'])

def login_code():
    username=request.form['textfield']
    password=request.form['textfield2']
    q="select * from login where username=%s and password=%s"
    val=(username,password)
    result = selectone(q,val)
    if(result is None):
        return '''<script>alert("Invalid User or Password!!");window.location='/';</script>'''
    else:
        session['login_id']=result[0]
        if result[3]=="Admin":
             return '''<script>alert("Login Successfull!!"); window.location='/adminhome';</script>'''
        elif result[3]=="Donor":
            return '''<script>alert("Login Successfull!!"); window.location='/donorindex';</script>'''
        else:
            return '''<script>alert("Invalid User or Password!!");window.location='/';</script>'''



@app.route("/register_donor",methods=['post'])
@login_required
def register_donor():
    try:
        firstname=request.form['textfield']
        lastname=request.form['textfield2']
        gender=request.form['radiobutton']
        date=request.form['textfield3']
        place=request.form['textfield4']
        post=request.form['textfield5']
        pin=request.form['textfield6']
        email=request.form['textfield7']
        phone=request.form['textfield8']
        username = request.form['textfield9']
        password = request.form['textfield10']
        try:

            gmail = smtplib.SMTP('smtp.gmail.com', 587)
            gmail.ehlo()
            gmail.starttls()
            gmail.login('shafeenshaznfc@gmail.com', '14731473')
        except Exception as e:
            print("Couldn't setup email!!" + str(e))

        msg = MIMEText("Your password is " + password + " and your username is " + username)
        msg['Subject'] = 'LifeLine'
        msg['To'] = email
        msg['From'] = 'projectdbc4@gmail.com'

        try:
            gmail.send_message(msg)
            print("see")

        except Exception as e:
            print("COULDN'T SEND EMAIL", str(e))


        q="insert into login values(null,%s,%s,%s)"
        val=(username,password,'Donor')
        id=iud(q,val)

        q="insert into donor values(null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val=(str(id),firstname,lastname,gender,date,place,post,str(pin),email,str(phone))
        print(val)
        iud(q,val)
        return '''<script>alert("Registered Successfully!-!"); window.location='/viewdonor';</script>'''

    except Exception as e:
        return '''<script>alert("Already Exists!!"); window.location='/viewdonor';</script>'''


@app.route("/register_deliver_agent",methods=['post'])
@login_required
def register_deliver_agent():
    try:
        firstname=request.form['textfield']
        lastname=request.form['textfield2']
        gender=request.form['radiobutton']
        date=request.form['textfield3']
        place=request.form['textfield4']
        email=request.form['textfield7']
        phone=request.form['textfield8']
        username = request.form['textfield9']
        password = request.form['textfield10']
        try:

            gmail = smtplib.SMTP('smtp.gmail.com', 587)
            gmail.ehlo()
            gmail.starttls()
            gmail.login('shafeenshaznfc@gmail.com', '14731473')
        except Exception as e:
            print("Couldn't setup email!!" + str(e))

        msg = MIMEText("Your password is " + password +" and your username is "+username)
        msg['Subject'] = 'LifeLine'
        msg['To'] = email
        msg['From'] = 'projectdbc4@gmail.com'

        try:
            gmail.send_message(msg)
            print("see")

        except Exception as e:
            print("COULDN'T SEND EMAIL", str(e))
        q="insert into login values(null,%s,%s,%s)"
        val=(username,password,'deliver_agent')
        id=iud(q,val)

        q="insert into deliveryagent values(null,%s,%s,%s,%s,%s,%s,%s,%s)"
        val=(str(id),firstname,lastname,gender,date,place,email,str(phone))
        print(val)
        iud(q,val)
        return '''<script>alert("Registered Successfully!!"); window.location='/donor_view_delivery_agent';</script>'''
    except Exception as e:
        print(e)
        return '''<script>alert("Already Exists!!"); window.location='/donor_view_delivery_agent';</script>'''

@app.route("/update_donor",methods=['post'])
@login_required
def update_donor():
    id=session['id']
    print(id)
    firstname=request.form['textfield']
    lastname=request.form['textfield2']
    gender=request.form['radiobutton']
    date=request.form['textfield3']
    place=request.form['textfield4']
    post=request.form['textfield5']
    pin=request.form['textfield6']
    email=request.form['textfield7']
    phone=request.form['textfield8']
    q="UPDATE `donor` SET `First_Name`=%s,`Last_Name`=%s,`gender`=%s,DOB=%s,`Place`=%s,`Post`=%s,`Pin`=%s,`Email`=%s,`Phone`=%s WHERE `Login_id`=%s"
    val=(firstname,lastname,gender,date,place,post,pin,email,phone,str(id))
    print(val)
    iud(q,val)
    return '''<script>alert("Registered Successfully!-!"); window.location='/viewdonor';</script>'''


@app.route("/register_item",methods=['post'])
@login_required
def register_item():
    login=session['login_id']
    item_name=request.form['item_name']
    item_type=request.form['textfield']
    quantity=request.form['textfield2']
    q="insert into item values(null,%s,%s,%s,%s)"
    val=(str(login),item_name,item_type,quantity)
    print(val)
    iud(q,val)
    return '''<script>alert("Item Added Successfully!!"); window.location='/view_item';</script>'''



app.run(debug=True)
