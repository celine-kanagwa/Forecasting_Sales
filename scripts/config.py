from pathlib import Path

class Config:
  RANDOM_SEED = 90
  ASSETS_PATH = Path("../")
  REPO = "../gdrive/1uwV5eeoidgJambZo3n5r9q9OwAko3khW"
  DATASET_FILE_PATH = "Data/train.csv"
  DATASET_PATH = ASSETS_PATH / "Data"
  FEATURES_PATH = ASSETS_PATH / "features"
  MODELS_PATH = ASSETS_PATH / "models"