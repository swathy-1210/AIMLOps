"""
Note: These tests will fail if you have not first trained the model.
"""
import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

import numpy as np
from bike_sharing_data.config.core import config
from bike_sharing_data.processing.features import WeathersitImputer

'''
#def test_age_variable_transformer(sample_input_data):
    # Given
 #   transformer = age_col_tfr(
        variables=config.model_config.age_var,  # cabin
    )
    assert np.isnan(sample_input_data[0].loc[709,'Age'])

    # When
    subject = transformer.fit(sample_input_data[0]).transform(sample_input_data[0])

    # Then
    assert subject.loc[709,'Age'] == 21
'''

def test_weathersit_variable_transformer(sample_input_data):
    # Given

    
    transformer = WeathersitImputer()
    assert np.isnan(sample_input_data[0].loc[12230,'weathersit'])

    # When
    subject = transformer.fit(sample_input_data[0]).transform(sample_input_data[0])

    # Then
    assert subject.loc[12230,'weathersit'] == 'Clear'




# def setUp(self):
#     self.df = pd.DataFrame({
#         'weathersit': ['clear', 'clear', 'mist', 'mist', 'rain', None, 'clear']
#     })
#     self.imputer = WeathersitImputer()

# def test_fit(self):
#     self.imputer.fit(self.df)
#     self.assertEqual(self.imputer.most_frequent_weathersit, 'clear')

# def test_transform(self):
#     self.imputer.fit(self.df)
#     transformed_df = self.imputer.transform(self.df)
#     expected_df = pd.DataFrame({
#         'weathersit': ['clear', 'clear', 'mist', 'mist', 'rain', 'clear', 'clear']
#     })
#     pd.testing.assert_frame_equal(transformed_df, expected_df)

# print("testing done")

# def test_fit_transform(self):
#     transformed_df = self.imputer.fit_transform(self.df)
#     expected_df = pd.DataFrame({
#         'weathersit': ['clear', 'clear', 'mist', 'mist', 'rain', 'clear', 'clear']
#     })
#     pd.testing.assert_frame_equal(transformed_df, expected_df)
# print("testing done - 2")