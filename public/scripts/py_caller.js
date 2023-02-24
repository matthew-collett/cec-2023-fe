import path from 'path';

const { spawn } = require('child_process');
const dir = path.join(__dirname, '/');

function callPython(scriptName, args) {
    return new Promise(function(success) {
        const process = spawn('python3', path.join(dir, scriptName), JSON.stringify(args));
        let data = '';
        process.stdout.on('data', function(d) {
            data += d.toString();
        });

        process.stdout.on('end', function(){
            success(JSON.parse(data));
        })
   });
}
module.exports.callPython = callPython;