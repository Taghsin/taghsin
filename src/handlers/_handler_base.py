class HandlerBase:
    events = {}

    def __init__(self, event, user):
        self.event = event
        self.user = user

    def handler(self):
        event_name = self.event['detail']['eventName']

        event_handler = self.events.get(event_name, None)
        if event_handler:
            event_handler(self.event, self.user)
        else:
            print("We will improve with other versions")
