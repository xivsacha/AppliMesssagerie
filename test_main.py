import unittest
from main import app, db, Group, Message

class TestApp(unittest.TestCase):

    def setUp(self):
        # Configure l'application Flask pour les tests
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  # Utilisation d'une base de données SQLite pour les tests
        self.app = app.test_client()
        self.db = db

        # Crée les tables dans la base de données de test
        with app.app_context():
            db.create_all()

    def tearDown(self):
        # Supprime les tables de la base de données de test
        with app.app_context():
            db.drop_all()

    def test_index_page(self):
        # Teste la page d'accueil '/'
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to the Chat App', response.data)

    def test_create_group(self):
        # Teste la création d'un groupe
        response = self.app.post('/group', data={'group_name': 'Test Group'})
        self.assertEqual(response.status_code, 200)
        group = Group.query.filter_by(name='Test Group').first()
        self.assertIsNotNone(group)

    def test_create_message(self):
        # Teste la création d'un message
        group = Group(name='Test Group')
        self.db.session.add(group)
        self.db.session.commit()

        response = self.app.post('/', data={'pseudo': 'Test User', 'content': 'Hello', 'group': group.id})
        self.assertEqual(response.status_code, 302)  # Redirection après l'envoi du message
        message = Message.query.filter_by(content='Hello').first()
        self.assertIsNotNone(message)

if __name__ == '__main__':
    unittest.main()
