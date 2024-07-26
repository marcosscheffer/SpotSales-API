from flask_restful import Resource
from flask import request

from ..extensions import api_v1
from ..services.position_service import (get_positions_service, get_position_by_id_service, 
                                         register_position_service)
from ..schemas.position_schema import PositionSchema
from ..entities.position import Position

class PositionsView(Resource):
    def get(self):
        positions = get_positions_service()
        ps = PositionSchema(many=True)
        response = ps.dump(positions)
        return response, 200
    
    def post(self):
        ps = PositionSchema()
        validate = ps.validate(request.json)
        if validate:
            return validate, 400
        
        data = request.get_json()
        position = Position(title=data["title"])
        response = register_position_service(position)
        return ps.dump(response), 201
    
class PositionView(Resource):
    def get(self, id):
        position = get_position_by_id_service(id)
        if not position:
            return "Not Found - No Position", 404
        
        ps = PositionSchema()
        response = ps.dump(position)
        return response, 200
    
    
api_v1.add_resource(PositionsView, '/positions')
api_v1.add_resource(PositionView, '/positions/<int:id>')
                