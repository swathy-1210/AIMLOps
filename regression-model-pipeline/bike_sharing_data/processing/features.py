from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder

class WeekdayImputer(BaseEstimator, TransformerMixin):
    """Impute missing values in 'weekday' column by extracting day name from 'dteday' column"""

    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self  # Nothing to fit, so just return self

    def transform(self, X):
        df = X.copy()

        # Ensure 'dteday' is in datetime format
        df['dteday'] = pd.to_datetime(df['dteday'], errors='coerce')
        wkday_null_idx = df[df['weekday'].isnull() == True].index
        df.loc[wkday_null_idx, 'weekday'] = df.loc[wkday_null_idx, 'dteday'].dt.day_name().apply(lambda x: x[:3])
        return df
    
class WeathersitImputer(BaseEstimator, TransformerMixin):
    """ Impute missing values in 'weathersit' column by replacing them with the most frequent category value """
    def __init__(self):
        pass

    def fit(self, X, y=None):
        self.most_frequent_weathersit = X['weathersit'].mode()[0]
        return self

    def transform(self, X):
        df = X.copy()
        # Fill missing values in weathersit
        df['weathersit'].fillna('Clear', inplace=True)
        return df

class MapperOptimal(BaseEstimator, TransformerMixin):
    """Categorical variable mapper."""

    def __init__(self, variables: str, mappings: dict):

        if not isinstance(variables, str):
            raise ValueError("variables should be a str")

        self.variables = variables
        self.mappings = mappings

    def fit(self, X: pd.DataFrame, y: pd.Series = None):
        # we need the fit statement to accomodate the sklearn pipeline
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        X = X.copy()
        #for feature in self.variables:
        X[self.variables] = X[self.variables].map(self.mappings).astype(int)

        return X

class Mapper(BaseEstimator, TransformerMixin):
    """
    Ordinal categorical variable mapper:
    Treat column as Ordinal categorical variable, and assign values accordingly
    """

    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self  # Nothing to fit, so just return self

    def transform(self, X):
        df = X.copy()
        df['yr'] = self.yr_mapping(df['yr'])
        df['mnth'] = self.month_map(df['mnth'])
        df['season'] = self.season_map(df['season'])
        df['weathersit'] = self.weather_map(df['weathersit'])
        df['holiday'] = self.holiday_map(df['holiday'])
        df['workingday'] = self.workday_map(df['workingday'])
        df['hr'] = self.hour_map(df['hr'])
        return df


    def yr_mapping(self,yrc):
        yr_mapping = {2011: 0, 2012: 1}
        return yrc.apply(lambda x: yr_mapping[x])

    def month_map(self,mnc):
        mnth_mapping = {'January': 0, 'February': 1, 'December': 2, 'March': 3, 'November': 4, 'April': 5,
                'October': 6, 'May': 7, 'September': 8, 'June': 9, 'July': 10, 'August': 11}
        return mnc.apply((lambda x: mnth_mapping[x]))

    def season_map(self,snm):
        season_mapping = {'spring': 0, 'winter': 1, 'summer': 2, 'fall': 3}
       # X_train['season'] = X_train['season'].apply(lambda x: season_mapping[x])
        return snm.apply((lambda x: season_mapping[x]))

    def weather_map(self,wrm):
        weather_mapping = {'Heavy Rain': 0, 'Light Rain': 1, 'Mist': 2, 'Clear': 3}
        return wrm.apply((lambda x: weather_mapping[x]))

    def holiday_map(self,hdm):
        holiday_mapping = {'Yes': 0, 'No': 1}
        #X_train['holiday'] = X_train['holiday'].apply(lambda x: holiday_mapping[x])
        return hdm.apply((lambda x: holiday_mapping[x]))

    def workday_map(self,wdm):
        workingday_mapping = {'No': 0, 'Yes': 1}
        #X_train['workingday'] = X_train['workingday'].apply(lambda x: workingday_mapping[x])
        return wdm.apply((lambda x: workingday_mapping[x]))

    def hour_map(self,hrm):
        hour_mapping = {'4am': 0, '3am': 1, '5am': 2, '2am': 3, '1am': 4, '12am': 5, '6am': 6, '11pm': 7, '10pm': 8,
                '10am': 9, '9pm': 10, '11am': 11, '7am': 12, '9am': 13, '8pm': 14, '2pm': 15, '1pm': 16,
                '12pm': 17, '3pm': 18, '4pm': 19, '7pm': 20, '8am': 21, '6pm': 22, '5pm': 23}

        #X_train['hr'] = X_train['hr'].apply(lambda x: hour_mapping[x])
        return hrm.apply((lambda x: hour_mapping[x]))
    

class OutlierHandler(BaseEstimator, TransformerMixin):
    """
    Change the outlier values:
        - to upper-bound, if the value is higher than upper-bound, or
        - to lower-bound, if the value is lower than lower-bound respectively.
    """
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self  # Nothing to fit, so just return self
    
    numerical_features = []
    categorical_features = []
    
    def get_numerical_categorical(self, dataframe):

        for col in dataframe.columns:
            if col not in "cnt":
                if dataframe[col].dtypes == 'float64':
                    self.numerical_features.append(col)
                else:
                    self.categorical_features.append(col)


    def transform(self, X):
      
        df = X.copy()
        self.get_numerical_categorical(df)
        for col in self.numerical_features:
            df = self.handle_outliers(df, col)
        return df


    def handle_outliers(self,dataframe, colm):

        df = dataframe.copy()
        q1 = df.describe()[colm].loc['25%']
        q3 = df.describe()[colm].loc['75%']
        iqr = q3 - q1
        lower_bound = q1 - (1.5 * iqr)
        upper_bound = q3 + (1.5 * iqr)
        for i in df.index:
            if df.loc[i,colm] > upper_bound:
                df.loc[i,colm]= upper_bound
            if df.loc[i,colm] < lower_bound:
                df.loc[i,colm]= lower_bound

        return df



class WeekdayOneHotEncoder(BaseEstimator, TransformerMixin):
    """ One-hot encode weekday column """



    def __init__(self):
        pass

    def fit(self, X, y=None):

        df = X.copy()
        encoder = OneHotEncoder(sparse_output=False)
        encoder.fit(df[['weekday']])
        self.encoder = encoder
        return self  # Nothing to fit, so just return self

    def transform(self, X):

        print('one hot encoder calledddddd')
        df = X.copy()
        
        print('weekday before encoding' , df[['weekday']])
    
        encoded_weekday = self.encoder.transform(df[['weekday']])
        print("encoded_weekday", encoded_weekday)

        # Get encoded feature names
        enc_wkday_features = self.encoder.get_feature_names_out(['weekday'])
        print("enc_wkday_features", enc_wkday_features)

        # Append encoded weekday features to X_train
        df[enc_wkday_features] = encoded_weekday
        
        return df


class UnusedColmnsClass(BaseEstimator, TransformerMixin):
    """ Impute missing values in 'weathersit' column by replacing them with the most frequent category value """
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        unused_colms1 = ['dteday', 'casual', 'registered', 'weekday'] 
        df = X.copy()
        #drop unused columns
        df.drop(labels = unused_colms1, axis = 1, inplace = True)
        return df

