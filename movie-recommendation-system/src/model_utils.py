# Load and save trained model artifacts

import pickle
from pathlib import Path

# project root directory
BASE_DIR=Path(__file__).resolve().parent.parent

# artifacts paths
MOVIES_PATH=BASE_DIR/"data"/"processed"/"movies.pkl"
SIMILARITY_PATH=BASE_DIR/"models"/"similarity.pkl"

# load artifacts(read)
def load_artifacts():
    # load movies
    with open(MOVIES_PATH,'rb') as file:
        movies=pickle.load(file)
    
    # load similarity
    with open(SIMILARITY_PATH,'rb') as file:
        similarity=pickle.load(file)
    
    return movies,similarity


# Save artifacts(write)
def save_artifacts(movies,similarity):
    MOVIES_PATH.parent.mkdir(parents=True,exist_ok=True)
    SIMILARITY_PATH.parent.mkdir(parents=True,exist_ok=True)
    
    with open(MOVIES_PATH,'wb') as file:
        pickle.dump(movies,file)
    
    with open(SIMILARITY_PATH,'wb') as file:
        pickle.dump(similarity,file)
    
    print("Model artifacts saved successfully!")