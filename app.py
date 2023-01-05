import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sumof1plus1'

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_student(ID):
    conn = get_db_connection()
    students = conn.execute('SELECT * FROM students WHERE stud_ID = ?', (ID,)).fetchone()
    conn.close()
    if students is None:
        abort(404)
    return students

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/students')
def view():
    conn = get_db_connection()
    students = conn.execute('SELECT * FROM students').fetchall()
    conn.close()
    return render_template('view.html', students=students)

@app.route('/<int:ID>')
def student(ID):
    student = get_student(ID)
    return render_template('student.html', student=student)

@app.route('/add', methods=('GET', 'POST'))
def add():
    if request.method == 'POST':
        firstName = request.form['first-name']
        middleName = request.form['middle-name']
        lastName = request.form['last-name']
        dateofBirth = request.form['dob']
        course = request.form['course']
        yearLevel = request.form['year']
        email = request.form['email']
        contact = request.form['contact']
        address = request.form['address']
        
        if not firstName:
            flash('First name is required.')
        elif not lastName:
            flash('Last name is required.')
        elif not email:
            flash('Date of Birth is required.')
        elif not course:
            flash('Course is required.')
        elif not yearLevel:
            flash('Year level is required.')
        elif not email:
            flash('Email is required.')
        elif not contact:
            flash('Contact is required.')
        elif not address:
            flash('Address is required.')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO students (stud_fname,stud_mname,stud_lname,stud_dob,stud_course,stud_year,stud_email,stud_contact,stud_address) VALUES (?,?,?,?,?,?,?,?,?)', (firstName,middleName, lastName,dateofBirth,course,yearLevel,email,contact,address))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/<int:ID>/edit', methods=('GET','POST'))
def edit(ID):
    student = get_student(ID)
    if request.method == 'POST':
        firstName = request.form['first-name']
        middleName = request.form['middle-name']
        lastName = request.form['last-name']
        dob = request.form['dob']
        course = request.form['course']
        yearLevel = request.form['year']
        email = request.form['email']
        contact = request.form['contact']
        address = request.form['address']

        if not firstName:
            flash('First name is required.')
        elif not lastName:
            flash('Last name is required.')
        elif not course:
            flash('Course is required.')
        elif not yearLevel:
            flash('Year level is required.')
        elif not email:
            flash('Year level is required.')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE students SET stud_fname = ?, stud_mname = ?, stud_lname = ?, stud_dob = ?, stud_course = ?, stud_year = ?, stud_email = ?, stud_contact = ?, stud_address = ? WHERE stud_ID = ?', (firstName, middleName, lastName, dob, course, yearLevel, email,contact,address, ID))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
        
    return render_template('edit.html', student=student)
            
@app.route('/<int:ID>/delete', methods=('POST',))
def delete(ID):
    student = get_student(ID)
    conn = get_db_connection()
    conn.execute('DELETE FROM students WHERE stud_id = ?', (ID,))
    conn.commit()
    conn.close()
    studentName = student['stud_fname'] + ' ' + student['stud_mname'] + ' ' + student['stud_lname'] 
    flash('Student "{}" was successfully deleted!'.format(student['stud_fname']))
    return redirect(url_for('index'))
    
@app.route('/about-us')
def about():
    return render_template('about.html')
    
if __name__ == '__main__':
    app.run(host='localhost', debug=True)
