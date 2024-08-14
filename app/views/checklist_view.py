from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt, get_jwt_identity
from flask import request

from ..schemas.checklist_schema import ChecklistSchema
from ..entities.checklist import Checklist
from ..services.checklist_service import register_checklist_service, get_checklist_service, update_checklist_service

from ..extensions import api_v1

class ChecklistsView(Resource):
    @jwt_required()
    def post(self):
        claims = get_jwt()
        if claims.get("roles", "guest") not in ['admin', 'user']:
            return "Unauthorized - Only admin can access", 403
        
        
        cs = ChecklistSchema(partial=True)
        data = request.get_json()
        validate = cs.validate(data)
        if validate:
            return validate, 400
        
        checklist = Checklist(id=data["id"],
                              seller_id=data.get("seller_id", 0),
                              sale_date=data.get("sale_date", "0000-00-00T00:00:00"),
                              value=data.get("value", 0))
        
        response = register_checklist_service(checklist)
        
        return cs.dump(response), 201
    
    
    
class ChecklistView(Resource):
    @jwt_required()
    def put(self, id):
        claims = get_jwt()
        if claims.get("roles", "guest") not in ['admin', 'user']:
            return "Unauthorized - Only admin can access", 403
        
        
        cs = ChecklistSchema(partial=True)
        data = request.get_json()
        validate = cs.validate(data)
        if validate:
            return validate, 400
        
        checklist = Checklist(phases=data.get('phases'),
                              voltage=data.get('voltage'),
                              power=data.get('power'),
                              special_project=data.get('special_project'),
                              eletric_key=data.get('eletric_key'),
                              eletric_panel=data.get('eletric_panel'),
                              description_panel=data.get('description'),
                              layout=data.get('layout'),
                              pipeline=data.get('pipeline'),
                              special_paint=data.get('special_paint'),
                              extra_filters=data.get('extra_filters'),
                              assembly=data.get('assembly'),
                              freight=data.get('freight'),
                              pallet=data.get('pallet'),
                              address=data.get('address'),
                              deadline=data.get('deadline'),
                              other=data.get('other'),
                              filled=data.get('filled'))
        
        
        response = update_checklist_service(checklist, id) 
        
        return cs.dump(response), 201
    
    @jwt_required()
    def get(self, id):
        claims = get_jwt()
        if claims.get("roles", "guest") not in ['admin', 'user']:
            return "Unauthorized - Only admin can access", 403
        
        cs = ChecklistSchema(partial=True)
        response = get_checklist_service(id)
        return cs.dump(response), 200
    
    
        
    
api_v1.add_resource(ChecklistsView, '/checklist')
api_v1.add_resource(ChecklistView, '/checklist/<int:id>')
        