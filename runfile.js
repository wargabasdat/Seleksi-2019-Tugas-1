import { run } from 'runjs'

export function clean () {
    fs.unlink('data/out.json', (err) => {
        if (err) throw err;
        console.log('path/file.txt was deleted');
    });
}

export function start () {
    clean()
    const spawn = require("child_process").spawn;
    const pythonProcess = spawn('python',["src/main.py"]);
}

export function build () {
  // if any (optional)
}