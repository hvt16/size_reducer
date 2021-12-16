from flask import Flask, render_template, request, redirect
from pdf_size_reducer import compress_file

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

@app.route("/", methods=['GET','POST'])
def uploadfile():
    if request.method == 'GET':
        return render_template('uploadfile.html')
    if request.method ==  'POST':
        if 'file' not in request.files:
            print('no file uploaded')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == "":
            print('no file uploaded')
            return redirect(request.url)
        else:
            filepath = './static/file.pdf'
            file.save(filepath)
            compress_file(filepath, filepath)
            return redirect('/downloadfile')
    return redirect(request.url)

@app.route("/downloadfile", methods=['GET'])
def downloadfile():
    file = '/static/file.pdf'
    return render_template('downloadfile.html',file=file)

if __name__ == "__main__":
    app.run(debug=True)