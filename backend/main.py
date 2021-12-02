from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from starlette.responses import RedirectResponse
import pprint
import jwt
import json 
import os 

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Mounting default Vue files after running npm run build 
app.mount("/dist", StaticFiles(directory="dist/"), name="dist")
app.mount("/css", StaticFiles(directory="dist/css"), name="css")
#app.mount("/img", StaticFiles(directory="dist/img"), name="img")
app.mount("/js", StaticFiles(directory="dist/js"), name="js")

templates = Jinja2Templates(directory="dist")

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/helloWorld")
def helloWorld(request: Request):
    return jsonable_encoder({'text': 'Hello World'})

@app.post("/webhook")
async def webhook(request: Request):
    import paho.mqtt.client as mqtt #import the client1

    print('got post event')
    try:
        data = await request.body()
    except RuntimeError:
        data = "Receive channel not available"
        response = JSONResponse({"json": data})

    print("===========================")
    #decoded = jwt.decode(data, PUBLIC_KEY, algorithms=["RS256"]) 
    #payload = json.loads((decoded['data']))
    broker_address="test.mosquitto.org" 
    client = mqtt.Client("ldu123456") #create new instance
    client.connect(broker_address) #connect to broker
    client.publish("test/test/ldu","Received post")#publish
    # Send mqtt message 
    # Check daily Sales 
    #wix.getDailySales()
    return jsonable_encoder({'status': 'true'}), 200
