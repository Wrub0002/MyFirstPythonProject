from flask import Flask, render_template, request, redirect, url_for
from models.bussines_logic import records, add_new_record, edit_new_record , delete_record , save_data, load_records_from_csv

app = Flask(__name__)

@app.route('/')
def index():
    loaded_records  = load_records_from_csv('data/new_data.csv')
    return render_template('index.html', records=loaded_records)


@app.route('/add', methods=['GET', 'POST'])
def add():
    """Route to add a new record."""
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        city = request.form['city']

        if not name or not age or not city:
            return "All fields are required", 400

        add_new_record(name, age, city)
        save_data()

        return redirect(url_for('index'))

    return render_template('add.html')


@app.route('/edit/<name>', methods=['GET', 'POST'])
def edit(name):
    """Route to edit an existing record."""
    record = next((rec for rec in records if rec.get_name() == name), None)

    if not record:
        return "Record not found", 404

    if request.method == 'POST':
        new_name = request.form['name']
        new_age = request.form['age']
        new_city = request.form['city']

        if not new_name or not new_age or not new_city:
            return "All fields are required", 400


        edit_new_record(name, new_name, new_age, new_city)
        save_data()
        return redirect(url_for('index'))

    return render_template('edit.html', record=record)


@app.route('/delete/<name>')
def delete(name):
    """Route to delete a record."""
    delete_record(name)
    save_data()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)