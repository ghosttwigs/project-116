# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Charlie" # write your name
    age = "14" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def home():

    name = "Mac" # write your name
    age = "44" # write your age

    return render_template('index.html' , name = name , age = age)



# define the route to mother webpage
@app.route("/mother")
def home():

    name = "Marisa" # write your name
    age = "42" # write your age

    return render_template('index.html' , name = name , age = age)


# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
