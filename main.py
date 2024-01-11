from flask import Flask, redirect, request, render_template, url_for, jsonify
from models import Group, db, Message

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
        group_id = request.form.get('group')

        message = Message(pseudo=pseudo, content=message_content, ip_address=ip_address, group_id=group_id)
        db.session.add(message)
        db.session.commit()

        return redirect(url_for('index'))

    all_groups = Group.query.all()
    conversation_id = request.args.get('conversation_id')

    if conversation_id:
        messages = Message.query.filter_by(group_id=conversation_id).order_by(Message.timestamp.asc()).all()
    else:
        messages = []

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
    app.run(debug=True, port=5001)
