from django.shortcuts import render
import pickle
import logging
import os

# Creating a logging object to log data
logger = logging.getLogger(__name__)

# Get the parent directory of the current directory (i.e. hello_django/)
parent_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

# Construct the path to the pickle file in the models/ directory
data_path = os.path.join(parent_dir, 'model', 'lr_final')

# Load the machine learning model from a saved file
with open(data_path, 'rb') as file:
    model = pickle.load(file)

def predict(request):
    if request.method == 'POST':
        # Get the user inputs from the form
        # request.POST returns a dictionary like object where 'gre_score' 
        # is the name tag from the html form acting like a key. The value we get is a string 
        # so we have to TypeCast it
        gre_score = int(request.POST['gre_score']) 
        toefl_score = int(request.POST['toefl_score'])
        lor = float(request.POST['lor'])
        cgpa = float(request.POST['cgpa'])

        # Prepare the input data for the model  
        input_data = [[1,gre_score, toefl_score, lor, cgpa]]

        # Use the model to make a prediction
        prediction = model.predict(input_data)[0]
        # [0.64523301] predicted value. Use [0] to access it
        logger.debug(model.predict(input_data))
        prediction = str(round(prediction, 3) * 100) + " %"

        # Render the prediction in the template
        # We include the request object here as per the render syntax.
        # It contains information about the request, including the requested URL, headers, and parameters.
        # The code still runs even if we dont provide the request object
        # Request object contains user information, session data and CRSF token data. 
        # Every website you request to needs this information.
        return render(request, 'prediction.html', {
            'prediction': prediction,
            'gre_score': gre_score,
            'toefl_score': toefl_score,
            'lor': lor,
            'cgpa': cgpa
        })
    else:
        # Render the form for the user to enter input
        return render(request, 'form.html')
    


