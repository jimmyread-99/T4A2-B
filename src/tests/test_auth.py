import unittest
from main import create_app, db


class TestAuthMoodApp(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.app = create_app()
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        cls.client = cls.app.test_client()

        db.create_all()

        runner = cls.app.test_cli_runner()
        runner.invoke(args=["db", "seed"])

    @classmethod
    def tearDown(cls):
        db.session.remove()
        db.drop_all()
        cls.app_context.pop()

    def test_home(self):
        response = self.client.get("/")
        self.assertIn("Murrumbeena Tennis Club", str(response.data))
        self.assertEqual(response.status_code, 200)

    def test_sign_up(self):
        response = self.client.post('/signup', data={
            'email': 'test55@test.com',
            'name': 'Test User',
            'password': '123456'
        })
        self.assertEqual(response.status_code, 302)

    def test_log_in(self):
        response = self.client.post('/signup', data={
            'email': 'test55@test.com',
            'name': 'Test User',
            'password': '123456'
        })
        self.assertEqual(response.status_code, 302)

        response = self.client.post('/login', data={
            'email': 'test55@test.com',
            'password': '123456'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_log_in_page(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)

    def test_signup_page(self):
        response = self.client.get('/signup')
        self.assertEqual(response.status_code, 200)

    def test_log_in_incorrect(self):
        response = self.client.post('/signup', data={
            'email': 'test55@test.com',
            'name': 'Test User',
            'password': '123456'
        })
        self.assertEqual(response.status_code, 302)

        response = self.client.post('/login', data={
            'email': 'test55@test.com,
            'password': '1123456'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_sign_up_twice(self):
        response = self.client.post('/signup', data={
            'email': 'test55@test.com',
            'name': 'Test User',
            'password': '123456'
        })

        response = self.client.post('/signup', data={
            'email': 'test55@test.com',
            'name': 'Test User',
            'password': '123456'
        })

        self.assertEqual(response.status_code, 200)

    def test_log_out(self):
        response = self.client.post('/signup', data={
            'email': 'test55@test.com',
            'name': 'Test User',
            'password': '123456'
        })
        self.assertEqual(response.status_code, 302)

        response = self.client.post('/login', data={
            'email': 'test55@test.com',
            'password': '123456'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/logout')
        self.assertEqual(response.status_code, 302)