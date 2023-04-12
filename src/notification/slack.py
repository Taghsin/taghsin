import os
import json
import logging
from random import choice
from urllib import request, parse
from config import configuration

logger = logging.getLogger()
logger.setLevel(logging.INFO)

SLACK_CHANNEL = configuration.SLACK_CHANNEL
SLACK_WEBHOOK_URL = configuration.SLACK_WEBHOOK_URL

def post_to_slack(resource, user, account, region, source):
    """
    Posts a message with a random kitten photo and some context information to a Slack channel using a webhook URL.
    """
    kitten_number = choice(range(1, 100)) # Generates a random integer between 1 and 100
    kitten_url = f"https://cataas.com/cat?width=200&height=200&c={kitten_number}" # Generates a URL to a random kitten photo
    
    data = {
        'channel': SLACK_CHANNEL,
        "attachments": [
            {
                "blocks": [
                    {
                        "type": "section",
                        "fields": [
                            {
                                "type": "mrkdwn",
                                "text": f"*Account :* {account}"
                            },
                            {
                                "type": "mrkdwn",
                                "text": f"*Region =* {region}"
                            },
                            {
                                "type": "mrkdwn",
                                "text": f"*Source Type :* {source}"
                            },
                            {
                                "type": "mrkdwn",
                                "text": f"*Source :* {resource}"
                            },
                            {
                                "type": "mrkdwn",
                                "text": f"*Created By :* {user}"
                            },
                        ],
                        "accessory": {
                            "type": "image",
                            "image_url": kitten_url,
                            "alt_text": "cute kitten"
                        }
                    }
                ]
            }
        ]
    }
    req = request.Request(SLACK_WEBHOOK_URL, method='POST', data=parse.urlencode({'payload': json.dumps(data)}).encode())
    with request.urlopen(req) as response:
        if response.code != 200:
            raise ValueError(f"Failed to post message to Slack: {response.code}")
        else:
            logger.info(f"Message posted to {SLACK_CHANNEL}")

def slack_event(resource, user, account, region, source):
    """
    Posts a message with a random kitten photo and some context information to a Slack channel using a webhook URL.
    """
    try:
        post_to_slack(resource, user, account, region, source)
    except Exception as e:
        logger.error(f"Error in slack_event function: {e}")
