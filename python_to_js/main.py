from bottle import Bottle, template

app = Bottle()

@app.route('/')
def index():
   data = {"to_display":"HI, how are you"}
   return template("bottle_javascript.html", data)

if __name__ == '__main__':
    app.run()
