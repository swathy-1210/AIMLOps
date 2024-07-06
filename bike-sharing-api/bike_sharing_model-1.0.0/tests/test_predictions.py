"""
Note: These tests will fail if you have not first trained the model.
"""
import sys
from pathlib import Path
from conftest import sample_input_data
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

import numpy as np
from sklearn.metrics import accuracy_score

from bike_sharing_data.predict import make_prediction


from bike_sharing_data import __version__ as _version
from bike_sharing_data.config.core import config
from bike_sharing_data.processing.data_manager import load_pipeline
from sklearn.metrics import mean_squared_error, r2_score
from bike_sharing_data.processing.data_manager import _load_raw_dataset
from sklearn.model_selection import train_test_split

import pytest


pipeline_file_name = f"{config.app_config.pipeline_save_file}{_version}.pkl"
print(pipeline_file_name)
bikeshare_pipeline= load_pipeline(file_name=pipeline_file_name)
from bike_sharing_data.processing.validation import validate_inputs


# def test_make_prediction(sample_input_data):
#     # Given
#     expected_no_predictions = 179

#     # When
#     result = make_prediction(input_data=sample_input_data[0])

#     # Then
#     predictions = result.get("predictions")
#     assert isinstance(predictions, np.ndarray)
#     assert isinstance(predictions[0], np.int64)
#     assert result.get("errors") is None
#     assert len(predictions) == expected_no_predictions
#     _predictions = list(predictions)
#     y_true = sample_input_data[1]
#     accuracy = accuracy_score(_predictions, y_true)
#     assert accuracy > 0.8


def sample_input_data():
    data = _load_raw_dataset(file_name=config.app_config.training_data_file)

    validated_data, errors = validate_inputs(input_df=data)

    target_col = ['cnt']
   # Separate target and prediction features
    X = validated_data.drop(target_col, axis=1)
    y = validated_data[target_col]

   

    # divide train and test
    X_train, X_test, y_train, y_test = train_test_split(
        X,  # predictors
        y,  # target
        test_size=.20,
        # we are setting the random seed here
        # for reproducibility
        random_state=42,
    )

    return X_test, y_test


def run_testing():
    
    """
    Train the model.
    """
    X_test, y_test = sample_input_data()


    print("X_test", X_test)
    print("y_test", y_test)

    # Prediction for test set
    y_pred = bikeshare_pipeline.predict(X_test)

    # Calculate the score/error
    print("R2 score:", r2_score(y_test, y_pred))
    print("Mean squared error:", mean_squared_error(y_test, y_pred))
    
    
    result = make_prediction(input_data=X_test)

    predictions = result.get("predictions")
    assert isinstance(predictions, np.ndarray)
    _predictions = list(predictions)
    y_true = y_test
    R2_score = r2_score(y_true, _predictions)
    assert R2_score > 0.9

    
if __name__ == "__main__":
        run_testing()

