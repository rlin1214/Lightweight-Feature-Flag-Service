import json

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal, engine, Base
from models import FeatureFlag, AuditLog
from schemas import FeatureFlagCreate
from evaluator import evaluate_flag

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Feature Flag Service")


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


def create_audit_log(
    db,
    flag_name,
    action,
    changed_by,
    before_state,
    after_state
):
    log = AuditLog(
        flag_name=flag_name,
        action=action,
        changed_by=changed_by,
        before_state=json.dumps(before_state),
        after_state=json.dumps(after_state)
    )

    db.add(log)
    db.commit()


@app.get("/")
def home():
    return {
        "message": "Feature Flag Service Running"
    }


@app.post("/admin/flags")
def create_flag(
    flag: FeatureFlagCreate,
    changed_by: str,
    db: Session = Depends(get_db)
):
    existing = db.query(FeatureFlag).filter(
        FeatureFlag.name == flag.name
    ).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Flag already exists"
        )

    db_flag = FeatureFlag(
        name=flag.name,
        description=flag.description,
        enabled=flag.enabled,
        kill_switch=flag.kill_switch,
        rollout_percentage=flag.rollout_percentage,
        targeted_users=",".join(flag.targeted_users)
    )

    db.add(db_flag)
    db.commit()

    create_audit_log(
        db,
        flag.name,
        "CREATE",
        changed_by,
        {},
        {"enabled": flag.enabled}
    )

    return {
        "message": "Flag created"
    }


@app.get("/client/flags/{user_id}")
def get_flags_for_user(
    user_id: str,
    db: Session = Depends(get_db)
):
    flags = db.query(FeatureFlag).all()

    result = {}

    for flag in flags:
        result[flag.name] = evaluate_flag(flag, user_id)

    return {
        "user_id": user_id,
        "flags": result
    }