class TaskList():
    def __init__(self, domain, name):
        self.swf = domain.swf
        self.domain_name = domain.name
        self.name = name

    def get_next_decision(self):
        """Long polling call that will get the next decision or eventually time out and return None"""
        return self.swf.poll_for_decision_task( self.domain_name, self.name )
