import unittest
from app import create_app, db
from app.models import ContactSubmission

class RouteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = create_app('testing')  # Use the testing configuration
        cls.client = cls.app.test_client()
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        db.create_all()

    @classmethod
    def tearDownClass(cls):
        db.drop_all()
        cls.app_context.pop()

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Home', response.data)

    def test_about(self):
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'About Us', response.data)

    def test_contact_form(self):
        response = self.client.post('/contact', data={
            'name': 'Jane Doe',
            'email': 'jane.doe@example.com',
            'message': 'Test message'
        }, follow_redirects=True)

        # Check if the response is redirected to /submissions
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Contact Submissions', response.data)

        # Verify form data is saved
        submission = ContactSubmission.query.filter_by(name='Jane Doe').first()
        self.assertIsNotNone(submission)
        self.assertEqual(submission.email, 'jane.doe@example.com')
        self.assertEqual(submission.message, 'Test message')

    def test_submissions(self):
        response = self.client.get('/submissions')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Contact Submissions', response.data)

    def test_profile(self):
        response = self.client.get('/profile')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Profile', response.data)

    def test_404(self):
        response = self.client.get('/nonexistent')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'Not Found', response.data)

if __name__ == '__main__':
    unittest.main()
