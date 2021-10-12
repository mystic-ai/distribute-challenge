import neuro-pipeline as pipe
from neuro-pipeline.objects import NpuModel
from neuro-pipeline.frameworks import XgboostModel

import numpy as np
import pandas as pd
import xgboost as xgb

# Run the following in your terminal
# mkdir 'data'
# curl 'https://raw.githubusercontent.com/agconti/kaggle-titanic/master/data/train.csv -o ./data/train.csv'
# curl 'https://raw.githubusercontent.com/agconti/kaggle-titanic/master/data/test.csv -o ./data/test.csv'

train = pd.read_csv("./data/train.csv")
test = pd.read_csv("./data/test.csv")
X_y_train = xgb.DMatrix(data=train[['Pclass', 'Age', 'Fare', 'SibSp', 'Parch']], label=train['Survived'])
X_test = xgb.DMatrix(data=test[['Pclass', 'Age', 'Fare', 'SibSp', 'Parch']])

params = {'base_score':np.mean(train['Survived']),
          'eta':0.1,
          'max_depth':3,
          'gamma':3,
          'objective':'reg:linear',
          'eval_metric':'mae'}

@pipe.artifacts([XgboostModel('model')])
class MyModel(NpuModel):
    def __init__(self):
        super().__init__()

    def prediction(self, x):
        out = self.model.predict(x)
        return out

    def run(self, x):
        out = self.prediction(x)
        return out

xgb_model = xgb.train(params=params,dtrain=X_y_train,num_boost_round=3)

model = MyModel()
model.artifacts({'model': xgb_model})

out = model.run(X_test)