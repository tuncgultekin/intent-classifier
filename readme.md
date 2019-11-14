# Intent Prediction Api
This project contains 2 different intent prediction models and a Flask based rest interface. The intent prediction models are language independent and the first model makes use of conventional TF.IDF features and a neural network that includes fully connected layers only whereas the second model is a LSTM based deep learning model that uses embeddings.

Only the LSTM based model is integrated to Rest interface, since it exhibits better performance than the conventional model. Please refer to train.ipynb file for model training and test operations.

## Project Structure
- data/: Includes training and test files
- model_artifacts/: Includes trained model artifacts
- train.ipynb: Jupyter Notebook file for model training and test operations
- intent_api_exceptions.py: Http exception classes for Rest service
- intent_classifier.py: Intent prediction model loader and evaluator
- server.py: Rest service api controller
- nltksetup.py: Nltk library setup utility
- requirements.txt: Python Dependencies
- Dockerfile


## Docker Build & Run Commands

### Docker Build:
docker build -t intentapi .

### Docker Run:
docker run -p 8080:8080 intentapi
