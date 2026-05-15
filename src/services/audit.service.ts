import { prisma } from '../lib/prisma';

export async function createAuditLog(data: any) {
  return prisma.auditLog.create({
    data
  });
}