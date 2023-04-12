import os
import json
import logging
from random import choice
from urllib import request, parse
from config import configuration

logger = logging.getLogger()
logger.setLevel(logging.INFO)

TEAMS_CHANNEL = configuration.TEAMS_CHANNEL
TEAMS_WEBHOOK_URL = configuration.TEAMS_WEBHOOK_URL

def post_to_teams(resource, user, account, region, source):
    """
    Posts a message with a random kitten photo and some context information to a Microsoft Teams channel using a webhook URL.
    """
    kitten_number = choice(range(1, 100)) # Generates a random integer between 1 and 100
    kitten_url = f"https://cataas.com/cat?width=200&height=200&c={kitten_number}" # Generates a URL to a random kitten photo
    
    data = {
        "type": "message",
        "attachments": [
            {
                "contentType": "application/vnd.microsoft.card.adaptive",
                "content": {
                    "type": "AdaptiveCard",
                    "version": "1.0",
                    "body": [
                        {
                            "type": "Container",
                            "items": [
                                {
                                    "type": "Image",
                                    "url": kitten_url,
                                    "altText": "cute kitten"
                                }
                            ]
                        },
                        {
                            "type": "Container",
                            "items": [
                                {
                                    "type": "TextBlock",
                                    "text": f"Account : {account}",
                                    "wrap": True
                                },
                                {
                                    "type": "TextBlock",
                                    "text": f"Region : {region}",
                                    "wrap": True
                                },
                                {
                                    "type": "TextBlock",
                                    "text": f"Source Type : {source}",
                                    "wrap": True
                                },
                                {
                                    "type": "TextBlock",
                                    "text": f"Source : {resource}",
                                    "wrap": True
                                },
                                {
                                    "type": "TextBlock",
                                    "text": f"Created By : {user}",
                                    "wrap": True
                                }
                            ]
                        }
                    ]
                }
            }
        ]
    }
    data = json.dumps(data).encode('utf-8')
    headers = {
        'Content-Type': 'application/json'
    }
    req = request.Request(TEAMS_WEBHOOK_URL, data=data, headers=headers, method='POST')
    with request.urlopen(req) as response:
        if response.status != 200:
            raise ValueError(f"Failed to post message to Teams: {response.status}")
        else:
            logger.info(f"Message posted to {TEAMS_CHANNEL}")

def teams_event(resource, user, account, region, source):
    """
    Posts a message with a random kitten photo and some context information to a Microsoft Teams channel using a webhook URL.
    """
    try:
        post_to_teams(resource, user, account, region, source)
    except Exception as e:
        logger.error(f"Error in teams_event function: {e}")
