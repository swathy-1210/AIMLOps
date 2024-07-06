import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from bike_sharing_data.config.core import config
from bike_sharing_data.pipeline import bikeshare_pipeline
from bike_sharing_data.processing.data_manager import load_dataset, save_pipeline
from sklearn.metrics import mean_squared_error, r2_score

def run_training() -> None:
    
    """
    Train the model.
    """

    # read training data
    bikeshare = load_dataset(file_name=config.app_config.training_data_file)

    print(bikeshare)


    target_col = ['cnt']
   # Separate target and prediction features
    X = bikeshare.drop(target_col, axis=1)
    y = bikeshare[target_col]


# Apply train test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

    # Pipeline fitting
    bikeshare_pipeline.fit(X_train,y_train)
    # y_pred = bikeshare_pipeline.predict(X_test)
    # print("Accuracy(in %):", accuracy_score(y_test, y_pred)*100)

    # Prediction for test set
    y_pred = bikeshare_pipeline.predict(X_test)

    # Calculate the score/error
    print("R2 score:", r2_score(y_test, y_pred))
    print("Mean squared error:", mean_squared_error(y_test, y_pred))

    # persist trained model
    save_pipeline(pipeline_to_persist= bikeshare_pipeline)
    # printing the score
    
if __name__ == "__main__":
    run_training()