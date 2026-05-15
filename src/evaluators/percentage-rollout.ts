import crypto from 'crypto';

export function isInRollout(
  userId: string,
  flagName: string,
  percentage: number
): boolean {
  const hash = crypto
    .createHash('sha256')
    .update(`${userId}:${flagName}`)
    .digest('hex');

  const bucket = parseInt(hash.substring(0, 8), 16) % 100;

  return bucket < percentage;
}