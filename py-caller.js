const { spawn } = require('child_process');

/** remove warning that you don't care about */
function cleanWarning(error) {
    return error.replace(/Detector is not able to detect the language reliably.\n/g,"");
}

function callPython(scriptPath, args) {
    return new Promise(function(success, reject) {
        const process = spawn('python3', [scriptPath, JSON.stringify(args)]);
        let result = "";
        let resultError = "";
        process.stdout.on('data', function(data) {
            result += data.toString();
        });

        process.stderr.on('data', (data) => {
            resultError += cleanWarning(data.toString());
        });

        process.stdout.on("end", function(){
            if(resultError == "") {
                success(JSON.parse(result));
            }else{
                const error = new Error(resultError);
                console.error(error);
                reject(resultError);
            }
        })
   });
}
module.exports.callPython = callPython;