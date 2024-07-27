import unittest
from flask_jwt_extended import create_access_token
from datetime import datetime

from app import create_app
from app.config import TestConfig
from app.extensions import db
from app.models.user_model import UserModel
from app.models.position_model import PositionModel
from app.models.lead_sale_model import LeadSaleModel

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
        
        self.lead = LeadSaleModel(id=1, sale_date=datetime(2023, 7, 26, 12, 0, 0), value=1.00, seller_id=1)
        db.session.add(self.lead)
        db.session.commit()
        
        self.access_token = create_access_token(self.user.id)
            
        
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
        
    def test_get_leads_sales(self):
        headers = {'Authorization': f'Bearer {self.access_token}'}
        response = self.client.get('/api/v1/leadsSales', headers=headers)
        self.assertEqual(200, response.status_code)
        
    def test_get_unauthorized_leads_sales(self):
        self.user.active = False
        access_token = create_access_token(self.user.id)
        headers = {'Authorization': f'Bearer {access_token}'}
        response = self.client.get('/api/v1/leadsSales', headers=headers)
        self.assertEqual(401, response.status_code)
        
    def test_get_lead_sale(self):
        headers = {'Authorization': f'Bearer {self.access_token}'}
        response = self.client.get('/api/v1/leadsSales/1', headers=headers)
        self.assertEqual(200, response.status_code)
        
    def test_get_unauthorized_lead_sale(self):
        self.user.active = False
        access_token = create_access_token(self.user.id)
        headers = {'Authorization': f'Bearer {access_token}'}
        response = self.client.get('/api/v1/leadsSales/1', headers=headers)
        self.assertEqual(401, response.status_code)
        
    def test_get_not_found_lead_sale(self):
        headers = {'Authorization': f'Bearer {self.access_token}'}
        response = self.client.get('/api/v1/leadsSales/999', headers=headers)
        self.assertEqual(404, response.status_code)
        
    def test_create_valid_lead_sale(self):
        headers = {'Authorization': f'Bearer {self.access_token}'}
        response = self.client.post('/api/v1/leadsSales', headers=headers, json={
            "id": 1234,
            "sale_date": "2023-07-26T12:00:00Z",
            "value": 2.00,
            "seller_id": 1
        })
        
        self.assertEqual(201, response.status_code)
        
    def test_create_invalid_lead_sale(self):
        headers = {'Authorization': f'Bearer {self.access_token}'}
        response = self.client.post('/api/v1/leadsSales', headers=headers, json={
            "sale_date": "2023-07-26T12:00:00Z",
            "value": 2.00
        })
        
        self.assertEqual(400, response.status_code)
        
        
    def test_create_invalid_date_lead_sale(self):
        headers = {'Authorization': f'Bearer {self.access_token}'}
        response = self.client.post('/api/v1/leadsSales', headers=headers, json={
            "id": "1234",
            "sale_date": "2023-07-26 12:00:00",
            "value": 2.00,
            "seller_id": 1
        })
        
        self.assertEqual(400, response.status_code)
        
    def test_create_unauthorized_lead_sale(self):
        self.user.active = False
        access_token = create_access_token(self.user.id)
        headers = {'Authorization': f'Bearer {access_token}'}
        response = self.client.post('/api/v1/leadsSales', headers=headers, json={
            "id": 1234,
            "sale_date": "2023-07-26T12:00:00Z",
            "value": 2.00,
            "seller_id": 1
        })
        
        self.assertEqual(401, response.status_code)
        