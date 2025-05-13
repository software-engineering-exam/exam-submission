from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud, database, auth, encryption


models.Base.metadata.create_all(bind=database.engine)


app = FastAPI()


# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/token")
def login():
    # For demonstration, returns a token for a dummy user
    access_token = auth.create_access_token(data={"sub": "testuser"})
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/products/", response_model=schemas.ProductOut)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db), username: str = Depends(auth.get_current_user)):
    return crud.create_product(db=db, product=product)


@app.get("/products/{product_id}", response_model=schemas.ProductOut)
def read_product(product_id: int, db: Session = Depends(get_db), username: str = Depends(auth.get_current_user)):
    db_product = crud.get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    # Decrypt sensitive fields before returning
    db_product.description = encryption.decrypt_field(db_product.description)
    db_product.category = encryption.decrypt_field(db_product.category)
    return db_product


@app.put("/products/{product_id}", response_model=schemas.ProductOut)
def update_product(product_id: int, product: schemas.ProductUpdate, db: Session = Depends(get_db), username: str = Depends(auth.get_current_user)):
    db_product = crud.update_product(db, product_id=product_id, product=product)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db), username: str = Depends(auth.get_current_user)):
    db_product = crud.delete_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"detail": "Product deleted"}
