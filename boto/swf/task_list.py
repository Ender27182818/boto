from boto.swf.decision import DecisionTask

class TaskList():
    def __init__(self, domain, name):
        self.swf = domain.swf
        self.domain_name = domain.name
        self.name = name

    def get_next_decision(self):
        """Long polling call that will get the next decision or eventually time out and return None"""
        decision_data = self.swf.poll_for_decision_task( self.domain_name, self.name )
        if 'taskToken' not in decision_data: #decision_data['startedEventId'] == 0 and decision_data['previousStartedEventId'] == 0:
            return None
        return DecisionTask(self, decision_data)

    def finish_decision(self, decision_task, decisions):
        """Finish the provided decision task by signaling the provided decisions"""
        decision_text = [d.data for d in decisions] 
        self.swf.respond_decision_task_completed( decision_task.task_token, decision_text )
