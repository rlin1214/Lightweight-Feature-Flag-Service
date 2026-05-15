import { Request, Response } from 'express';
import * as featureService from '../services/feature.service';

export async function createFlag(
  req: Request,
  res: Response
) {

  const flag = await featureService.createFlag(
    req.body
  );

  res.json(flag);
}

export async function updateFlag(
  req: Request,
  res: Response
) {

  const flag = await featureService.updateFlag(
    req.params.id,
    req.body
  );

  res.json(flag);
}

export async function deleteFlag(
  req: Request,
  res: Response
) {

  await featureService.deleteFlag(req.params.id);

  res.json({
    success: true
  });
}

export async function killSwitch(
  req: Request,
  res: Response
) {

  const flag = await featureService.updateFlag(
    req.params.id,
    {
      killSwitch: true
    }
  );

  res.json(flag);
}