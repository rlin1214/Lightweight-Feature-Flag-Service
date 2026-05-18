from pydantic import BaseModel
from typing import List


class FeatureFlagCreate(BaseModel):
    name: str
    description: str = ""
    enabled: bool = False
    kill_switch: bool = False
    rollout_percentage: int = 0
    targeted_users: List[str] = []


class FeatureFlagResponse(BaseModel):
    id: int
    name: str
    description: str
    enabled: bool
    kill_switch: bool
    rollout_percentage: int
    targeted_users: List[str]

    class Config:
        from_attributes = True