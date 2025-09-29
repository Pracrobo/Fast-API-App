from fastapi import FastAPI, Body

app = FastAPI()
data_list = [
    {"list_id" : 1, "osp_name" : "known", "url" : "www.naver.com", "country" : "Korea"},
    {"list_id" : 2, "osp_name" : "known", "url" : "www.google.com", "country" : "American"},
    {"list_id" : 3, "osp_name" : "known", "url" : "www.amazon.com", "country" : "American"},
    {"list_id" : 4, "osp_name" : "known", "url" : "www.daum.com", "country" : "Korea"},
    {"list_id" : 5, "osp_name" : "known", "url" : "www.github.com", "country" : "American"},
]


@app.get("/")
def home():
    p = "welcome to Webpage"
    return p

@app.post("/list/{list_id}")
def add_list(Item=Body()):
    print(Item)
    data_list.append(Item)
    return "OK"


@app.get("/list")
def get_list_all():
    return data_list 