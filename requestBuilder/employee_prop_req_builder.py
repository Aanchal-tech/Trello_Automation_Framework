class addEmpDetails:
    def __init__(self):
        self.name =""
        self.job =""


class empDetailsParamsBuilder:
    def __init__(self):
        self.empDetails = addEmpDetails()

    def with_emp_name(self, name):
        self.empDetails.name = name
        return self

    def with_emp_job(self, job):
        self.empDetails.job = job
        return self

    def build(self):
        return self.empDetails.__dict__


class empDetailsParamsRequestsBuilder:
    def __init__(self):
        self.emp_obj = empDetailsParamsBuilder()
        self.emp_obj.empDetails = empDetailsParamsBuilder().build()

    def with_emp_details_requests(self, emp_obj):
        self.emp_obj.empDetails = emp_obj
        return self

    def build(self):
        return self.emp_obj.__dict__