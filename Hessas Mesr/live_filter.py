import pandas as pd

df = pd.read_csv("C:\\Users\\20812018100700\\working\work\\Hessas_analysis\\full_DF.csv")


g = df.id.str.split("_")


id_list = [g[i][0] for i in range(len(g))]

df["post_id"] = pd.Series(id_list)
df[["id", "post_id"]].sample(5)



ids_list = df.post_id.unique()

from pyfacebook import GraphAPI as gpi
import requests
import json
import time
from datetime import datetime
   
## access  token info
access = {'access_token': 'EAAY9cHPAisUBAEw20ZBsV33oTeCoeyGRAocA8jzbppiV59xqOZAJec33mSYAXxXabc7dbvO6qkD7e8fGXYtSsGWmZBJKs4IRcIIYMWxb7ZAXGOgZCsPde4i70XkjEK263DckcejPbws7KqJ1nAthxGP2bRSoi41LeG1uKSSZAexw5DP93K1ucH',
           'category': 'Education website',
           'category_list': [{'id': '2704', 'name': 'Education website'},
            {'id': '2250', 'name': 'Education'}],
           'name': '??? ??? - Hesas Misr',
           'id': '102899871666500',
           'tasks': ['ANALYZE', 'ADVERTISE', 'MESSAGING', 'MODERATE']}


api = gpi(access_token=access['access_token'])


ids_lis = []


for i in ids_list:
    ids_lis.append("{}_{}".format(access["id"], i))
    


video_result = []
for i in range(len(ids_list)%50):
    video_result.append(api.get_objects(ids = ", ".join( ids_lis[i*50:(i+1)*50] ), fields = "attachments"))
    print(i*50)
    print((i+1)*50)



subjects = [
    "التفاضل والتكامل",
    "الجيولوجيا",
    "الاستاتيكا",
    "الأحياء",
    "الديناميكا",
    "علم النفس والاجتماع",
    "اللغة الإنجليزية",
    "التاريخ",
    "الفيزياء",
    "الكيمياء",
    "الجغرافيا",
    "الجبر والهندسة الفراغية",
    "العربية",
    "الألمانية",
    "الإسبانية",
    "الإيطالية",
    "الإيطالية",
   "الفلسفة",
    ]

video_posts_gen = []
video_posts_id = []
video_posts_res = []
for i in video_result:
    video_posts_res.extend(i.values())
    
n = 0
for i in video_posts_res:
    if "attachments" in i.keys():
        k = i["attachments"]["data"][0]
        if (k['type'] == "video_inline") and ("title" in i["attachments"]["data"][0].keys()):
           if("مادة" in k["title"] or "مراجعة" in k["title"] or "المراجعة" in k["title"]):
               for subject in subjects:
                   if subject in k["title"]:
                       print(subject)
                       video_posts_id.append(i["id"].split("_")[1])
                       video_posts_gen.append(subject)
                       print(k["title"])

data = pd.DataFrame({"video_id":video_posts_id, "genere":video_posts_gen})

video_df = df[df["post_id"].isin(data["video_id"])]
df.drop( video_df.index, axis = 0)
df.reset_index(drop=True, inplace=True)
clean_df = df.drop( video_df.index, axis = 0)

#len(df[df["post_id"].isin(ser)])/len(df)


clean_df.to_csv("C:\\Users\\20812018100700\\working\work\\Hessas_analysis\\hessas_nolive.csv", index = False)



"""
work with video posts
get info

"""


video_df.reset_index(drop=True, inplace=True)
i = 0
data["video_id"].loc[0]
video_df["genere"] = ""




for i in range (len(data)):
    video_df.loc[ video_df[ video_df.post_id == data["video_id"].loc[i]  ].index,"genere"] = data["genere"].iloc[i]

video_df["genere"].sample(10)

video_df.to_csv("C:\\Users\\20812018100700\\working\work\\Hessas_analysis\\hessas_live.csv", index = False)

