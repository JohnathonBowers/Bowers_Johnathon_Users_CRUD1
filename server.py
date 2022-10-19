from flask import Flask, render_template, request, redirect

from user import User

app = Flask(__name__)
@app.route('/')
def home():
    print("Redirecting to Users Page")
    return redirect('/users')

@app.route('/users')
def users():
    print("Showing All Users")
    users = User.get_all()
    return render_template("all_users.html", users = users)

@app.route('/users/add')
def add():
    print("Showing New User Form")
    return render_template("new_user_form.html")

@app.route('/users/input', methods=['POST'])
def input():
    print("Got Post Info")
    User.save(request.form)
    print(request.form)
    return redirect('/users')

@app.route('/users/destroy/<int:id>')
def destroy(id):
    print("Ready to Destroy")
    dictionary = {'id':id}
    User.delete(dictionary)
    return redirect('/users')

@app.route('/users/show/<int:id>')
def show(id):
    print ("Ready to Show")
    dictionary = {'id':id}
    user = User.show_one(dictionary)
    return render_template("show_user.html", user = user, id = id)

@app.route('/users/edit/<int:id>')
def exhibit(id):
    print ("Ready to Edit")
    dictionary = {'id':id}
    user = User.show_one(dictionary)
    return render_template("edit_user.html", user = user, id = id)

@app.route('/users/update', methods=['POST'])
def update():
    print ("Got Update Info")
    User.update(request.form)
    print(request.form)
    return redirect ('/users')

if __name__ == "__main__":
    app.run(debug=True, port=5001)