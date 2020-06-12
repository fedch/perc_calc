from flask import Flask, render_template, request, jsonify
from models.model import InputForm1, InputForm2
from models.percentage import Percentage

app = Flask(__name__)
app.secret_key = "asdgfartf"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/increase', methods=['GET', 'POST'])
def increase():
    form = InputForm1(request.form)
    if request.method == 'POST' and form.validate():
        result = Percentage.increase_function(form.x.data, form.y.data)
    else:
        result = None

    return render_template('increase.html',
                           form=form, result=result)

@app.route('/relative_perc', methods=['GET', 'POST'])
def relative_perc():
    form = InputForm1(request.form)
    if request.method == 'POST' and form.validate():
        result = Percentage.one_of_the_other_function(form.x.data, form.y.data)
    else:
        result = None

    return render_template('relative_perc.html',
                           form=form, result=result)

@app.route('/gst_calculator', methods=['GET', 'POST'])
def gst_calculator():
    form = InputForm2(request.form)
    if request.method == 'POST' and form.validate():
        if '+' in request.form:
            print(request.form)
            #result = Percentage.gst_sub_function(form.x.data, form.y.data)
        if '-' in request.form:
            result = Percentage.add_function(form.x.data, form.y.data)
    else:
        result = None



        return render_template('gst.html',
                           form=form, result=result)

if __name__ == '__main__':
    app.debug = True
    app.run(port=5000, debug=True)
