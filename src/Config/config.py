import configparser 

config = configparser.ConfigParser()
config.read('config.ini') 

def GetAIURL():
    return config["ai server"]["url"]

def GetAIPrompt(text:str)->str:
    return config["ai server"]["promt"] + text