
import sys,os
import warnings
sys.path.append(os.path.abspath(os.path.join('../scripts')))
from file_handler import FileHandler
from df_cleaner import *
from df_selector import *
from df_visualizer import *
from lightgbm import LGBMRegressor
from scripts import *

from train_model import TrainModel

# create a model
model = LGBMRegressor()

train_model = TrainModel(model, "Light GBM Regressor")

train_model.train_sales()
train_model.train_customers()