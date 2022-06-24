# you need to import from the app
# you need to import the following from flask to render, redirect, request, session, and flash. <--- anything that controls what the front-end user will see or go to.
# you will need to import your model associated with the controller.

from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.models.login_and_reg_model import User
from flask_bcrypt import Bcrypt


bcrypt = Bcrypt(app)


# ####################
# Displays
# ####################


@app.route("/")
def home():

    # ####################
    # Route guard
    # ####################

    if 'user_id' in session:
        return redirect("/dashboard")

    return render_template("reg.html")



# ####################
# Redirects
# ####################


@app.route("/register/user", methods=['POST'])
def register():

    if not User.validate_reg(request.form):
        return redirect("/")

    pw_hash = bcrypt.generate_password_hash(request.form['pw'])
    print(pw_hash)

    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'pw' : pw_hash,
        'role' : 0
    }

    user_in_db = User.create(data)
    session['user_id'] = user_in_db
    session['user_role'] = data['role']

    return redirect("/")


@app.route("/login", methods=["POST"])
def login():

    data = {'email' : request.form['email'] }
    user_in_db = User.get_one_email(data)


    if not user_in_db:
        flash("Invalid Email/Password", "err_log")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.pw, request.form['pw']):
        flash("Invalid Email/Password", "err_log")
        return redirect("/")
    
    session['user_id'] = user_in_db.id
    session['user_role'] = user_in_db.role

    return redirect("/dashboard")
