from flask import request, url_for
from sqlalchemy import or_

def paginate(model, schema):
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    q = request.args.get("q", None)
    

    query = model.query

    if q:
        filters = []
        for column in model.__table__.columns:
            if column.type.python_type == str:
                filters.append(column.ilike(f"%{q}%"))
        
        if filters:
            query = query.filter(or_(*filters))
        

    
        
    page_obj = query.paginate(page=page, per_page=per_page)

    
    
    next = url_for(
        request.endpoint,
        page=page_obj.next_num if page_obj.has_next else page_obj.page, 
        per_page=per_page,
        q=q,
        **request.view_args
    )
    
    prev = url_for(request.endpoint,
                   page=page_obj.prev_num if page_obj.has_prev else page_obj.page, 
                   per_page=per_page,
                   q=q,
                   **request.view_args)
    
    return {
        "total": page_obj.total,
        "pages": page_obj.pages,
        "next": next,
        "prev": prev,
        
        "results": schema.dump(page_obj.items)
        
    }