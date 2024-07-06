from pydantic import BaseModel
from bike_sharing_data.predict import make_prediction  # Import the model package

import json

# data_in= {'dteday':["2012-11-05"],'season':["winter"],'hr':  ['6am'], 'holiday':['No'],
#              'weekday':['Mon'],'workingday': ['Yes'], 'weathersit': ['Mist'], 'temp': ['6.1'],
#              'atemp':['3.0014000000000003'], 'hum':['49.0'],'windspeed':['19.0012'],
#              'casual':[4], 'registered':['135']} #removed count 139
    
#output = make_prediction(input_data=data_in)

#print(output)


def api_make_prediction(data):
    
    # Use the model to make a prediction
    prediction = make_prediction(input_data=data)
    print(prediction)
    #finalpredictions = prediction[0]
    #print(finalpredictions)
    prediction["predictions"] = prediction["predictions"].tolist()
    response_json = json.dumps(prediction)
    print(response_json)
    return response_json