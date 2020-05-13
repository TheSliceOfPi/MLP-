Edith Flores
 

Files:
preprocess.py
normalize.py
experiment.py
mlp.py
preprocessOutput.txt
normalizeOutput.txt
indels.arff
MLHW3.Report.pdf
readme.txt

--------preprocess.py-----------------
The program preprocess.py takes a file with the all the data samples. The output is a file,that can be used with loadtxt, with the same data samples but whos targets are changed to 0 or 1, depending on what their original target was. 
To run(general): python3 reg.py <data filename> <output filename>

--------normalize.py--------------
The program normalize.py takes a file with the all the data samples whos target are 0 or 1. The output is a file,that can be used with loadtxt, with the same data samples but with the features normalized between 0 to 1. Numbers above 50 were automatically set to 1 in order to prevent extremes from skewing the results 
To run(general): python3 reg.py <preprocessed filename> <normalize filename>

--------experiment.py--------------
The program experiment.py allows the user to test out various number of nodes in the hidden layer, test out various momentums, and output the confusion matrix and percentage of samples correctly categorized. Experiment.py had three functions: Main, getParameter(array,parameter), and getMatrix(nHidden,momentum).
The function getParameter has two parameters, array and parameter. The parameter "array" is an array of the number we want to test out as our nHidden or our momentum. The parameter "parameter" is a string that tells us what parameter in mlp training do we want to test out (number of nodes in the hidden layer, or the momentum). The function getParameter uses 5-fold crossvalidation to find the validation errors we get for each number in the array.
The function getMatrix takes two parameters, nHidden and momentum. The parameter "nHidden" is the number of nodes that the hidden layer will have, and the parameter "momentum" is the momentum that mlp will use to train our data set. The function getMatric uses 5-fold validation to determine which portion of the data samples will be the training samples, the validation samples, and test samples. getMatrix then calls mlp in order to determine the confusion matrix and the percentage of samples correctly categorized.

To run(general): python3 experiment.py

--------------overall--------------
To run(general): python3 reg.py <data filename> <output filename>
                 python3 reg.py <preprocessed filename> <normalize filename>
                 python3 experiment.py


