from flask import render_template,redirect,request,session
from flask_app import app
from flask_app.models.birthday_model import Birthday
from flask_app.models.login_and_reg_model import User

# ####################
# Displays
# ####################


@app.route("/dashboard")
def dashboard():
    # ####################
    # Route guard
    # ####################


    if not 'user_id' in session:
        return redirect("/")

    if session['user_role'] != User.get_one({'id': session['user_id']}).role:
        session.clear()
        return redirect("/logout")

    # ####################


    pendings = Birthday.get_all_pending()
    birthdays = Birthday.get_all_birthdays()
    
    return render_template("dashboard.html", pendings = pendings, birthdays = birthdays)


@app.route("/edit/<int:id>")
def edit_display(id):
    # ####################
    # Route guard
    # ####################


    if not 'user_id' in session:
        return redirect("/")

    if session['user_role'] != User.get_one({'id': session['user_id']}).role:
        session.clear()
        return redirect("/logout")
    
    if session['user_role'] != 1:
        return redirect("/")
    
    # ####################


    data = {
        'id' : id
    }

    info = Birthday.get_one_birthday(data)

    return render_template("edit.html", info = info)


# ####################
# Redirects
# ####################


@app.route("/logout")
def logout():
    # ####################
    # Route guard
    # ####################

    if not 'user_id' in session:
        return redirect("/")

    if session['user_role'] != User.get_one({'id': session['user_id']}).role:
        return redirect("/")
    
    session.clear()

    return redirect("/")



# ####################
# Pending
# ####################


@app.route("/process/approved/<int:id>", methods=['POST'])
def process_pending_approval(id):

    data = {
        'id' : id
    }

    pending_data = Birthday.get_one_pending(data)

    data_to_transfer = {
        'id' : pending_data.id,
        'handle' : pending_data.handle,
        'birthday' : pending_data.birthday,
    }

    Birthday.delete_pending(data)

    Birthday.create_birthday(data_to_transfer)
    

    return redirect("/dashboard")


@app.route("/process/new", methods=["POST"])
def process_new_birthdays():

    data = {
        'handle' : request.form['handle'],
        'birthday' : request.form['birthday'],
    }

    Birthday.create_pending(data)

    return redirect("/dashboard")


@app.route("/delete/pending/<int:id>", methods=["POST"])
def delete_pending(id):

    data = {
        'id' : id
    }

    Birthday.delete_pending(data)

    return redirect("/dashboard")


# ####################
# Approved
# ####################


@app.route("/delete/approved/<int:id>", methods=["POST"])
def delete_approved(id):

    data = {
        'id' : id
    }

    Birthday.delete_birthday(data)

    return redirect("/dashboard")


@app.route("/process/edit", methods=["POST"])
def process_edit():

    data = {
        'id' : request.form['i'],
        'handle': request.form['handle'],
        'birthday': request.form['birthday'],
    }

    Birthday.update_birthday(data)
    print("**********************")
    return redirect("/dashboard")


