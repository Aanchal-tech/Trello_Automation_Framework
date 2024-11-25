from voluptuous import Schema, Required, All, Any, Length, Object, Optional

# {"name":"morpheus","job":"leader","id":"417","createdAt":"2021-10-20T07:27:17.815Z"}
class Schemas:

    def __init__(self):

        self.create_emp_record_201 = Schema(Object(
            {
            Required('http_code'):201,
            Required('name'): All(str),
            Required('job'): All(str),
            Required('id'): All(str),
            Required('createdAt'): All(str),
            # Required('createdAt'): Any(None, str, int, list),
        }))
        self.create_emp_record_201_new = Schema(
            {
                # Required('http_code'): 201,
                Required('name'): All(str),
                Required('job'): All(str),
                Required('id'): All(str),
                Required('createdAt'): All(str),
                # Required('createdAt'): Any(None, str, int, list),
            })


