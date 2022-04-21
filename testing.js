const PythonShell = require('python-shell').PythonShell;

var options = {
  mode: 'text',
  // pythonPath: 'C:/Users/x5/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Python 3.9',
  pythonOptions: ['-u'],
  // scriptPath: 'grammar_check.py',
   args: ['he and i go to school.']
};

PythonShell.run('grammar_check.py', options, function (err, results) {
  if (err) 
    throw err;
  // Results is an array consisting of messages collected during execution
  console.log(results[0]);
});