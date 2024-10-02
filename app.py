from flask import Flask,render_template,request,redirect,url_for
import webbrowser
from bussiness_layer.bussines_logic import load_data, records, add_new_record, edit_new_record, delete_record

app = Flask(__name__)

load_data()

@app.route('/')
def index():
    return render_template('index.html', records = records)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        city = request.form['city']
        add_new_record()(name, age, city)
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<name>', methods=['GET','POST'])
def edit(name):
    if request.method == 'POST':
        new_name = request.form['name']
        new_age = request.form ['age']
        new_city = request.form['city']
        edit_new_record(name,new_name,new_age,new_city)
        return redirect(url_for('index'))
    return render_template('edit.html, record = name')

@app.route('/delete/<name>')
def delete(name):
    delete_record(name)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)