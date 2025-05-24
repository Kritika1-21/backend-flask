#import the flask module
from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

print("this is is a project which is using the tkinter")
#let see the content of flsk module


#let us creet an object 
app=Flask(__name__)

print(__name__)
# Ensure instance directory exists


# SQLite database ko instance folder mein rakhne ke liye proper config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////task.db'

# creating an object of sqlalchemy
database=SQLAlchemy(app)

class Task(database.Model):

    sno=database.Column(database.Integer,primary_key=True)
    tasktitle=database.Column(database.String(100),nullable=False)
    taskdescription=database.Column(database.String(200),nullable=False)




# let us creta an first route
@app.route('/',methods=["GET","POST"])
def index():

    # print(request.form)

    # let check the request is get or post
    # if request is post
    # then fetch the title and description
    # add to the database

    if request.method=="POST":
        task_title=request.form.get('title')
        task_description=request.form.get('description')
        # print(tasktitle,taskdescription)

        # add it to the database
        task=task(tasktitle=task_title,taskdescription=task_description)
        database.session(task)
        database.session.commit()

    #     pass

    return render_template('index.html')


# let us creta an second route
@app.route('/contact')
def contact():
    return render_template('contact.html')
    


# let us creta an third route
@app.route('/about')
def about():
    return render_template('about.html')
app.run(debug=True,host='0.0.0.0')










