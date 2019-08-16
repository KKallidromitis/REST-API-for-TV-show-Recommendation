import pickle
import numpy as np
from scipy import sparse
import time
import pandas as pd
from lightfm import LightFM
import flask
import urllib.request,json

def loadJSON(url): #Loading JSON from Jikan API to get profile information

    try:
        with urllib.request.urlopen(url) as url:
            output=json.loads(url.read().decode())

        return output
    except urllib.request.HTTPError as err:
        print(err.status)
        if err.status==429:
            output=loadJSON(url)
            return output
        else:
            flask.abort(err.status,'An error has occured :( Please contact me for troubleshooting')

def load_obj(name ):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)

def anime_names(nums,dict_anime):
    a_arr=[]
    for n in nums:
        a_arr.append(dict_anime[n])
    return a_arr

def recommendation_n(model,users,crosstab_mat,dict_anime):
    fav=[]
    rec=[]
    for u in users:
        fav.append(anime_names(crosstab_mat.tocsr()[u].indices[:],dict_anime)[:])
        scores = model.predict(u, np.arange(crosstab_mat.shape[1]))
        top_anime = np.argsort(-scores)
        rec.append(anime_names(top_anime,dict_anime)[:])
    return fav,rec

def make_prediction(username,model,crosstab_mat,dict_anime,dict_user):
    num=list(dict_user.keys())[list(dict_user.values()).index(username)]
    fav,rec=recommendation_n(model,[num],crosstab_mat,dict_anime)
    final=[]
    for n in range(len(rec[0][:])):
        if rec[0][n] not in fav[0]:
            final.append(rec[0][n])
    return(final,fav)

def json_gen(preds,val):
    json_x={}
    json_x[val]=[]
    info=load_obj("anime_info")

    for i in range(len(preds)):
        url="https://myanimelist.net/anime/"+str(preds[i][0])
        index=info[info['anime_id']==preds[i][0]].index.values.astype(int)[0]
        json_x[val].append({
            "title":info["title"][index],
            "image_url":info["image_url"][index],
            "anime_url":url
            })

    return json_x

def fun_profile(username):
    user_url = "https://api.jikan.moe/v3/user/" + username
    data_user = loadJSON(user_url)

    json_u={}
    json_u["profile"]=[]
    json_u["profile"].append({"username":data_user["username"],
                         "profile_url":data_user["url"],
                         "image_url":data_user["image_url"],
                         "anime_stats":data_user["anime_stats"]})
    return json_u


def main(username):
    start = time.time()
    crosstab_mat = load_obj("crosstab")
    dict_user = load_obj("dict_user")
    if username not in dict_user.values():
        end = time.time()
        return 0,end-start,[],[],"Error username not found or not included in the scaled down version of the data"
    dict_anime = load_obj("dict_anime")

    model = load_obj("model")

    f,favs = make_prediction(username,model,crosstab_mat,dict_anime,dict_user)
    final_pred=json_gen(f[:20],"recs")
    print(favs)
    favs=json_gen(favs[0][:10],"favs")
    profile_json=fun_profile(username)
    end = time.time()
    return (1,end-start,profile_json,final_pred,favs)

