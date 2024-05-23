from sqlalchemy.orm import Session
from fastapi import Depends

from database import get_db
from repositories.campaigns_repository import CampaignRepository
from repositories.users_repository import UserRepository


def get_user_repository(db: Session = Depends(get_db)) -> UserRepository:
    return UserRepository(db)


def get_campaign_repository(db: Session = Depends(get_db)) -> CampaignRepository:
    return CampaignRepository(db)