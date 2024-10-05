from flask import Flask

'''
it creates an instance of the flask class 
which will be your WSGI(web server gateway interface) application
'''

app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome Diwankar .Thanks"





if __name__=="__main__":
    app.run(debug=True)