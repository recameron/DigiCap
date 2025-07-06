// server/index.js
import express from 'express';
import cors from 'cors';

const app = express();
const PORT = 4000;

app.use(cors());
app.use(express.json());

let capsules = [];

app.post('/api/capsules', (req, res) => {
  const capsule = req.body;
  capsules.push({ ...capsule, id: capsules.length + 1 });
  res.status(201).json({ message: 'Capsule saved', capsule });
});

app.get('/api/capsules', (req, res) => {
  res.json(capsules);
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
