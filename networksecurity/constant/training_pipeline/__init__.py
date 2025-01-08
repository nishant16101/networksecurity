import os
import sys
import numpy as np
import pandas as pd

"""Common Constants"""
TARGET_COLUMN = "Result"
PIPELINE_NAME:str = "networksecurity"
ARTIFACT_DIR:str = "Artifacts"
FILE_NAME:str ="phisingData.csv"

TRAIN_FILE_NAME:str= "train.csv"
TEST_FILE_NAME:str = "test.csv"


DATA_INEGESTION_COLLECTION_NAME:str = "NetworkData"
DATA_INEGESTION_DATABASE_NAME:str = "Project_1"
DATA_INEGESTION_DIR_NAME:str = "data_ingestion"
DATA_INEGESTION_FEATURE_STORE_DIR:str = "feature_store"
DATA_INEGESTION_INGESTED_DIR:str = "ingested"
DATA_INEGESTION_TRAIN_TEST_SPLIT_RATIO:float =0.2
