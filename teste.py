from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        static_file = request.files['file']
        # here you can send this static_file to a storage service
        # or save it permanently to the file system
        static_file.save('./profilephoto.png')

@app.route('/')
def home():
   return render_template('upload.html')

if __name__ == '__main__':
   app.run(debug = False)
