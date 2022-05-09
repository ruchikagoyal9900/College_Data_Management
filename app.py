import mysql.connector
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def home_view():
    return render_template('index.html')


@app.route('/student')
def student_view():
    return render_template('student.html')


@app.route('/student/detail', methods=['POST'])
def student_detail_view():
    if request.method == "POST":
        reg_no = request.form.get("register_no")
        result = view_student_record({'reg_no': reg_no})
        s = ""
        for i in result:
            s = s + str(i)
        return s


@app.route('/student/add', methods=['POST'])
def student_add_view():
    if request.method == "POST":
        reg_no = request.form.get("add_reg_no")
        name = request.form.get("add_stud_name")
        email = request.form.get("add_stud_email")
        num = request.form.get("add_stud_num")
        add = request.form.get("add_stud_add")
        result = view_student_record(
            {'reg_no': reg_no, 'name': name, 'email': email, 'num': num, 'add': add})
        s = ""
        for i in result:
            s = s + str(i)
        return s


@app.route('/student/delete', methods=['POST'])
def student_delete_view():
    if request.method == "POST":
        reg_no = request.form.get("delete_reg_no")
        result = view_student_record({'reg_no': reg_no})
        s = ""
        for i in result:
            s = s + str(i)
        return s


@app.route('/student/fee', methods=['POST'])
def student_fee_view():
    if request.method == "POST":
        reg_no = request.form.get("fee_reg_no")
        result = view_student_record({'reg_no': reg_no})
        s = ""
        for i in result:
            s = s + str(i)
        return s


@app.route('/student/subject', methods=['POST'])
def student_subject_view():
    if request.method == "POST":
        reg_no = request.form.get("sub_reg_no")
        id = request.form.get("sub_id")
        name = request.form.get("sub_name")
        facID = request.form.get("sub_fac_id")
        result = view_student_record(
            {'reg_no': reg_no, 'name': name, 'id': id, 'facID': facID})
        s = ""
        for i in result:
            s = s + str(i)
        return s


@app.route('/faculty')
def faculty_view():
    return render_template('faculty.html')

#     # Creating connection object
# mydb = mysql.connector.connect(
# 	host = "localhost",
# 	user = "root",
# 	password = "Ac$giesc2001"
# )

# cursor = mydb.cursor()
# cursor.execute("use College_data;")

# def student_record_add(val):
# 	sql='''INSERT INTO STUDENT VALUES(%s, %s, %s, %s, %s);'''
# 	cursor.execute(sql, val)

# def student_record_delete(val):
# 	sql='''DELETE FROM STUDENT WHERE reg_no=%s;'''
# 	cursor.execute(sql, val)

# def view_student_record(x):
# 	sql='''select * from student where reg_no=%(reg_no)s;'''
# 	cursor.execute(sql, {'reg_no': x})
# 	result= cursor.fetchall()
# 	return result

# def view_student_fee_details(val):
# 	sql='''select * from fees_details where reg_no=%s;'''
# 	cursor.execute(sql, val)
# 	result= cursor.fetchall()
# 	return result

# def subject_add(val):
# 	sql='''INSERT INTO SUBJECT_LIST VALUES(%s, %s, %s, %s);'''

# def faculty_record_add(val):
# 	sql='''INSERT INTO FACULTY VALUES(%s, %s, %s, %s, %s);'''
# 	cursor.execute(sql, val)

# def faculty_record_delete(val):
# 	sql='''DELETE FROM STUDENT WHERE ID=%s;'''
# 	cursor.execute(sql, val)

# def view_faculty_record(val):
# 	sql='''select * from faculty where ID=%s;'''
# 	cursor.execute(sql, val)
# 	result= cursor.fetchall()
# 	return result


def student_record_add(val):
    return 'ok'


def student_record_delete(val):
    return 'ok'


def view_student_record(x):
    return 'ok'


def view_student_fee_details(val):
    return 'ok'


def subject_add(val):
    return 'ok'


def faculty_record_add(val):
    return 'ok'


def faculty_record_delete(val):
    return 'ok'


def view_faculty_record(val):
    return 'ok'
