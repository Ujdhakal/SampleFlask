import unittest
from app import create_app, db
from app.models import ContactSubmission

class ModelTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = create_app()
        cls.app.config['TESTING'] = True
        cls.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        cls.client = cls.app.test_client()
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        db.create_all()

    @classmethod
    def tearDownClass(cls):
        db.drop_all()
        cls.app_context.pop()

    def test_contact_submission(self):
        submission = ContactSubmission(name='John Doe', email='john.doe@example.com', message='Hello!')
        db.session.add(submission)
        db.session.commit()

        retrieved = ContactSubmission.query.first()
        self.assertEqual(retrieved.name, 'John Doe')
        self.assertEqual(retrieved.email, 'john.doe@example.com')
        self.assertEqual(retrieved.message, 'Hello!')

if __name__ == '__main__':
    unittest.main()
