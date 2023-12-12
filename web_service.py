import pymysql
from flask import *
from werkzeug.utils import secure_filename
import os

from dbconnect import *
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)


@app.route("/user_register", methods=['post'])
def user_register():
    try:
        fname = request.form['fname']
        lname = request.form['lname']
        place = request.form['place']
        post = request.form['post']
        pin = request.form['pin']
        district = request.form['district']
        phone = request.form['phone']
        email = request.form['email']
        username = request.form['username']
        password = request.form['pass']
        q = "insert into login values(null,%s,%s,'user')"
        val = username, password
        fun = iud(q, val)
        qry = "insert into user values(null,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        vals = str(fun), fname, lname, place, post, pin, district, phone, email
        iud(qry, vals)
        return jsonify({'task': 'success'})
    except Exception as e:
        print(e)
        return jsonify({'task': 'Already Exists!!'})


@app.route("/user_login", methods=['post'])
def user_login():
    username = request.form['uname']
    password = request.form['pass']
    q = "select * from login where Username=%s and Password=%s"
    val = username, password
    fun = selectone(q, val)
    id = fun[0]
    if fun is None:
        return jsonify({'task': 'fail'})
    else:
        return jsonify({'task': 'success', 'id': id})


@app.route("/user_feedback", methods=['post'])
def user_feedback():
    user_id = request.form['lid']
    feedback = request.form['feedback']
    q = "insert into feedback values(null,%s,%s,curdate())"
    val = str(user_id), feedback
    fun = iud(q, val)
    return jsonify({'task': 'success'})


@app.route("/user_viewitem", methods=['post'])
def user_viewitem():
    type = request.form['type']
    q = "select * from item where item_type=%s"
    val = (type)
    vals = androselectalls(q, val)
    print(val)
    return jsonify(vals)


@app.route("/user_viewitems", methods=['post'])
def user_viewitems():
    q = "select * from item"
    val = (type)
    vals = androselectall(q)
    print(val)
    return jsonify(vals)


@app.route("/newitems", methods=['post'])
def newitems():
    type = request.form['type']
    q = "SELECT * FROM `item` WHERE `Item_type`=%s"
    val = (type)

    val = androselectalls(q, val)
    return jsonify(val)


@app.route("/assign_work", methods=['post'])
def assign_work():
    agent_id = request.form['agent_id']
    print(agent_id)
    q = "SELECT `request`.`Description`,`request`.`Date`,`user`.`First_Name`,`user`.`Last_Name`,`user`.`Phone` ,`donor`.`First_Name` AS dname ,`donor`.`Last_Name` AS dlname,`assign`.`Assign_id`,`request`.`Request_id` FROM `request` JOIN  `user` ON `request`.`Login_id`=`user`.`Login_id` JOIN `assign` ON `assign`.`Request_id`=`request`.`Request_id` JOIN `donor` ON `donor`.`Login_id`=`request`.`Donor_id`WHERE `assign`.`Agent_id`=%s AND `assign`.`Status`='pending'"
    val = (agent_id)
    fun = androselectalls(q, val)
    return jsonify(fun)


@app.route("/update_work", methods=['post'])
def update_work():
    status = request.form['status']
    reqid = request.form['req_id']
    q = "UPDATE `assign` SET `Status`=%s WHERE `Assign_id`=%s"
    val = (status, reqid)
    iud(q, val)
    return jsonify({'task': 'success'})


@app.route("/user_request", methods=['post'])
def user_request():
    login_id = request.form['lid']
    print(login_id)
    item_id = request.form['item_id']
    print(item_id)
    description = request.form['description']
    print(description)
    donor_id = request.form['donor_id']
    print(donor_id)
    q = "insert into request values(null,%s,%s,%s,%s,'pending',curdate())"

    val = (str(login_id), str(item_id), description, str(donor_id))
    iud(q, val)
    return jsonify({'task': 'success'})

@app.route('/forgotpassword',methods=['post'])
def forgotpassword():
    email=request.form['email']
    username=request.form['username']
    qry="SELECT `login`.`Password` FROM `login` JOIN `user` ON `user`.`Login_id`=`login`.`Login_id` WHERE `login`.`Username`=%s AND `user`.`Email`=%s"
    val=(username,email)
    res=selectone(qry,val)
    if res is None:
        return jsonify({"task":"invalid"})
    else:
        password=res[0]
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
        return jsonify({"task": "sucess"})

app.run(host="0.0.0.0", port=5000)
