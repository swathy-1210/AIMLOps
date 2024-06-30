import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from typing import Union
import pandas as pd
import numpy as np

from bike_sharing_data import __version__ as _version
from bike_sharing_data.config.core import config
from bike_sharing_data.pipeline import bikeshare_pipeline
from bike_sharing_data.processing.data_manager import load_pipeline
from bike_sharing_data.processing.data_manager import pre_pipeline_preparation
from bike_sharing_data.processing.validation import validate_inputs


pipeline_file_name = f"{config.app_config.pipeline_save_file}{_version}.pkl"
print(pipeline_file_name)
bikeshare_pipeline= load_pipeline(file_name=pipeline_file_name)


def make_prediction(*,input_data:Union[pd.DataFrame, dict]) -> dict:
    """Make a prediction using a saved model """

    validated_data, errors = validate_inputs(input_df=pd.DataFrame(input_data))
    
    # validated_data = validated_data.reindex(columns=['Pclass','Sex','Age','Fare', 'Embarked','FamilySize','Has_cabin','Title'])
    #validated_data = validated_data.reindex(columns=config.model_config.features)
    #print(validated_data)
    #results = {"predictions": None, "version": _version, "errors": errors}
    
    if not errors:
        predictions = bikeshare_pipeline.predict(validated_data)
        results = {"predictions": predictions,"version": _version, "errors": errors}
        
    return results


    # predictions = bikeshare_pipeline.predict(validated_data)
    # results = {"predictions": predictions,"version": _version}
    # return results

if __name__ == "__main__":

   
    

    data_in= {'dteday':["2012-11-05"],'season':["winter"],'hr':  ['6am'], 'holiday':['No'],
             'weekday':['Mon'],'workingday': ['Yes'], 'weathersit': ['Mist'], 'temp': ['6.1'],
             'atemp':['3.0014000000000003'], 'hum':['49.0'],'windspeed':['19.0012'],
             'casual':[4], 'registered':['135']} #removed count 139
    
    output = make_prediction(input_data=data_in)
    print(output)
