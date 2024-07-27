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
    
    def test_get_valid_user(self):
        response = self.client.get('api/v1/user/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.user.name, response.get_data(as_text=True))
        
    def test_get_invalid_user(self):
        response = self.client.get('api/v1/user/999')
        self.assertEqual(response.status_code, 404)
        
    def test_put_valid_user(self):
        headers = {'Authorization': f'Bearer {self.access_token}'}
        response = self.client.put('api/v1/user/1', json={"name": "NewTestUser"}, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn("NewTestUser", response.get_data(as_text=True))
        
    def test_put_invalid_user(self):
        headers = {'Authorization': f'Bearer {self.access_token}'}
        response = self.client.put('api/v1/user/999', json={"name": "NewTestUser"}, headers=headers)
        self.assertEqual(response.status_code, 404)
    
    def test_put_invalid_field_user(self):
        headers = {'Authorization': f'Bearer {self.access_token}'}
        response = self.client.put('api/v1/user/1', json={"invalid_field": "NewTestUser"}, headers=headers)
        self.assertEqual(response.status_code, 400)
        
    def test_put_unauthorized_user(self):
        self.user.admin = False
        db.session.commit()
        self.access_token = create_access_token(self.user.id)
        headers = {'Authorization': f'Bearer {self.access_token}'}
        response = self.client.put('api/v1/user/1', json={"name": "TestName"}, headers=headers)
        self.assertEqual(response.status_code, 401)
