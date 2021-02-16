from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from .. import crud, deps, models, schemas

router = APIRouter()


@router.post("/users/{user_id}/categories/", response_model=schemas.JobCategory)
def create_item_for_user(
        user_id: int, category: schemas.JobCategoryCreate, db: Session = Depends(deps.get_db)):
    """
    Create an item for a specific user.
    """
    return crud.create_user_category(db=db, category=category, user_id=user_id)


# @router.get("/categories/{category}", response_model=schemas.JobCategory)
# def get_category(category: List[str], db: Session = Depends(deps.get_db)):
#     db_category = crud.get_cats(db, category=category)
#     if db_category is None:
#         raise HTTPException(status_code=404, detail="category not found")
#     return db_category


@router.get("/categories/", response_model=List[schemas.JobCategory])
def get_categories(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db),
                   q: Optional[str] = Query(None, alias="category-query")):
    """
    Read all the items. Doesn't need authentication.
    """
    categories = crud.get_categories(db, skip=skip, limit=limit)
    results = []

    if q:
        for i in categories:
            if q == i.category:
                results.append(i)
        return results
    return categories

# @router.get("/categories/")
# async def read_items():
#     if q:
#         query_items = {"q": q}
#     return query_items
