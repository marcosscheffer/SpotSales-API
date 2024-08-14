from ..extensions import db
from ..models.checklist_model import ChecklistModel
from ..entities.checklist import Checklist


def register_checklist_service(checklist: Checklist):
    checklist_db = ChecklistModel(id=checklist.id,
                   seller_id=checklist.seller_id,
                   sale_date=checklist.sale_date,
                   value=checklist.value,
                   )
    
    db.session.add(checklist_db)
    db.session.commit()
    
def update_checklist_service(checklist: Checklist, id: int):
    checklist_db = ChecklistModel.query.get(id)
    
    if checklist.phases != None:
        checklist_db.phases = checklist.phases
    if checklist.voltage != None:
        checklist_db.voltage = checklist.voltage
    if checklist.power != None:
        checklist_db.power = checklist.power
    if checklist.special_project != None:
        checklist_db.special_project = checklist.special_project
    if checklist.eletric_key != None:
        checklist_db.eletric_key = checklist.eletric_key
    if checklist.eletric_panel != None:
        checklist_db.eletric_panel = checklist.eletric_panel
    if checklist.description_panel != None:
        checklist_db.description_panel = checklist.description_panel
    if checklist.layout!= None:
        checklist_db.layout = checklist.layout
        
        
    if checklist.pipeline!= None:
        checklist_db.pipeline = checklist.pipeline
    if checklist.special_paint != None:
        checklist_db.special_paint = checklist.special_paint
    if checklist.extra_filters!= None:
        checklist_db.extra_filters = checklist.extra_filters
    if checklist.assembly!= None:
        checklist_db.assembly = checklist.assembly
        
    
    if checklist.freight!= None:
        checklist_db.freight = checklist.freight
    if checklist.pallet!= None:
        checklist_db.pallet = checklist.pallet
    if checklist.adress!= None:
        checklist_db.adress = checklist.adress
    if checklist.deadline!= None:
        checklist_db.deadline = checklist.deadline
    
    if checklist.other!= None:
        checklist_db.other = checklist.other
    if checklist.filled!= None:
        checklist_db.filled = checklist.filled
    
    db.session.commit()
    return checklist_db
    

def get_checklist_service(id: int):
    checklist_db = ChecklistModel.query.get(id)
    return checklist_db
    
    
    