import express from 'express';
import cors from 'cors';
import morgan from 'morgan';

import adminRoutes from './routes/admin.routes';
import clientRoutes from './routes/client.routes';

const app = express();

app.use(cors());
app.use(express.json());
app.use(morgan('dev'));

app.use('/admin', adminRoutes);
app.use('/client', clientRoutes);

export default app;