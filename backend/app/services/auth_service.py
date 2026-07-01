from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate


class AuthService:

    @staticmethod
    def register(db: Session, user: UserCreate):

        existing = UserRepository.get_by_email(db, user.email)

        if existing:
            raise ValueError("Email already registered")

        db_user = User(
            full_name=user.full_name,
            email=user.email,
            hashed_password=hash_password(user.password),
            role="Student",
        )

        return UserRepository.create(db, db_user)