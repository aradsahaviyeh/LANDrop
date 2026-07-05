from flask import Flask, request, redirect, render_template, session, url_for, send_from_directory
from werkzeug.utils import secure_filename
import secrets
import os

app = Flask(__name__)
app.secret_key = 'my-secret-key'

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        room = request.form.get('room')

        if not room:
            return render_template('index.html', error='اسم روم را وارد کنید')

        room_path = os.path.join(UPLOAD_FOLDER, room)
        os.makedirs(room_path, exist_ok=True)

        return redirect(url_for('room', title=room))

    return render_template('index.html')


@app.route('/room/<title>/', methods=['GET', 'POST'])
def room(title):
    room_path = os.path.join(UPLOAD_FOLDER, title)
    os.makedirs(room_path, exist_ok=True)

    if request.method == 'POST':
        file = request.files.get('file')
        title = request.form.get('title')
        if file and file.filename:
            name, ext = os.path.splitext(file.filename)
            name = title if title else name
            file_name = f'{name}_{secrets.token_hex(8)}{ext}'
            file.save(os.path.join(room_path, file_name))

        return redirect(url_for('room', title=title))

    files = os.listdir(room_path)
    return render_template('room.html', title=title, files=files)


@app.route('/room/<title>/download/<filename>')
def downloaded_file(title, filename):
    secure_title = secure_filename(title)
    secure_name = secure_filename(filename)

    room_path = os.path.join(UPLOAD_FOLDER, secure_title)

    return send_from_directory(room_path, secure_name, as_attachment=True)
