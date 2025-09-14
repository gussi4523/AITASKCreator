from notion_client import Client
from dotenv import load_dotenv
import json
import os
import re

load_dotenv()

API_KEY = os.getenv("NOTION_API_KEY")
DATABASE_ID_TASK  = os.getenv("DATABASE_ID_TASK")

class Notion():
    def __init__(self):
        self.notion = Client(auth=API_KEY)
        self.DB_TASK = DATABASE_ID_TASK

    def createPage(self,Text,Date,LeadID=None,TeamMate=None,Bold=False,Color="default"):
        properties = {
            "Tasks": {
                "title": [
                    {
                        "text": {
                            "content": Text
                        }
                    }
                ]
            }
        }

        # Add Leads relation only if LeadID is not None or empty string
        if LeadID:
            properties["Lead"] = {
                "type": "relation",
                "relation": [
                    {
                        "id": LeadID
                    }
                ]
            }

        if TeamMate:
            properties["Team"] = {
                "type": "relation",
                "relation": [
                    {
                        "id": TeamMate
                    }
                ]
            }

        properties["Date"] = {
            "type": "date",
            "date": 
                {
                    "start": str(Date)
                }
            
        }

        page = self.notion.pages.create(
            parent={"database_id": self.DB_TASK},
            properties=properties,
            icon={
                "type": "external",
                "external": {
                    "url": "https://www.notion.so/icons/checkmark_red.svg"
                }
            }
        )
        return page["id"]
        print("Page created:", page)