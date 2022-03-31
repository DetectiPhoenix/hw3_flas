from app import myapp_obj
from app.forms import LoginForm
from flask import render_template, flash, request

name = "Lisa"
city_names = ["Paris", "London", "Rome", "Tahiti"]

@myapp_obj.route("/", methods = ["POST", "GET"])
def home():
	form = LoginForm()

	if request.method == "POST":
		flash(request.form["cityName"])

	return render_template("home.html", name=name, city_names=city_names, form=form)
