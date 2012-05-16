class DecisionTask():
    """
    Example data for a decision task:

{'previousStartedEventId': 0, 'workflowExecution': {'workflowId': 'thumbnail@-eli-test3', 'runId': 'e56e9b8e-788c-428f-9824-2e8cba7a0cf2'}, 'startedEventId': 3, 'workflowType': {'version': '1.2', 'name': 'Thumbnail'}, 'events': [{'eventId': 1, 'eventType': 'WorkflowExecutionStarted', 'workflowExecutionStartedEventAttributes': {'taskList': {'name': 'ThumbnailTaskList'}, 'parentInitiatedEventId': 0, 'taskStartToCloseTimeout': '3600', 'childPolicy': 'TERMINATE', 'executionStartToCloseTimeout': '3600', 'workflowType': {'version': '1.2', 'name': 'Thumbnail'}}, 'eventTimestamp': 1337186157.838}, {'eventId': 2, 'eventType': 'DecisionTaskScheduled', 'decisionTaskScheduledEventAttributes': {'startToCloseTimeout': '3600', 'taskList': {'name': 'ThumbnailTaskList'}}, 'eventTimestamp': 1337186157.838}, {'eventId': 3, 'decisionTaskStartedEventAttributes': {'scheduledEventId': 2}, 'eventTimestamp': 1337187977.553, 'eventType': 'DecisionTaskStarted'}], 'taskToken': 'AAAAKgAAAAEAAAAAAAAAAeIiGiJNausk3GXpBMvNTeO8+FNwFRCOG5SY+630ARlworccaWRplGwTMcyqTKK7JDyFaeH0+82VxBx/CIETMaYrT7KBiUjNnEBpLBMNRhnUY1AN1c0eSL0WHAxvAXJG4UTAkUB1NN0gMLAdPWq/AMU3EDGE7g1niR6TAMbu4FIOZoF7ekvnbXrtbkj4SsbE8BLEHcxwlRyIP19OszD0p3WcqY4F2DLcH27bl46Z9plj9tW6N851t++e8o2ezCJa/1jBo935IISDqx4965Lz9kU='}
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
        
