from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.annotation import Annotated

from core.config import settings
from core.models import db_helper
from core.schemas.user import UserRead, UserCreate
from core.models import User
from crud import get_all_users, create_user

router = APIRouter(
    prefix=settings.api.v1.users,
    tags=["users"],
)


@router.get("/", response_model=list[UserRead])
async def get_users(
    session: AsyncSession = Depends(db_helper.session_getter),
):
    users = await users_crud.get_all_users(session=session)
    return users


@router.post("/", response_model=UserRead)
async def create_user(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    user_create: UserCreate,
) -> User:
    user = await users_crud.create_user(
        session=session,
        user_create=user_create,
    )
    return user
