from flask import Flask, redirect, request, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    pseudo = db.Column(db.String(50))
    ip_address = db.Column(db.String(15))

    def __repr__(self):
        return f'<Message {self.id}>'
    
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


@app.route('/messages')
def messages():
    all_messages = Message.query.order_by(Message.timestamp.asc()).all()
    return render_template('messages.html', messages=all_messages)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5001)
