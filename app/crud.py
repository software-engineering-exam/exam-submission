from sqlalchemy.orm import Session
from . import models, schemas, encryption


def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()


def get_products(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Product).offset(skip).limit(limit).all()


def create_product(db: Session, product: schemas.ProductCreate):
    encrypted_description = encryption.encrypt_field(product.description)
    encrypted_category = encryption.encrypt_field(product.category)
    db_product = models.Product(
        name=product.name,
        description=encrypted_description,
        price=product.price,
        category=encrypted_category,
        in_stock_quantity=product.in_stock_quantity
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def update_product(db: Session, product_id: int, product: schemas.ProductUpdate):
    db_product = get_product(db, product_id)
    if not db_product:
        return None
    for var, value in vars(product).items():
        if value is not None:
            setattr(db_product, var, value)
    db.commit()
    db.refresh(db_product)
    return db_product


def delete_product(db: Session, product_id: int):
    db_product = get_product(db, product_id)
    if not db_product:
        return None
    db.delete(db_product)
    db.commit()
    return db_product
