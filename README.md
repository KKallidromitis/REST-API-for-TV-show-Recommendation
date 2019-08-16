# REST-API-for-Anime-Recommendation
The Jupyter Notebook includes data analytics as well as machine learning algorithms that recommend anime according to a scaled down version of the datset https://www.kaggle.com/azathoth42/myanimelist. Keep in mind the dataset was taken in 2018 and thus some links to the website have been deprecated.

The main.py is the flask microframework that will be used to deploy the web app and handles the responses of the API.
The algorithm.py includes the machine learning ranking algorithm that is used to process inputs and create outputs: Example (username=BlueWolf): https://anirec.appspot.com/BlueWolf (Deployed on GCP).
