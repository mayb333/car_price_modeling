import catboost
from src.data import Data

model = catboost.load_model("src/artifacts/catboost_model")
data_processor = Data()