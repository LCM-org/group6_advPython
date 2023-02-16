from django.shortcuts import render
import pickle

# Load the machine learning model from a saved file
with open(r'C:\Users\user\Desktop\DATA BACK UP\Data_sdsouza33\LAMBTON\SEM 2\BDM 2203 AML\project\model\lr', 'rb') as file:
    model = pickle.load(file)

def predict(request):
    if request.method == 'POST':
        # Get the user inputs from the form
        gre_score = int(request.POST['gre_score'])
        toefl_score = int(request.POST['toefl_score'])
        lor = float(request.POST['lor'])
        cgpa = float(request.POST['cgpa'])
        research = int(request.POST['research'])

        # Prepare the input data for the model
        input_data = [[1,gre_score, toefl_score, lor, cgpa, research]]

        # Use the model to make a prediction
        prediction = model.predict(input_data)[0]
        prediction = str(round(prediction,2) * 100) + " %"

        # Render the prediction in the template
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
    


