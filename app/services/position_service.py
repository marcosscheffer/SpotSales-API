from ..extensions import db
from ..models.position_model import PositionModel
from ..entities.position import Position

def get_positions_service():
    return PositionModel.query.all()

def get_position_by_id_service(position_id: int):
    return PositionModel.query.get(position_id)

def register_position_service(position: Position):
    position_db = PositionModel(title=position.title)
    db.session.add(position_db)
    db.session.commit()
    return position_db
    

