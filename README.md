# REST-API-for-Anime-Recommendation

The main.py is the flask microframework that will be used to deploy the web app and handles the responses of the API.
The algorithm.py includes the machine learning ranking algorithm that is used to process inputs and create outputs.
The valid_usernames.txt includes a list with all the compatible myanimelist website usernames for the API:

[Example Link Deployed on GCP (username=FrostCat)](https://anirec.appspot.com/FrostCat)

!!PLEASE NOTE CURRENTLY API DOES NOT WORK BECAUSE THE MYANIME LIST JIKAN API IS DOWN AND IS UNABLE TO RECIEVE LIVE DATA!!

I have added some JS to display the results on my [github page](https://kkarraskallidromitis.github.io/projects/ainime)


The Jupyter Notebook includes data analytics as well as machine learning algorithms that recommend anime according to a scaled down version of the datset. [Source](https://www.kaggle.com/azathoth42/myanimelist)

Code for the website is on my [personal repo](https://github.com/KKarrasKallidromitis/KKarrasKallidromitis.github.io/tree/master/projects/ainime)
