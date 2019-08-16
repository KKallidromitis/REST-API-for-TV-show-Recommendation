# REST-API-for-Anime-Recommendation

The main.py is the flask microframework that will be used to deploy the web app and handles the responses of the API.
The algorithm.py includes the machine learning ranking algorithm that is used to process inputs and create outputs.
The valid_usernames.txt includes a list with all the compatible myanimelist website usernames for the API:

Example (username=FrostCat): https://anirec.appspot.com/FrostCat

API General Link: https://anirec.appspot.com/<insert_username> (Deployed on GCP)

I have added some JS to display the results on my github page: https://kkarraskallidromitis.github.io./arec

The Jupyter Notebook includes data analytics as well as machine learning algorithms that recommend anime according to a scaled down version of the datset https://www.kaggle.com/azathoth42/myanimelist. The dataset was extracted in 2018 and thus some links to the website might have been deprecated.
