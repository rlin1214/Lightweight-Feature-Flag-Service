import { prisma } from '../lib/prisma';
import { redis } from '../lib/redis';
import { evaluateFlag } from '../evaluators/evaluation-engine';

export async function createFlag(data: any) {

  const flag = await prisma.featureFlag.create({
    data
  });

  await redis.del('all_flags');

  return flag;
}

export async function updateFlag(
  id: string,
  data: any
) {

  const flag = await prisma.featureFlag.update({
    where: { id },
    data
  });

  await redis.del('all_flags');

  return flag;
}

export async function deleteFlag(id: string) {

  return prisma.featureFlag.delete({
    where: { id }
  });
}

export async function getFlagsForUser(
  userId: string
) {

  const cached = await redis.get('all_flags');

  let flags;

  if (cached) {
    flags = JSON.parse(cached);
  } else {

    flags = await prisma.featureFlag.findMany();

    await redis.set(
      'all_flags',
      JSON.stringify(flags),
      'EX',
      30
    );
  }

  const evaluated: Record<string, boolean> = {};

  for (const flag of flags) {

    evaluated[flag.name] = evaluateFlag(
      flag,
      userId
    );
  }

  return evaluated;
}