import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor

from bike_sharing_data.config.core import config
from bike_sharing_data.processing.features import WeekdayImputer
from bike_sharing_data.processing.features import WeathersitImputer
from bike_sharing_data.processing.features import Mapper
from bike_sharing_data.processing.features import OutlierHandler
from bike_sharing_data.processing.features import WeekdayOneHotEncoder
from bike_sharing_data.processing.features import UnusedColmnsClass


bikeshare_pipeline = Pipeline([
    
    ("weekday_imputer", WeekdayImputer()),
    ("weathersit_imputer", WeathersitImputer()),
    ("mappers", Mapper()),
    ("outliers",OutlierHandler()),
    ("encoded_weekday", WeekdayOneHotEncoder()),
    ("unusedcolms", UnusedColmnsClass()),
    ("model_rf", RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42))
])