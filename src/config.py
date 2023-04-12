import os
import boto3 



def get_config_value(parameter_path):
    # Initialize the AWS SDK for Python
    ssm = boto3.client('ssm')
    
    # Retrieve the parameter value from Parameter Store
    response = ssm.get_parameter(
        Name=parameter_path,
        WithDecryption=True
    )
    
    # Extract the value from the response
    parameter_value = response['Parameter']['Value']
    
    # Return the parameter value
    return parameter_value


class Settings:

    def __init__(self):
        self.IGNORED_USERS = get_config_value(os.getenv("IGNORED_USERS", [])) # _terraform

        # slack
        self.SLACK_WEBHOOK_URL = get_config_value(os.getenv("SLACK_WEBHOOK_URL", None))
        self.SLACK_CHANNEL = get_config_value(os.getenv("SLACK_CHANNEL", None))

        # microsoft teams
        self.TEAMS_CHANNEL = get_config_value(os.getenv("TEAMS_CHANNEL", None))
        self.TEAMS_WEBHOOK_URL = get_config_value(os.getenv("TEAMS_WEBHOOK_URL", None))


configuration = Settings()
