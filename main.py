from flask import Flask, render_template, request,redirect,url_for,Response
from income import app
import sqlite3
import matplotlib.pyplot as plt
import io
DATABASE="database_income.db"


@app.route("/")
def index():
    con=sqlite3.connect(DATABASE)
    db_jobs=con.execute("SELECT * FROM jobs").fetchall()
    con.close()

    jobs=[]
    for row in db_jobs:
        jobs.append({'name':row[0],'yph':row[1]})

    return render_template("mypage.html",jobs=jobs)

@app.route("/record")
def record():
    con=sqlite3.connect(DATABASE)
    db_jobs=con.execute("SELECT * FROM jobs").fetchall()
    con.close()

    jobs=[]
    for row in db_jobs:
        jobs.append({'id':row[0],'name':row[1],'yph':row[2]})
    return render_template("record.html",jobs=jobs)

@app.route("/overview")
def overview():
    con=sqlite3.connect(DATABASE)
    jobs=[]
    db_jobs=con.execute("SELECT * FROM jobs").fetchall()
    for row in db_jobs:
        job_id=row[0]

        #合計時間
        total_time=con.execute("SELECT SUM(time) FROM worktimes WHERE job_id=?",(job_id,)).fetchone()[0]
        if total_time is None:
            total_time=0

        jobs.append({'id':row[0],'name':row[1],'yph':row[2],'total_time':total_time})
    
    return render_template("overview.html", jobs=jobs)

@app.route("/graph_showpage/<int:id>", methods=["POST"])
def graph_showpage(id):
    con=sqlite3.connect(DATABASE)
    job=con.execute("SELECT * FROM jobs WHERE id = ?",(id,)).fetchone()
    db_worktimes=con.execute("SELECT * FROM worktimes WHERE job_id=? ORDER BY year, month, day",(id,)).fetchall()
    con.close()

    worktimes=[]
    for row in db_worktimes:
        worktimes.append({'id':row[0],'job_id':row[1],'time':row[2],'year':row[3],'month':row[4],'day':row[5],'hour':row[6],'minute':row[7]})
    
    

    return render_template("graph_showpage.html", job=job, worktimes=worktimes)

    
@app.route("/add_job")
def add_job():
    return render_template("add_job.html")

@app.route("/add_job", methods=["POST"])
def addjob():
    name=request.form["name"]
    yph=request.form["yph"]
    
    con=sqlite3.connect(DATABASE)
    con.execute("INSERT INTO jobs (name,yph) VALUES (?,?)",(name,yph))
    con.commit()
    con.close()

    return redirect(url_for('record'))

@app.route("/record_time/<int:id>",methods=["POST","GET"])
def record_time(id):
    con=sqlite3.connect(DATABASE)
    job=con.execute("SELECT * FROM jobs WHERE id = ?",(id,)).fetchone()
    db_worktime=con.execute("SELECT * FROM worktimes WHERE job_id = ?",(id,)).fetchall()
    con.close()

    worktimes=[]
    for row in db_worktime:
        worktimes.append({'id':row[0], 'job_id':row[1],'time':row[2],'year':row[3],'year':row[3],'month':row[4],'day':row[5],'hour':row[6],'minute':row[7]})


    return render_template("record_time.html", job=job, worktimes=worktimes)

@app.route("/recordtime/<int:id>",methods=["POST"])
def recordtime(id):
    year=request.form["year"]
    month=request.form["month"]
    day=request.form["day"]
    hour=request.form["hour"]
    minute=request.form["minute"]
    
    time=int(hour)+int(minute)/60

    con=sqlite3.connect(DATABASE)
    con.execute("INSERT INTO worktimes (job_id,time,year,month,day,hour,minute) VALUES (?,?,?,?,?,?,?)",(id,time,year,month,day,hour,minute))
    con.commit()
    con.close()

    return redirect(url_for("record_time",id=id))

@app.route("/delete_job/<int:id>",methods=["POST"])
def delete_job(id):
    con=sqlite3.connect(DATABASE)
    con.execute("DELETE FROM jobs WHERE id=?",(id,))
    con.execute("DELETE FROM worktimes WHERE job_id=?",(id,))
    con.commit()
    con.close()

    return redirect(url_for('record'))

@app.route("/delete_worktime/<int:id>",methods=["POST"])
def delete_worktime(id):    
    con=sqlite3.connect(DATABASE)
    worktime=con.execute("SELECT job_id FROM worktimes WHERE id = ?",(id,)).fetchone()
    job_id=worktime[0]
    con.execute("DELETE FROM worktimes WHERE id=?",(id,))
    con.commit()
    con.close()

    return redirect(url_for('record_time',id=job_id))


if __name__ == "__main__":
    app.run(debug=True)