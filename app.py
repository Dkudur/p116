from flask import Flask , render_template

app = Flask(__name__)



@app.route("/")
def home():

    name = "Aniket" 
    age = "15" 

    return render_template('index.html' , name = name , age = age)


@app.route("/father")
def father():
    name = "Dharaneesh"
    age = "42"

    return render_template('father.html' , name = name , age = age)


@app.route("/mother")
def mother():
    name = "Arundhaty"
    age = "37"

    return render_template('mother.html', name = name, age = age)


@app.route("/friends")
def friends():
    name = "Sam"
    age = "15"

    return render_template('friends.html', name = name, age = age)






# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
