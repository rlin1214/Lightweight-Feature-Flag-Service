import { Router } from 'express';
import * as controller from '../controllers/admin.controller';

const router = Router();

router.post('/flags', controller.createFlag);

router.put('/flags/:id', controller.updateFlag);

router.delete('/flags/:id', controller.deleteFlag);

router.post('/flags/:id/kill', controller.killSwitch);

export default router;