const { spawn } = require('child_process');

function callPython(scriptPath, args) {
    return new Promise(function(success) {
        const process = spawn('python', [scriptPath, JSON.stringify(args)]);

        let data = '';
        let error = false;

        process.stdout.on('data', (d) => {
            data += d.toString();
        });

        process.stderr.on('data', () => {
            error = true;
        });
    
        process.stdout.on("end", () => {
            if (error) {
                let errorMsg = 'An unexpected python error occured.';
                console.error(errorMsg);
                reject(errorMsg);  
            } else {
                success(JSON.parse(data));
            }
        })
   });
}
module.exports.callPython = callPython;