from django.shortcuts import render
import pickle
import logging

# Creating a logging object to log data
logger = logging.getLogger(__name__)

# Load the machine learning model from a saved file
with open(r'C:\Users\user\Desktop\DATA BACK UP\Data_sdsouza33\LAMBTON\SEM 2\BDM 2203 AML\project\model\lr', 'rb') as file:
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
        research = int(request.POST['research'])

        # Prepare the input data for the model  
        input_data = [[1,gre_score, toefl_score, lor, cgpa, research]]

        # Use the model to make a prediction
        prediction = model.predict(input_data)[0]
        # [0.64523301] predicted value. Use [0] to access it
        logger.debug(model.predict(input_data))
        prediction = str(round(prediction,2) * 100) + " %"

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
            'cgpa': cgpa,
            'research': research,
        })
    else:
        # Render the form for the user to enter input
        return render(request, 'form.html')
    


