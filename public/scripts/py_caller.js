const { spawn } = require('child_process');
const pythonDir = (__dirname + "/venv/");  
const python = 'python3'

function cleanWarning(error) {
    return error.replace(/Detector is not able to detect the language reliably.\n/g,"");
}

function callPython(scriptName, args) {
    return new Promise(function(success, reject) {
        const script = pythonDir + scriptName;
        const pyArgs = [script, JSON.stringify(args)]
        const pyprog = spawn(python, pyArgs);
        let result = "";
        let resultError = "";
        pyprog.stdout.on('data', function(data) {
            result += data.toString();
        });

        pyprog.stderr.on('data', (data) => {
            resultError += cleanWarning(data.toString());
        });

        pyprog.stdout.on("end", function(){
            if(resultError == "") {
                success(JSON.parse(result));
            }else{
                console.error(`Python error, you can reproduce the error with: \n${python} ${script} ${pyArgs.join(" ")}`);
                const error = new Error(resultError);
                console.error(error);
                reject(resultError);
            }
        })
   });
}
module.exports.callPython = callPython;