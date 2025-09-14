from flask import Flask, request, jsonify
import requests
from src.Config.config import GetAIURL,GetAIPrompt
from src.NotionAPI.notion import Notion

notion = Notion()
app = Flask(__name__)

@app.get("/")
def Home():
    return "home"

@app.post("/ai/chat")
def generate():
    data = request.get_json()
    print(data)
    url = GetAIURL()
    message = GetAIPrompt(data["text"])
    responseAI = requests.post(url=url,json={"message":message}).json()
    if data["IDType"] == "Team":
        page = notion.createPage(Text=responseAI["reply"],Date=str(data["date"]),TeamMate=data["Id"])
        return jsonify({"reply":f"Teammate's task was added by id of {page}, on date: {data["date"]}"})
    elif data["IDType"] == "Lead":
        page = notion.createPage(Text=responseAI["reply"],Date=str(data["date"]),LeadID=data["Id"])
        return jsonify({"reply":f"Lead's task was added by id of {page}, on date: {data["date"]}"})

    
app.run(debug=True,port=8080)