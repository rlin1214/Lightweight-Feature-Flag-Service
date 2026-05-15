import { Request, Response } from 'express';
import { getFlagsForUser } from '../services/feature.service';

export async function getUserFlags(
  req: Request,
  res: Response
) {

  const userId = req.query.userId as string;

  const flags = await getFlagsForUser(userId);

  res.json({
    userId,
    flags
  });
}