from bottle import Bottle, template, request

app = Bottle()
users = [{"ajax1234":"zorro"}]

username = None
password = None
@app.route('/')
def index():
   data = {"to_display":"HI, how are you"}
   return template("simple.html", to_display = "HI, how are you?")

@app.route('/run_code', method = "POST")
def get_code():
    full_code = request.forms.get('code')
    print full_code

if __name__ == '__main__':
    app.run()
