import unittest
from flask_jwt_extended import create_refresh_token, decode_token, create_access_token

from app import create_app
from app.config import TestConfig
from app.extensions import db
from app.models.user_model import UserModel
from app.models.position_model import PositionModel


class TestUserAuthView(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

        with self.app.app_context():
            db.create_all()
            
        self.position = PositionModel(title="TestPosition")
        db.session.add(self.position)
        db.session.commit()
        
        self.user = UserModel(name="TestUser", email="TestUser@example.com", 
                              cpf="12345678900", password="12345678", active=True,
                              admin=True, bot=False, position_id=1)
        self.user.encrypt_password()
        db.session.add(self.user)
        db.session.commit()
        
        self.refresh_token = create_refresh_token(self.user.id)
            
        
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()   
    
    def test_register_valid_user(self):
        response = self.client.post('/api/v1/user/register', json={
            'name': 'Test User',
            'email': 'test@example.com',
            'cpf': '12345678901',
            'password': 'test1234',
            'position_id': self.position.id
        })
        
        self.assertEqual(response.status_code, 201)
    
    def test_register_invalid_user(self):
        response = self.client.post('/api/v1/user/register', json={
            'name': '',
            'email': 'test@example.com',
            'cpf': '12345678901',
            'password': 'test1234',
            'position_id': self.position.id
        })
        
        self.assertEqual(response.status_code, 400)
        
    def test_login_valid_user(self):
        response = self.client.post('/api/v1/user/login', json={
            'cpf': '12345678900',
            'password': '12345678'
        })
        
        self.assertIn('access_token', response.json)
        self.assertEqual(200, response.status_code)
        
    def test_login_invalid_user(self):
        response = self.client.post('/api/v1/user/login', json={
            'cpf': '',
            'password': '12345678'
        })
        
        self.assertEqual(400, response.status_code)
        
    def test_refresh_user(self):
        headers = {"Authorization": f"Bearer {self.refresh_token}"}
        response = self.client.post('/api/v1/user/refresh', headers=headers)
        
        self.assertEqual(200, response.status_code)
        
    def test_roles_admin(self):
        access_token = create_access_token(self.user.id)
        roles = decode_token(access_token)['roles']
        self.assertEqual(roles, 'admin')

    def test_roles_bot(self):
        self.user.admin = False
        self.user.bot = True
        db.session.commit()
        access_token = create_access_token(self.user.id)
        roles = decode_token(access_token)['roles']
        self.assertEqual(roles, 'bot')
        
    def test_roles_user(self):
        self.user.active = False
        db.session.commit()
        access_token = create_access_token(self.user.id)
        roles = decode_token(access_token)['roles']
        self.assertEqual(roles, 'guest')
        
        
         