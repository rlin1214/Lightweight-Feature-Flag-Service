import hashlib


def user_in_rollout(user_id: str, percentage: int) -> bool:
    if percentage <= 0:
        return False

    if percentage >= 100:
        return True

    hash_value = hashlib.sha256(user_id.encode()).hexdigest()

    numeric_value = int(hash_value, 16)

    bucket = numeric_value % 100

    return bucket < percentage



def evaluate_flag(flag, user_id: str) -> bool:
    # kill switch overrides everything
    if flag.kill_switch:
        return False

    # flag disabled globally
    if not flag.enabled:
        return False

    # explicit targeted users
    targeted = []

    if flag.targeted_users:
        targeted = flag.targeted_users.split(",")

    if user_id in targeted:
        return True

    # percentage rollout
    return user_in_rollout(user_id, flag.rollout_percentage)