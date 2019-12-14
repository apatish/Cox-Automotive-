from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def home():
    from sqlquery.sqlquery import sql_query
    results = sql_query('''SELECT * FROM student_gpa''')
    msg = 'SELECT * FROM student_gpa'
    return render_template("index.html", results=results, msg=msg)

@app.route('/delete',methods = ['POST', 'GET']) #this is when user clicks delete link
def sql_datadelete():
    from sqlquery.sqlquery import sql_delete, sql_query
    if request.method == 'GET':
        student_id = request.args.get('student_id')
        sql_delete('''DELETE FROM student_gpa where student_id = ?''', [student_id] )
    return_url = request.referrer or '/'
    return redirect(return_url) 

@app.route('/edit',methods = ['POST', 'GET']) #this is when user submits an edit
def sql_dataedit():
    from sqlquery.sqlquery import sql_edit_insert, sql_query
    if request.method == 'POST':
        last_name = request.form['last_name']
        first_name = request.form['first_name']
        gpa = request.form['gpa']
        student_id = request.form['student_id']
        version = request.form['version']
        if len(last_name) and len(first_name) and len(gpa) and len(student_id): 
            sql_edit_insert(''' REPLACE INTO student_gpa (first_name,last_name,gpa, student_id, version) SELECT ?,?,?,?,? WHERE NOT EXISTS (SELECT * FROM student_gpa WHERE version = ? AND student_id = ?)''', (first_name,last_name,gpa,student_id,version,version,student_id) )
        results = sql_query(''' SELECT * FROM student_gpa''')
        msg = 'SELECT * FROM student_gpa'
        return render_template("index.html", results=results, msg=msg)
    eresult = {}
    eresult['last_name'] = request.args.get('last_name')
    eresult['first_name'] = request.args.get('first_name')
    eresult['gpa'] = request.args.get('gpa')
    eresult['student_id'] = request.args.get('student_id')
    return render_template('edit_student.html', eresult=eresult)

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)

if __name__ == "__main__":
    app.run(debug=True)
