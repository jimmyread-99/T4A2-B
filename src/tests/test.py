import unittest                                                        
from main import create_app, db                                        
from models.User import User
                              

class TestProfiles(unittest.TestCase):                                     
    @classmethod
    def setUp(cls):                                                     
        cls.app = create_app()                                          
        cls.app_context = cls.app.app_context()                         
        cls.app_context.push()                                          
        cls.client = cls.app.test_client()                              
        db.create_all()                                                 
        runner = cls.app.test_cli_runner()
        runner.invoke(args=["db-custom", "seed"])                       

    @classmethod                                                        
    def tearDown(cls):                                                  
        db.session.remove()                                             
        db.drop_all()                                                   
        cls.app_context.pop()                                           

   
    def test_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_how_to_play_page(self):
        response = self.client.get('/play')
        self.assertEqual(response.status_code, 200)

    def test_calendar_page(self):
        response = self.client.get('/calendar')
        self.assertEqual(response.status_code, 200)

    def test_memberships_page(self):
        response = self.client.get('/memberships')
        self.assertEqual(response.status_code, 200)

    def test_contact_page(self):
        response = self.client.get('/contact')
        self.assertEqual(response.status_code, 200)

    def test_about_page(self):
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)

    def test_date_page(self):
        response = self.client.get('//date')
        self.assertEqual(response.status_code, 200)

    def test_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)