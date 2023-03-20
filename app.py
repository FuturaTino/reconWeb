from flask import Flask, render_template, request
import os

app = Flask(__name__)

# 配置上传文件的存储路径
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 允许上传的文件类型
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # 检查是否有文件
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']

        # 检查文件是否为空
        if file.filename == '':
            return 'No selected file'

        # 检查文件类型是否允许
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return 'File uploaded successfully'
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
