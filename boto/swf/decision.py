import simplejson

class DecisionAction():
    """Some sort of action taken when a decision is finished"""
    def __str__(self):
        return simplejson.dumps(self.data)


class ScheduleActivityTask(DecisionAction):
    """A decision to schedule a new activity"""

    def __init__(self, decision_task, activity_type_name, activity_type_version, activity_id, activity_input=''):
        self.decision_task          = decision_task
        self.activity_type_name     = activity_type_name
        self.activity_type_version  = activity_type_version
        self.activity_id            = activity_id
        self.activity_input         = activity_input
 
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

class CompleteWorkflowExecution(DecisionAction):
    @property
    def data(self):
        return {
            'decisionType'  : 'CompleteWorkflowExecution'
        }




class Event():
    """ An event that may be returned with a decision """
    def __init__(self, data):
        self._data = data

    @property
    def id(self):
        return self._data['eventId']

    @property
    def type(self):
        return EVENT_TYPE_NAME_MAP[self._data['eventType']]

    @staticmethod
    def parse(data):
        """Create a new Event object given a data dictionary"""
        event_class = EVENT_TYPE_NAME_MAP(data['eventType'])
        return event_class(data)

class ActivityTaskCompleted(Event):
    pass
class ActivityTaskStarted(Event):
    pass
class ActivityTaskCompleted(Event):
    pass
class ActivityTaskScheduled(Event):
    pass
class DecisionTaskCompleted(Event):
    pass
class DecisionTaskScheduled(Event):
    pass
class DecisionTaskStarted(Event):
    pass
class WorkflowExecutionCompleted(Event):
    pass
class WorkflowExecutionStarted(Event):
    pass

EVENT_TYPE_NAME_MAP = {
    'ActivityTaskStarted'           : ActivityTaskStarted,
    'ActivityTaskCompleted'         : ActivityTaskCompleted,
    'ActivityTaskScheduled'         : ActivityTaskScheduled,
    'DecisionTaskCompleted'         : DecisionTaskCompleted,
    'DecisionTaskScheduled'         : DecisionTaskScheduled,
    'DecisionTaskStarted'           : DecisionTaskStarted,
    'WorkflowExecutionCompleted'    : WorkflowExecutionCompleted,
    'WorkflowExecutionStarted'      : WorkflowExecutionStarted,
}

class EventList():
    """A special class for managing access to the events on a decision"""

    def __init__(self, data):
        """Set up the event manager provided the list of event data"""
        self._data = data

    @property
    def types(self):
        """Return a list of the types of events that are in this eventlist"""
        if not hasattr(self, '_types'):
            self._types = self._get_types()
        return self._types

    def _get_types(self):
        """Generate and return the list of types in the events in this EventList"""
        my_types = set()
        for event in self:
            my_types.add( event.type )
        return my_types
    
    def __iter__(self):
        self._i = 0
        return self

    def next(self):
        try:
            result = Event(self._data[self._i])
            self._i += 1
            return result
        except IndexError:
            raise StopIteration
    
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
        self.events = EventList(data['events'])
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
        self.task_list.finish_decision( self, decisions )
        
    def ScheduleActivityTask( self, activity_type_name, activity_type_version, activity_id, activity_input='' ):
        return ScheduleActivityTask( self, activity_type_name, activity_type_version, activity_id, activity_input )
    def CompleteWorkflowExecution( self ):
        return CompleteWorkflowExecution()
