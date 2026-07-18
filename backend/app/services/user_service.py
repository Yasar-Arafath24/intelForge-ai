from sqlalchemy.orm import Session

from app.models.user import User
from app.auth.password import hash_password


def create_user(
    db: Session,
    name: str,
    email: str,
    password: str
):

    user = User(
        name=name,
        email=email.strip().lower(),
        password_hash=hash_password(password)
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def get_user_by_email(db, email):

    return db.query(User).filter(
        User.email == email
    ).first()


def get_user_by_email(
    db: Session,
    email: str
):

    return (
        db.query(User)
        .filter(
            User.email == email.strip().lower()
        )
        .first()
    )
    
def get_user_by_id(
    db,
    user_id
):

    return db.query(User).filter(
        User.id == user_id
    ).first()