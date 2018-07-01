const { Router } = require('express');
const { spawn } = require('child_process');

const router = Router();

router.post('/server', (req, res) => {
  const python = spawn('/Users/parkjaeheong/anaconda3/envs/mysqlad/bin/python3.5', ['./replication.py', JSON.stringify(req.body.setting), JSON.stringify(req.body.dbUser), JSON.stringify(req.body.host)]);
  let msg = '';
  python.stdout.on('data', (data) => {
    msg += data;
    console.log(`stdout: ${data}`);
  });

  python.stderr.on('data', (data) => {
    msg += data;
    console.log(`stderr: ${data}`);
  });

  python.on('close', (code) => {
    console.log(`child process exited with code ${code}`);
    res.json({ msg });
  });
});

module.exports = router;
