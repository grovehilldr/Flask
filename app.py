from datetime import date
from urllib import request
from flask import Flask, render_template, request
import datetime

app = Flask(__name__)
# Append this value to studentOrganisationDetails
global studentOrganisationDetails
# Assign default 5 values to studentOrganisationDetails for Application  3.
studentOrganisationDetails = ['aa', 'bb', 'cc']

@app.get('/')
def index():
    # Complete this function to get current date and time assign this value to currentDate, display this data on index.html

    return render_template('index.html', currentDate = datetime.datetime.now().replace(microsecond=0).isoformat(' '))


@app.get('/calculate')
def displayNumberPage():
    # Complete this function to display form.html page
    return render_template('form.html')


@app.route('/result', methods=['POST'])
def checkNumber():
    # Get Number from form and display message according to number
    # Display "Number {Number} is even" if given number is even on result.html page
    
    # Display "Number {Number} is odd" if given number is odd on result.html page
    # Display "No number provided" if value is null or blank on result.html page
    # Display "Provided input is not an integer!" if value is not a number on result.html page
    global number
    number = request.form['number']
   
    # Write your to code here to check whether number is even or odd and render result.html page
    global oddEven
    if int(request.form['number']) % 2 == 0:
        oddEven = "is even"
        return render_template('result.html', number=number, oddEven = oddEven)
    else :
        oddEven = "is odd"
        return render_template('result.html', number=number, oddEven = oddEven)

@app.get('/addStudentOrganisation')
def displayStudentForm():
    # Complete this function to display studentFrom.html page

    return render_template('studentForm.html')


@app.route('/studentdetails', methods=['POST', 'GET'])
def displayRegistrationPage():
    # Get student name and organisation from form.
    global studentName
    global select
    if request.form.method == 'POST':
        studentName = request.form['studentName']
    elif request.form.method == 'GET':
        select = request.args.get("select")
        
    
   

    # Append this value to studentOrganisationDetails
 

    # Display studentDetails.html with all students and organisations
    return render_template('StudentDetails.html', studentName = studentName, select=select,studentOrganisationDetails=studentOrganisationDetails)