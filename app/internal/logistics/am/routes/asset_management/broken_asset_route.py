  
from fastapi import APIRouter, Depends, HTTPException, Cookie
from sqlalchemy.orm import Session
from app.internal.logistics.am.schemas.asset_management.broken_asset_schema import CreateBroken
from app.internal.logistics.am.schemas.asset_management.asset_schema import UpdateStatus
from models import *
from database import get_db
# from dependencies import get_token


router = APIRouter(
    prefix='/asset_management/api/broken_asset',
    tags=['Broken_Asset'],
    # dependencies=[Depends(get_token)]
)

# @router.get('/{id}')
# def read(id: str, db: Session = Depends(get_db)):
#     event = db.query(Events).filter(Events.asset_id == id).order_by(Events.created_at.desc()).all()
#     if not event:
#         raise HTTPException(404, 'events not found')
#     return {'data': event}

@router.post('/')
def add(broken_asset: CreateBroken, db: Session = Depends(get_db)):
    try:
        broken_asset_schema = Broken_Asset(
            
            asset_id = broken_asset.asset_id,
            remarks = broken_asset.remarks,
            broken_date = broken_asset.broken_date,
            created_by = broken_asset.created_by,

        )

        db.query(Asset).filter(Asset.asset_id == broken_asset_schema.asset_id).update({
        "asset_remarks" : broken_asset_schema.remarks,
        "asset_status" : "Broken",
        })

        db.add(broken_asset_schema)
        db.commit()
        return {'message': 'Status created successfully.'}
    except Exception as e:
        print(e)

@router.delete('/undo/{id}')
def remove(id: str, db: Session = Depends(get_db)): 
    db.query(Broken_Asset).filter(Broken_Asset.asset_id == id).update({
        'active_status': 'Inactive',
    })
    db.query(Asset).filter(Asset.asset_id == id).update({
        'asset_status': 'Available',
    })
    db.commit()
    return {'message': 'asset status removed successfully.'}

@router.delete('/{id}')
def remove(id: str, db: Session = Depends(get_db)): 
    db.query(Broken_Asset).filter(Broken_Asset.asset_id == id).update({
        'active_status': 'Inactive',
    })
    db.commit()
    return {'message': 'asset status removed successfully.'}