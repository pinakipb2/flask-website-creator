from flask import Flask, render_template, flash, make_response, url_for, request, redirect
import os

app = Flask(__name__)
app.secret_key = 'poit,hino;ptnh/ps.ntgl'

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        try :
            basedir = request.form.get('directory')     #'C:\Users\John\Desktop'
            os.chdir(basedir)
            Foldername = request.form.get('foldername')      #'me'
            os.makedirs(Foldername)
            f = os.path.join(basedir, Foldername)
            os.chdir(f)
            templates = 'templates'
            os.makedirs(templates)
            static = 'static'
            os.makedirs(static)
            myapp = open('app.py','w')
            myapp.write("from flask import Flask, render_template, flash, make_response, url_for, request, redirect\n\napp = Flask(__name__)\n\n@app.route('/')\ndef index():\n    return render_template('index.html')\n\nif __name__ == '__main__':\n    app.run(debug=True)")
            myapp.close()
            f = os.path.join(f, templates)
            os.chdir(f)
            myapp = open('index.html','w')
            myapp.write("<!doctype html>\n<html lang=\"en\">\n  <head>\n    <!-- Required meta tags -->\n    <meta charset=\"utf-8\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1, shrink-to-fit=no\">\n\n    <!-- Bootstrap CSS -->\n    <link rel=\"stylesheet\" href=\"https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css\" integrity=\"sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T\" crossorigin=\"anonymous\">\n\n    <title>Hello, world!</title>\n  </head>\n  <body>\n    <h1>Hello, world!</h1>\n\n    <!-- Optional JavaScript -->\n    <!-- jQuery first, then Popper.js, then Bootstrap JS -->\n    <script src=\"https://code.jquery.com/jquery-3.3.1.slim.min.js\" integrity=\"sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo\" crossorigin=\"anonymous\"></script>\n    <script src=\"https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js\" integrity=\"sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1\" crossorigin=\"anonymous\"></script>\n    <script src=\"https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js\" integrity=\"sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM\" crossorigin=\"anonymous\"></script>\n  </body>\n</html>")
            myapp.close()
            flash('Your Flask Website has Successfully been Created!','success')
        except:
            flash('The Process Failed Due to Some Reason. Please Try Again!','error')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)