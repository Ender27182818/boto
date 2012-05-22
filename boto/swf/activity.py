import simplejson

class ActivityTask():
    """
    Example data for an activity task:

    {'activityId': 'a-b-c',
     'activityType': {'name': 'GenerateThumbnail', 'version': '1.0'},
     'input': '/a/b/c',
     'startedEventId': 6,
     'taskToken': 'AAAAKgAAAAEAAAAAAAAAAab9taY9Rxzt50tYLodLe0DdvZ0d1rF/5/vjUqJ3rCAKhUqafeC1+eAmOmTbq3RHMlkI1G2y1bU69M8p93SqzwHVeBa9S7I6tzKO9aRz3QR2qKEjqyL+VHq5ClwyAroGMmA7gIztc/V+l2ofqnvZppQy+6VJP4H4BlaISfiQWDnN7koBR3oKT8Mml8PUuEwyXpz8BKgdiQiBW3F9+ZjKA1VXPEeXx+fthpVLAaZmrsA+LgSBQeUtba4qy4HmiVBcwp19aXf4jI2Z7n32oXPTy7E=',
     'workflowExecution': {'runId': '54c7f5eb-2a57-41c1-bbb7-25c647994397',
                           'workflowId': 'thumbnail@test21'}}
    """
    def __init__(self, task_list, data):
        self.task_list = task_list
        self._data = data
    

    @property
    def workflow_id(self):
        return self._data['workflowExecution']['workflowId']

    @property
    def run_id(self):
        return self._data['workflowExecution']['runId']
 
    @property
    def task_token(self):
        return self._data['taskToken']

    @property
    def input(self):
        return self._data['input']

    def finish( self, status ):
        """Finish this decision task and signal the provided decisions"""
        self.task_list.finish_activity( self, status )
