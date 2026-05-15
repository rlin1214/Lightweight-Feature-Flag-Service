import { Router } from 'express';
import { getUserFlags } from '../controllers/client.controller';

const router = Router();

router.get('/flags', getUserFlags);

export default router;