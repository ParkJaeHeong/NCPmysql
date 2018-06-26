const { Router } = require('express')
const { spawn } = require('child_process');

const router = Router()

router.post('/server', (req, res) => {
  const python = spawn('python', ['./replication.py', JSON.stringify(req.body.setting), JSON.stringify(req.body.dbUser)]);
  python.stdout.on('data', (data) => {
    console.log(`stdout: ${data}`);
  });

  python.stderr.on('data', (data) => {
    console.log(`stderr: ${data}`);
  });

  python.on('close', (code) => {
    console.log(`child process exited with code ${code}`);
    res.json({ msg: 'ok' });
  });
});

module.exports = router
