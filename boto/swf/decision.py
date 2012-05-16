import simplejson

class DecisionAction():
    """Some sort of action taken when a decision is finished"""
    pass

class ScheduleActivityTask(DecisionAction):
    """A decision to schedule a new activity"""

    def __init__(self, decision_task, activity_type_name, activity_type_version, activity_id, activity_input=''):
        self.decision_task          = decision_task
        self.activity_type_name     = activity_type_name
        self.activity_type_version  = activity_type_version
        self.activity_id            = activity_id
        self.activity_input         = activity_input
 
    def __str__(self):
        return simplejson.dumps(self.data)

    @property
    def data(self):
        return {
            'decisionType'                          : 'ScheduleActivityTask',
            'scheduleActivityTaskDecisionAttributes': {
                'activityId'                        : self.activity_id,
                'activityType'                      : {
                    'name'                          : self.activity_type_name,
                    'version'                       : self.activity_type_version,
                },
                'input'                                 : self.activity_input,
             },
        }

class DecisionTask():
    """
    Example data for a decision task:

{'events': [{'eventId': 1,
             'eventTimestamp': 1337206241.18,
             'eventType': 'WorkflowExecutionStarted',
             'workflowExecutionStartedEventAttributes': {'childPolicy': 'TERMINATE',
                                                         'executionStartToCloseTimeout': '3600',
                                                         'parentInitiatedEventId': 0,
                                                         'taskList': {'name': 'ThumbnailTaskList'},
                                                         'taskStartToCloseTimeout': '3600',
                                                         'workflowType': {'name': 'Thumbnail',
                                                                          'version': '1.2'}}},
            {'decisionTaskScheduledEventAttributes': {'startToCloseTimeout': '3600',
                                                      'taskList': {'name': 'ThumbnailTaskList'}},
             'eventId': 2,
             'eventTimestamp': 1337206241.18,
             'eventType': 'DecisionTaskScheduled'},
            {'decisionTaskStartedEventAttributes': {'scheduledEventId': 2},
             'eventId': 3,
             'eventTimestamp': 1337206241.391,
             'eventType': 'DecisionTaskStarted'}],
 'previousStartedEventId': 0,
 'startedEventId': 3,
 'taskToken': 'AAAAKgAAAAEAAAAAAAAAAeFU+YjFj6pKW4kYYI0e07mfx0jH1O8BLuY1WsNevwKLhHnzkuAKgf90PVmt6FEU1YZsOgVKPNcXk9aQGAIyh/OOVfKaxETdSofzrJJbTbo3Hs2T1tuWUTY3weX9ZeqQZKZqfcDHOlOISiwI74PVUcQa2iRlmHW+DX3cOEFA/t1h6whDwbWkflJ7R2sCrTS2kpro57H57kQBj/1vZn8F9FiluAeC18ujcWfeUUOmFxbr6qJHOzTBVnzh0Iypxeg5xcerR5q+tdnlTrdLkHVsKlo=',
 'workflowExecution': {'runId': 'e1552210-241a-42ec-b87a-eb42e19d7533',
                       'workflowId': 'thumbnail@test13'},
 'workflowType': {'name': 'Thumbnail', 'version': '1.2'}}
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

    def finish( self, decisions ):
        """Finish this decision task and signal the provided decisions"""
        import pdb;pdb.set_trace()
        self.task_list.finish_decision( self, decisions )
        
    def ScheduleActivityTask( self, activity_type_name, activity_type_version, activity_id, activity_input='' ):
        return ScheduleActivityTask( self, activity_type_name, activity_type_version, activity_id, activity_input )
