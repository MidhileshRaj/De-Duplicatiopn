from flask import *
from DBConnection import Db
app = Flask(__name__)
app.secret_key='samih234'

# static_path = 'D:\\final\\cloud_deduplication\\static'
# static_path = "D:\\kavya\\mahe\\final\\cloud_deduplication\\static"
static_path = "D:\\kabu\\final\\cloud_deduplication\\static"
@app.route('/')
def login():
    return render_template('login index.html')


@app.route('/login_post', methods=['POST'])
def login_post():
    username=request.form['textfield']
    password=request.form['textfield2']
    db=Db()
    qry="select * from login where username ='"+username+"' and password='"+password+"'"
    res=db.selectOne(qry)
    if res is not None:
        session['lid']=res['login_id']
        if res['type']=="admin":
            return redirect('/adminhome')
        elif res['type']=="student":
            return redirect('/')
        elif res['type']=="teacher":
            return redirect('/thome')
        else :
            return """<script>alert("invalid credentials");window.location="/"</script>"""
    else:
        return """<script>alert("invalid credentials");window.location="/"</script>"""


@app.route('/adminhome')
def adminhome():
    return render_template("admin/index.html")
    # return render_template("admin/ahome.html")


@app.route('/admin_adddepartment')
def admin_adddepartment():
    return render_template('admin/department add.html')

@app.route('/adddepartment_post',methods=['POST'])
def adddepartment_post():
    adddepartment=request.form['textfield']
    db=Db()
    qry="INSERT INTO `department`(`department`)VALUES('"+adddepartment+"')"
    res=db.insert(qry)
    return "ok"

@app.route('/edit_department/<id>')
def edit_department(id):
    db=Db()
    qry="SELECT * FROM `department` WHERE `department_id`='"+id+"'"
    res=db.selectOne(qry)
    return render_template("admin/department edit.html",data=res)

@app.route('/edit_department_post', methods=['POST'])
def edit_department_post():
    department = request.form['textfield']
    id = request.form['id']
    db = Db()
    qry = "UPDATE`department`SET department='"+department+"'WHERE `department_id`='"+id+"'"
    res = db.update(qry)
    return '''<script>alert("updated");window.location='/admin_viewdepartment'</script>'''


@app.route('/admin_viewdepartment')
def admin_viewdepartment():
    db=Db()
    qry="SELECT * FROM `department`"
    res=db.select(qry)
    return render_template('admin/view department.html',data=res)
@app.route('/admin_viewdepartment_post',methods=['POST'])
def admin_viewdepartment_post():
    search = request.form['textfield']
    db = Db()
    qry = "SELECT * FROM `department` where department like '%"+search+"%'"
    res = db.select(qry)
    return render_template('admin/view department.html', data=res)

@app.route('/viewdepartment_post',methods=['POST'])
def viewdepartment_post():
      search=request.form['textfield']
      return "ok"

@app.route('/admin_addcourse')
def admin_addcourse():
    db=Db()
    qry="SELECT * FROM`department`"
    res=db.select(qry)
    return render_template('admin/Add course.html',data=res)

@app.route('/addcourse_post',methods=['POST'])
def addcourse_post():
    department=request.form['select']
    course=request.form['textfield2']
    sem=request.form['textfield4']
    db=Db()
    qry="INSERT INTO `course`(`course`,`department_id`,`total_semester`)VALUES('"+course+"','"+department+"','"+sem+"')"
    res=db.insert(qry)


    return "ok"



@app.route('/edit_course/<id>')
def edit_course(id):
    db=Db()
    qry="SELECT * FROM `course` WHERE `course_id`='"+id+"'"
    res=db.selectOne(qry)
    qry2="select * from department"
    res2=db.select(qry)
    return render_template("admin/edit_course.html",data=res,data2=res2)

@app.route('/edit_course_post', methods=['POST'])
def edit_course_post():
    department = request.form['select']
    course = request.form['textfield2']
    sem = request.form['textfield4']
    id=request.form['cid']
    db=Db()
    qry="UPDATE `course` SET `course`='"+course+"',`department_id`='"+department+"',`total_semester`='"+sem+"' WHERE `course_id`='"+id+"'"
    res=db.update(qry)
    return '''<script>alert("updated");window.location='/admin_viewcourse'</script>'''



@app.route('/admin_viewcourse')
def admin_viewcourse():
    db=Db()
    qry="SELECT * FROM `course` INNER JOIN `department` ON `department`.`department_id`=`course`.`department_id`"
    res=db.select(qry)
    return render_template('admin/View course.html',data=res)

@app.route('/admin_viewcourse_post', methods=['POST'])
def admin_viewcourse_post():
    search=request.form['textfield']
    db = Db()
    qry = "SELECT * FROM `course` INNER JOIN `department` ON `department`.`department_id`=`course`.`department_id` where course like '%"+search+"%'"
    res = db.select(qry)
    return render_template('admin/View course.html', data=res)


@app.route('/viewcourse_post',methods=['POST'])
def viewcourse_post():
    search=request.form['textfield']
    return "ok"


@app.route('/admin_addsubject')
def admin_addsubject():
    db=Db()
    qry="SELECT * FROM `course`"
    res=db.select(qry)
    return render_template('admin/Add subject.html',data=res)

@app.route('/addsubject_post',methods=['POST'])
def addsubject_post():
    semester=request.form['textfield']
    course_id=request.form['select']
    subject=request.form['textfield3']
    db=Db()
    qry="INSERT INTO `subject`(`subject`,`course_id`,`semester`)VALUES('"+subject+"','"+course_id+"','"+semester+"')"
    print(qry)
    res=db.insert(qry)
    print(res)
    return "ok"

@app.route('/edit_subject/<id>')
def edit_subject (id):
    db = Db()
    qry = "SELECT * FROM `subject` WHERE `subject_id`='" + id + "'"
    res = db.selectOne(qry)
    qry2= "select * from course"
    res2=db.select(qry2)
    return render_template("admin/Edit subject.html",data=res,data2=res2)

@app.route('/edit_subject_post', methods=['POST'])
def edit_subject_post():
    semester = request.form['textfield']
    course_id = request.form['select']
    subject = request.form['textfield3']
    id = request.form['id']
    db = Db()
    qry ="UPDATE `subject`SET`subject`='"+subject+"',`course_id`='"+course_id+"',`semester`='"+semester+"'WHERE`subject_id`='"+id+"'"
    res = db.update(qry)
    return '''<script>alert("updated");window.location='/admin_viewsubject'</script>'''

@app.route('/admin_viewsubject')
def admin_viewsubject():
    db=Db()
    qry="SELECT * FROM `subject` INNER JOIN `course` ON `course`.`course_id`=`subject`.`course_id` INNER JOIN `department` ON `department`.`department_id`=`course`.`department_id`"
    res=db.select(qry)
    return render_template('admin/View subject.html',data=res)
@app.route('/admin_viewsubject_post',methods=['post'])
def admin_viewsubject_post():
    search = request.form['textfield']
    db = Db()
    qry = "SELECT * FROM `subject` INNER JOIN `course` ON `course`.`course_id`=`subject`.`course_id` INNER JOIN `department` ON `department`.`department_id`=`course`.`department_id` where subject like '%"+search+"%'"
    res = db.select(qry)
    return render_template('admin/View subject.html', data=res)



@app.route('/viewsubject_post',methods=['POST'])
def viewsubject_post():
    search=request.form['textfield']
    return "ok"

@app.route('/admin_teacherverification')
def admin_teacherverification():
    db=Db()
    qry="SELECT * FROM `teacher` INNER JOIN`department` ON `department`.`department_id`=`teacher`.`department_id`"
    res=db.select(qry)
    return render_template('admin/View teacher.html',data=res)

@app.route('/admin_studentverification')
def admin_studentverification():
    db=Db()
    qry="SELECT * FROM `student`INNER JOIN `course`  ON `course`.`course_id`=`student`.`course_id`"
    res=db.select(qry)
    return render_template('admin/View student.html',data=res)

@app.route('/admin_viewcomplaints')
def admin_viewcomplaints():
    db = Db()
    qry = "SELECT * FROM `complaints`INNER JOIN `student` ON `complaints`.`user_id`=`student`.`login_id` "
    res = db.select(qry)
    return render_template('admin/View complaints.html',data=res)

@app.route('/admin_feedback')
def admin_feedback():
    db=Db()
    qry="SELECT * FROM `feedback` INNER JOIN `student` ON `student`.`login_id`=`feedback`.`user_id`"
    res=db.select(qry)
    return render_template('admin/Feedback.html',data=res)

@app.route('/admin_reply/<id>')
def admin_reply(id):
    return render_template('admin/Reply.html',id=id)
@app.route('/reply_post',methods=['POST'])
def reply_post():
    reply=request.form['textarea']
    id=request.form['cid']
    db=Db()
    qry="UPDATE`complaints`SET`reply`='"+reply+"',`status`='replied' WHERE`complaints_id`='"+id+"'"
    res=db.update(qry)
    return '''<script>alert("sending");window.location='/admin_viewcomplaints'</script>'''





@app.route('/delete_course/<id>')
def delete_course(id):
    db=Db()
    qry="DELETE FROM `course` WHERE `course_id`='"+id+"'"
    res=db.delete(qry)
    return '''<script>alert("deleted");window.location='/admin_viewcourse'</script>'''

@app.route('/delete_subject/<id>')
def delete_subject(id):
    db=Db()
    qry="DELETE FROM `subject` WHERE `subject_id`='"+id+"'"
    res=db.delete(qry)
    return '''<script>alert("deleted");window.location='/admin_viewsubject'</script>'''

@app.route('/delete_department/<id>')
def delete_department(id):
    db=Db()
    qry="DELETE FROM `department` WHERE `department_id`='"+id+"'"
    res=db.delete(qry)
    return '''<script>alert("deleted");window.location='/admin_viewdepartment'</script>'''


#=============Teacher============================#

@app.route('/thome')
def thome():
    return render_template("teacher/teacher_index.html")
@app.route('/Sign_up')
def sign_up():
    db = Db()
    qry = "SELECT * FROM `department`"
    res = db.select(qry)
    return render_template('teacher/signup index.html',data=res)

@app.route('/Signup_post',methods=['post'])
def signup_post():
    first_name=request.form['textfield']
    # last_name=request.form['textfield2']
    gender=request.form['textfield3']
    department=request.form['textfield4']
    Email=request.form['textfield5']
    phone_no=request.form['textfield7']
    place=request.form['textfield8']
    post=request.form['textfield9']
    pin=request.form['textfield10']
    password=request.form['textfield11']
    confirm_password=request.form['textfield12']
    photo=request.files['fileField']
    from datetime import datetime
    dt=datetime.now().strftime("%Y%m%d-%H%M%S")
    photo.save("C:\\Users\\USER\\PycharmProjects\\cloud_deduplication\\static\\teacher\\" +dt+".jpg")
    path="/static/teacher/"+dt+".jpg"
    db=Db()
    qry="INSERT INTO `login`(`username`,`password`,`type`)VALUES('"+Email+"','"+confirm_password+"','teacher')"
    res=db.insert(qry)
    qry2="INSERT INTO `teacher`(`login_id`,`name`,`gender`,`phone_number`,`place`,`post`,`pin`,`email`,`photo`,`department_id`,`status`)VALUES('"+str(res)+"','"+first_name+"','"+gender+"','"+phone_no+"','"+place+"','"+post+"','"+pin+"','"+Email+"','"+path+"','"+department+"','pending')"
    res2=db.insert(qry2)
    return '''<script>alert('Registered sucessfully..');window.location='/'</script>'''



@app.route('/view_complaints')
def view_complaints():
    db=Db()
    qry="SELECT * FROM `complaints`INNER JOIN `student`ON `complaints`.`user_id`=`student`.`login_id` "
    res=db.select(qry)
    return render_template('teacher/complaints.html',data=res)

@app.route('/view_department')
def view_department():
    db=Db()
    qry="SELECT * FROM `department`"
    res=db.select(qry)
    return render_template('teacher/view department.html',data=res)

@app.route('/view_department_post', methods=['POST'])
def view_department_post():
    search=request.form['textfield']
    db = Db()
    qry = "SELECT * FROM `department` WHERE `department` LIKE '%"+search+"%' "
    res = db.select(qry)
    return render_template('teacher/view department.html', data=res)

@app.route('/view_course')
def view_course():
    db=Db()
    qry="SELECT * FROM `course` INNER JOIN `department` ON  `department`.`department_id`=`course`.`department_id`"
    res=db.select(qry)
    return render_template('teacher/View course.html',data=res)

@app.route('/view_course_post', methods=['POST'])
def view_course_post():
    search=request.form['textfield']
    db=Db()
    qry="SELECT * FROM `course` WHERE `course` LIKE '%"+search+"%'"
    res=db.select(qry)
    return  render_template('teacher/view course.html',data=res)

@app.route('/view_subject')
def view_subject():
    db=Db()
    qry="SELECT * FROM `subject` INNER JOIN `course` ON `subject`.`course_id`=`course`.`course_id` INNER JOIN `department` ON `course`.`department_id`=`department`.`department_id`"
    res=db.select(qry)
    return render_template('teacher/view subject.html',data=res)

@app.route('/view_subject_post', methods=['POST'])
def view_subject_post():
     search=request.form['textfield']
     db=Db()
     qry="SELECT * FROM `subject` WHERE `subject` LIKE '%"+search+"%'"
     res=db.select(qry)
     return render_template('teacher/view subject.html',data=res)

@app.route('/view_profile')
def view_profile():
      db=Db()
      qry="SELECT * FROM `teacher`JOIN `department` ON `teacher`.`department_id`=`department`.`department_id` WHERE `login_id`='"+str(session['lid'])+"'"
      res=db.selectOne(qry)
      return render_template('teacher/view profile.html',data=res)


@app.route('/edit_profile')
def edit_profile():
    db=Db()
    db = Db()
    qry = "SELECT * FROM `department`"
    res = db.select(qry)
    qry1="SELECT * FROM `teacher`JOIN `department` ON `teacher`.`department_id`=`department`.`department_id` WHERE `login_id`='"+str(session['lid'])+"'"
    res1=db.selectOne(qry1)
    return render_template('teacher/edit profile.html',data=res,data1=res1)


@app.route('/edit_profile_post', methods=['POST'])
def edit_profile_post():
    first_name = request.form['textfield']
    # last_name=request.form['textfield2']
    gender = request.form['textfield3']
    department = request.form['textfield4']
    Email = request.form['textfield5']
    phone_no = request.form['textfield7']
    place = request.form['textfield8']
    post = request.form['textfield9']
    pin = request.form['textfield10']

    photo = request.files['fileField']
    from datetime import datetime
    dt = datetime.now().strftime("%Y%m%d-%H%M%S")
    photo.save("C:\\Users\\USER\\PycharmProjects\\cloud_deduplication\\static\\teacher\\" + dt + ".jpg")
    path = "/static/teacher/" + dt + ".jpg"
    db=Db()
    qry="UPDATE `teacher` SET `name`='"+first_name+"',`gender`='"+gender+"',`phone_number`='"+phone_no+"',`place`='"+place+"',`post`='"+post+"',`pin`='"+pin+"',`email`='"+Email+"',`photo`='"+path+"', department_id='"+department+"' WHERE `login_id`='"+str(session['lid'])+"'"
    res=db.update(qry)
    return'''<script>alert(' Edited sucessfully');window.location='/view_profile' </script>'''

@app.route('/view_student')
def view_student():
    db = Db()
    qry="SELECT student.*,course.*,department.* FROM `student` JOIN `course` ON `student`.`course_id`=`course`.`course_id` JOIN `department` ON `course`.`department_id`=`department`.`department_id` JOIN `teacher` ON `teacher`.`department_id` =`department`.`department_id` "
        # "WHERE `teacher`.`login_id`='"+str(session['lid'])+"'"
    res = db.select(qry)
    return render_template("teacher/View student.html",data=res)


@app.route('/Upload_document')
def Upload_document():
    return render_template('teacher/Upload document.html')

@app.route('/Upload_document_post', methods=['POST'])
def Upload_document_post():
    Title=request.form['textfield']
    File=request.form['fileField']
    return render_template('teacher/Upload document.html')

@app.route('/view_file_list')
def view_file_list():
   return render_template('teacher/view file list.html')

@app.route('/send_notification')
def send_notification():
  return  render_template('teacher/Send notification.html')

@app.route('/send_notification_post', methods=['POST'])
def send_notification_post():
    notification=request.form['textarea']
    db=Db()
    qry="INSERT INTO `notification`(`notification`,`date`)VALUES('"+notification+"',curdate())"
    res=db.insert(qry)
    return '''<script> alert('notification sent');window.location='/send_notification'</script>'''


@app.route('/send_complaint')
def send_complaint():
    return render_template('teacher/Send complaint.html')


@app.route('/send_complaint_post', methods=['POST'])
def send_complaint_post():
     complaint=request.form['textarea']
     db=Db()
     qry="INSERT INTO `complaints`(`complaints`,`user_id`,`date`,`reply`,`status`)VALUES ('"+complaint+"','"+str(session['lid'])+"',CURDATE(),'pending','pending')"
     res=db.insert(qry)
     return'''<script>alert('complaint sent');window.location='/send_complaint'</script>'''

@app.route('/feedback')
def feedback():
    db=Db()
    qry="SELECT * FROM `feedback` JOIN `student`ON `feedback`.`user_id`=`student`.`login_id`"
    res=db.select(qry)
    return render_template('teacher/Feedback.html',data=res)

@app.route('/view_notification')
def view_notification():
    db=Db()
    qry="SELECT * FROM `notification`"
    res=db.select(qry)
    return render_template('teacher/view notification.html',data=res)
@app.route('/delete_notification/<id>')
def delete_notification(id):
    db=Db()
    qry="DELETE FROM `notification` WHERE `notification_id`='"+id+"'"
    res=db.delete(qry)
    return '''<script>alert("deleted");window.location='/view_notification'</script>'''



#######student




@app.route('/and_login', methods=['POST'])
def and_login():
    db=Db()
    username=request.form['user']
    password=request.form['password']
    qry="select * from login where username ='"+username+"' and password='"+password+"' and type = 'student'"
    res=db.selectOne(qry)
    if res is not None:
        return jsonify(status="ok",lid=res['login_id'],type=res['type'])
    else:
        return jsonify(status="not ok")

@app.route('/and_signup', methods=['POST'])
def and_signup():
    photo=request.form['photo']
    name=request.form['name']
    gender=request.form['gender']
    email=request.form['email']
    phone_number=request.form['phone_number']
    place=request.form['place']
    post=request.form['post']
    pin=request.form['pin']
    semester=request.form['semester']
    course=request.form['course']
    password=request.form['password']
    db = Db()
    import base64
    a = base64.b64decode(photo)
    from datetime import datetime
    dt = datetime.now().strftime("%Y%m%d-%H%M%S")+".jpg"
    with open(static_path+"\\student\\"+dt, "wb") as fs:
        fs.write(a)
    path="/static/student/"+dt
    qry = "INSERT INTO `login`(`username`,`password`,`type`)VALUES('" + email + "','" + password + "','student')"
    res = db.insert(qry)
    qry2 = "INSERT INTO `student`(`login_id`,`name`,`gender`,`email`,`place`,`post`,`pin`,`semester`,`phone_number`,`course_id`,`photo`)VALUES('"+str(res)+"','"+name+"','"+gender+"','"+email+"','"+place+"','"+post+"','"+pin+"','"+semester+"','"+phone_number+"','"+course+"','"+path+"')"
    res2=db.insert(qry2)
    return jsonify(status="ok")

@app.route('/and_courses_drop', methods=['POST'])
def and_courses_drop():
    db=Db()
    qry="SELECT * FROM `course`"
    res=db.select(qry)
    return jsonify(status="ok",data=res)

@app.route('/and_courses', methods=['POST'])
def and_courses():
    dept_id=request.form['dept_id']
    db=Db()
    qry="SELECT * FROM `course` where `department_id`='"+dept_id+"'"
    res=db.select(qry)
    return jsonify(status="ok",data=res)

@app.route('/and_department', methods=['POST'])
def and_department():
    db=Db()
    qry="SELECT * FROM `department`"
    res=db.select(qry)
    return jsonify(status="ok",data=res)

@app.route('/and_subject', methods=['POST'])
def and_subject():
    db=Db()
    crs_id=request.form['crs_id']
    qry="SELECT * FROM `subject` where course_id='"+crs_id+"'"
    res=db.select(qry)
    return jsonify(status="ok",data=res)

@app.route('/and_notification', methods=['POST'])
def and_notification():
    db=Db()
    qry="SELECT * FROM `notification`"
    res=db.select(qry)
    return jsonify(status="ok",data=res)

@app.route('/and_filelist', methods=['POST'])
def and_filelist():
    db=Db()
    lid=request.form['lid']
    qry="SELECT * FROM `student_upload`WHERE`student_id`='"+lid+"'"
    res=db.select(qry)
    return jsonify(status="ok",data=res)

@app.route('/and_view_profile', methods=['POST'])
def and_view_profile():
    lid=request.form['lid']
    db=Db()
    qry = "SELECT * FROM `student`JOIN `course` ON `student`.`course_id`=`course`.`course_id` WHERE `login_id`='" + lid + "'"
    print(qry)
    res=db.selectOne(qry)
    return jsonify(status="ok",data=res)

@app.route('/and_upload_assignment_seminar', methods=['POST'])
def and_upload_assignment_seminar():
    db=Db()
    file=request.form['file']
    lid=request.form['lid']
    assign_id=request.form['assign_id']
    qry="INSERT INTO `student_upload`(`assignment_id`,`file_name`,`date`,`student_id`)VALUES('"+assign_id+"','"+file+"',CURDATE(),'"+lid+"') "
    res=db.insert(qry)
    return jsonify(status="ok")

@app.route('/and_view_reply', methods=['POST'])
def and_view_reply():
    db=Db()
    lid=request.form['lid']
    qry="SELECT * FROM`complaints` WHERE user_id = '"+lid+"'"
    res=db.select(qry)
    return jsonify(status="ok",data=res)
    
@app.route('/and_send_complaint', methods=['POST'])
def and_send_complaint():
    db=Db()
    complaint=request.form['complaint']
    lid=request.form['lid']
    qry="INSERT INTO `complaints`(`complaints`,`user_id`,`date`,`reply`,`status`)VALUES('"+complaint+"','"+lid+"',CURDATE(),'pending','pending')"
    res=db.insert(qry)
    return jsonify(status="ok")

@app.route('/and_send_feedback', methods=['POST'])
def and_send_feedback():
     db=Db()
     feedback=request.form['feedback']
     lid=request.form['lid']
     qry="INSERT INTO `feedback`(`feedback`,`date`,`action`,`user_id`)VALUES('"+feedback+"',CURDATE(),'pending','"+lid+"')"
     db.insert(qry)
     return jsonify(status="ok")


@app.route('/and_view_feedback', methods=['POST'])
def and_view_feedback():
    lid=request.form['lid']
    db=Db()
    qry="SELECT * FROM `feedback` WHERE user_id = '"+lid+"'"
    res=db.select(qry)
    return jsonify(status="ok",data=res)

@app.route('/and_edit_profile', methods=['POST'])
def and_edit_profile():
        photo=request.form['Photo']
        Name=request.form['Name']
        Gender=request.form['Gender']
        Email=request.form['Email']
        Phone_number=request.form['Phone_number']
        Place=request.form['Place']
        Post=request.form['Post']
        Pin=request.form['Pin']
        Semester=request.form['Semester']
        Course=request.form['Course']
        lid=request.form['lid']
        db=Db()
        if len(photo)>1:
            import base64
            a = base64.b64decode(photo)
            from datetime import datetime
            dt = datetime.now().strftime("%Y%m%d-%H%M%S")+".jpg"
            with open(static_path+"\\student\\"+dt, "wb") as fs:
                fs.write(a)
            path="/static/student/"+dt
            qry="UPDATE `student` SET `photo`='"+path+"' WHERE `login_id`='"+lid+"'"
            res=db.update(qry)
        qry="UPDATE `student` SET `name`='"+Name+"',`gender`='"+Gender+"',`phone_number`='"+Phone_number+"',`place`='"+Place+"',`post`='"+Post+"',`pin`='"+Pin+"',`email`='"+Email+"', course_id='"+Course+"', semester='"+Semester+"' WHERE `login_id`='"+str(session['lid'])+"'"
        res=db.update(qry)
        return jsonify(status="ok")

#-------------------------------
if __name__ == '__main__':
    app.run(debug=True, port=4000, host='0.0.0.0')
