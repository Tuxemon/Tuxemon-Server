
# All controllers/handlers should implement this protocol.
class AbstractHandler(object):
    def __init__(self):
        self.event_type = "EVENT_TYPE"
        self.required_fields = []

    def _has_required_fields(self, event):
        """Verifies that the given event has the required fields for this handler.
        """
        has_fields = True
        for field in self.required_fields:
            if type(event.target) != dict:
                has_fields = False
                break
            if field not in event.target.keys():
                has_fields = False

        return has_fields


    def invoke(self, event):
        """Invoke should return a result, warning, and error response.
        """
        pass
