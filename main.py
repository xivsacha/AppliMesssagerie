from flask import Flask, redirect, request, render_template, url_for
from config import db
from models import Message
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pseudo = request.form['pseudo']
        ip_address = request.remote_addr
        message_content = request.form['content']

        message = Message(pseudo=pseudo, content=message_content, ip_address=ip_address)
        db.session.add(message)
        db.session.commit()

        return redirect(url_for('index'))
    return render_template('index.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5001)
