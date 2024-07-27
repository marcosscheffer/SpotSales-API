import unittest
from flask_jwt_extended import create_access_token

from app import create_app
from app.config import TestConfig
from app.extensions import db
from app.models.user_model import UserModel
from app.models.position_model import PositionModel

from app.models.seller_model import SellerModel


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
        self.seller = SellerModel(id=1, 
                                  first_name="test", 
                                  last_name="seller", 
                                  email="test@example.com")
        db.session.add(self.user)
        db.session.add(self.seller)
        db.session.commit()
        
        self.access_token = create_access_token(self.user.id)
            
        
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()  
        
    def test_get_sellers(self):
        headers = {'Authorization': f'Bearer {self.access_token}'}
        response = self.client.get('/api/v1/sellers', headers=headers)

        self.assertEqual(response.status_code, 200)
    
    def test_get_valid_seller(self):
        headers = {'Authorization': f'Bearer {self.access_token}'}
        response = self.client.get('/api/v1/sellers/1', headers=headers)

        self.assertEqual(response.status_code, 200)
        
    def test_get_invalid_seller(self):
        headers = {'Authorization': f'Bearer {self.access_token}'}
        response = self.client.get('/api/v1/sellers/999', headers=headers)
        
        self.assertEqual(response.status_code, 404)
        
    def test_get_unauthorized_sellers(self):
        self.user.active = False

        access_token = create_access_token(self.user.id)
        headers = {'Authorization': f'Bearer {access_token}'}
        
        response = self.client.get('/api/v1/sellers', headers=headers)
        
        self.assertEqual(response.status_code, 401)
        self.assertIn("Unauthorized - Only admin and user can access", response.get_data(as_text=True))
        
    def test_get_unauthorized_seller(self):
        self.user.active = False
        
        access_token = create_access_token(self.user.id)
        headers = {'Authorization': f'Bearer {access_token}'}
        
        response = self.client.get('/api/v1/sellers/1', headers=headers)
        
        self.assertEqual(response.status_code, 401)
        self.assertIn("Unauthorized - Only admin and user can access", response.get_data(as_text=True))

    def test_create_valid_seller(self):
        headers = {'Authorization': f'Bearer {self.access_token}'}
        response = self.client.post('/api/v1/sellers', json={
            "id": 2,
            "first_name": "TestSeller",
            "last_name": "Seller",
            "email": "testseller@example.com"}, headers=headers)
        
        self.assertEqual(response.status_code, 201)
        
    def test_create_invalid_seller(self):
        headers = {'Authorization': f'Bearer {self.access_token}'}
        response = self.client.post('/api/v1/sellers', json={
            "id": 1,
            "first_name": "TestSeller",
            "last_name": "Seller",
            "email": "testseller@example.com"}, headers=headers)
        
        self.assertEqual(response.status_code, 400)
        
    def test_create_unauthorized_seller(self):
        self.user.active = False
        
        access_token = create_access_token(self.user.id)
        headers = {'Authorization': f'Bearer {access_token}'}
        response = self.client.post('/api/v1/sellers', json={
            "id": 2,
            "first_name": "TestSeller",
            "last_name": "Seller",
            "email": "testseller@example.com"}, headers=headers)
        
        self.assertEqual(response.status_code, 401)

