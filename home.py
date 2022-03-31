from flask import Flask

myapp_obj = Flask(__name__)

name = "Lisa"
city_names = ["Paris", "London", "Rome", "Tahiti"]


@myapp_obj.route("/")
def home():

	city_string = ""
	for city in city_names:
		city_string += "<li>" + city + "</li>"

	return '''
	<html>
	<body>
		<h1>Welcome ''' + name + '''!</h1>
		<a href="https://www.google.com/">not google</a>
		<ul>''' + city_string + '''</ul>
	</body>
	</html>'''

#myapp_obj.run()
