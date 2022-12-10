from flask import current_app as app
from flask import redirect, render_template, url_for, request, flash

from .forms import *
from .functions import *


#@app.route("/", methods=['GET', 'POST'])
@app.route("/", methods=['GET', 'POST'])
def user_options():
    
    form = UserOptionForm()
    if request.method == 'POST' and form.validate_on_submit():
        option = request.form['option']

        if option == "1":
            return redirect('/admin')
        else:
            return redirect("/reservations")
    
    return render_template("options.html", form=form, template="form-template")

@app.route("/admin", methods=['GET', 'POST'])
def admin():

    form = AdminLoginForm()

    err = None
    seating_chart = None

    if request.method == 'POST' and form.validate_on_submit():
        username = request.form['username']
        password = request.form['password']
        
        if validate_user(username, password):
            seating_chart = "There's gonna be a seating chart here trust me"
            
            # CODE FOR SEATING CHART AND TOTAL SALES:
            #########################################

            # - Use the reservations.py file and the cost matrix code to generate seating chart and total sales/cost
            # - Code can be developed here to ensure it's working, but should ideally be formatted in functions in the functions.py file for organization and clarity

            #########################################


        else:
            err = "User does not exist."

    return render_template("admin.html", form=form, template="form-template", err = err, seating_chart = seating_chart)

@app.route("/reservations", methods=['GET', 'POST'])
def reservations():

    form = ReservationForm()

    return render_template("reservations.html", form=form, template="form-template")

