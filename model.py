import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import logging

class Model():
  __instance = None

  @staticmethod
  def get_instance():
    if Model.__instance == None:
      Model.__instance = Model()
      Model.__instance.fit()
    return Model.__instance

  def __init__(self):
    self.model = None
    self.data = None

  def fit(self):
    file_path = './melb_data.csv'
    self.data = pd.read_csv(file_path)
    logging.info(f"Length of dataset {len(self.data)}")
    self.data = self.data.dropna(axis=0)
    features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
    y = self.data.Price
    X = self.data[features]
    train_X, test_X, train_y, test_y = train_test_split(X, y, random_state=1)
    self.model = RandomForestRegressor(random_state=1)
    self.model.fit(train_X, train_y)
    # logging.info(self.model.predict(test_X))

  def predict(self, data):
    df = pd.DataFrame.from_dict(data, orient='columns')
    prediction = self.model.predict(df)
    # logging.info(prediction)
    return prediction

  def add_data(self, data):
    df = pd.DataFrame.from_dict(data, orient='columns')
    df.to_csv(path_or_buf='./melb_data.csv', mode='a',header=False)
    self.fit()
    return True

