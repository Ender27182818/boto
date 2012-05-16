import boto.swf.task_list

class Domain():
    """An SWF domain"""
    def __init__(self, swf, domain_name):
        self.swf = swf
        self.name = domain_name


    def start_workflow(self, workflow_id, workflow_name, workflow_version):
        return self.swf.start_workflow_execution( self.name, workflow_id, workflow_name, workflow_version )

    def task_list(self, task_list_name):
        return boto.swf.task_list.TaskList( self, task_list_name)
