from flask import Flask, render_template
app = Flask(__name__)
import income.main
from income import db
db.create_jobs_table()
db.create_worktimes_table()