from flask import Flask, jsonify, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models import db, Message, Group, Member
from flask_migrate import Migrate
from ntplib import NTPClient
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)
ntp_client = NTPClient()

def get_ntp_time():
    response = ntp_client.request('pool.ntp.org', version=4)
    return datetime.utcfromtimestamp(response.tx_time)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pseudo = request.form['pseudo']
        message_content = request.form['content']
        conversation_id = request.form['group']
        ip_address = request.remote_addr
        timestamp = get_ntp_time()

        message = Message(pseudo=pseudo, content=message_content, group_id=conversation_id, ip_address=ip_address, timestamp=timestamp)
        db.session.add(message)
        db.session.commit()

        return redirect(url_for('index', group=conversation_id))

    all_groups = Group.query.all()
    conversation_id = request.args.get('group')

    messages = []
    if conversation_id:
        messages = Message.query.filter_by(group_id=conversation_id).order_by(Message.timestamp.asc()).all()

    return render_template('index.html', messages=messages, groups=all_groups, conversation_id=conversation_id)

@app.route('/group', methods=['GET', 'POST'])
def group():
    if request.method == 'POST':
        group_name = request.form['group_name']

        new_group = Group(name=group_name)
        db.session.add(new_group)
        db.session.commit()

    all_groups = Group.query.all()

    return render_template('group.html', groups=all_groups)

@app.route('/get_groups', methods=['GET'])
def get_groups():
    all_groups = Group.query.all()
    groups_data = [{'id': group.id, 'name': group.name} for group in all_groups]
    return jsonify(groups_data)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='192.168.70.34', port=5000)
