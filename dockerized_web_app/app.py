from flask import Flask, request, render_template, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)


client = MongoClient(host='test_mongodb', port=27017,
                    username='root', password='pass', authSource="admin")
db = client.mytododb
students_collection = db.students

departments = ["Computer Science", "Software Engineering", "Data Science", "Information Technology"]
universities = ["Addis Ababa University", "Adama Science and Technology", "Addis Ababa Science and Technology"]

@app.route('/')
def home():
    students = students_collection.find()
    return render_template('index.html', students=students, departments=departments, universities=universities)

@app.route('/add_student', methods=['POST'])
def add_student():
    if request.method == 'POST':
        student_data = {
            'name': request.form['name'],
            'campus_id': request.form['campus_id'],
            'department': request.form['department'],
            'university': request.form['university']
        }
        students_collection.insert_one(student_data)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
