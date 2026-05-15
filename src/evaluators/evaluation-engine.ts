import { FeatureFlag } from '@prisma/client';
import { isInRollout } from './percentage-rollout';

export function evaluateFlag(
  flag: FeatureFlag,
  userId: string
): boolean {

  if (flag.killSwitch) {
    return false;
  }

  if (!flag.enabled) {
    return false;
  }

  if (flag.enableForAll) {
    return true;
  }

  if (flag.targetUsers.includes(userId)) {
    return true;
  }

  if (flag.rollout) {
    return isInRollout(
      userId,
      flag.name,
      flag.rollout
    );
  }

  return false;
}