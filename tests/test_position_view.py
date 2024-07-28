import unittest
from flask_jwt_extended import create_access_token

from app import create_app
from app.config import TestConfig
from app.extensions import db
from app.models.user_model import UserModel
from app.models.position_model import PositionModel


class TestUserView(unittest.TestCase):
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
        
        self.access_token = create_access_token(identity=self.user.id)
        
        
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()    
    
    def test_get_position(self):
        headers = {'Authorization': f'Bearer {self.access_token}'}
        response = self.client.get('/api/v1/positions/1', headers=headers)
        self.assertEqual(200, response.status_code)
        
    def test_get_unauthorized_position(self):
        self.user.active = False
        access_token = create_access_token(self.user.id)
        headers = {'Authorization': f'Bearer {access_token}'}
        response = self.client.get('/api/v1/positions/1', headers=headers)
        self.assertEqual(401, response.status_code)
        
    def test_get_not_found_position(self):
        headers = {'Authorization': f'Bearer {self.access_token}'}
        response = self.client.get('/api/v1/positions/999', headers=headers)
        self.assertEqual(404, response.status_code)
        
    def test_get_positions(self):
        headers = {'Authorization': f'Bearer {self.access_token}'}
        response = self.client.get('/api/v1/positions', headers=headers)
        self.assertEqual(200, response.status_code)
        
    def test_get_unauthorized_positions(self):
        self.user.active = False
        access_token = create_access_token(self.user.id)
        headers = {'Authorization': f'Bearer {access_token}'}
        response = self.client.get('/api/v1/positions', headers=headers)
        self.assertEqual(401, response.status_code)
        
    def test_create_valid_positions(self):
        headers = {'Authorization': f'Bearer {self.access_token}'}
        response = self.client.post('/api/v1/positions', json={
            "title": "TestPosition2"
        }, headers=headers)
        self.assertEqual(201, response.status_code)
        
    def test_create_invalid_positions(self):
        headers = {'Authorization': f'Bearer {self.access_token}'}
        response = self.client.post('/api/v1/positions', json={
            "title": 1
        }, headers=headers)
        self.assertEqual(400, response.status_code)
        
    def test_create_unauthorized_positions(self):
        self.user.active = False
        access_token = create_access_token(self.user.id)
        headers = {'Authorization': f'Bearer {access_token}'}
        response = self.client.post('/api/v1/positions', json={
            "title": "TestPosition2"
        }, headers=headers)
        self.assertEqual(401, response.status_code)
        