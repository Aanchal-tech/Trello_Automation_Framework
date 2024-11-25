import json

import requests
from employee_prop_req_builder import addEmpDetails, empDetailsParamsBuilder, empDetailsParamsRequestsBuilder
from emp_schemas import Schemas
# from voluptuous import MultipleInvalid, Invalid

emp_details_prop_builder = empDetailsParamsBuilder() \
    .with_emp_name("same") \
    .with_emp_job("lead") \
    .build()

body = empDetailsParamsRequestsBuilder().with_emp_details_requests(emp_details_prop_builder).build()


print(emp_details_prop_builder)
print(body)

body = {
    "name": "morpheus",
    "job": "leader"
}
url ="https://reqres.in/api/users"

r = requests.post(url, data=body)

print(r.text)
print(r)

validate_schemas = Schemas()
r = requests.request(url=url, method='POST', data=body)
# response = {"name":"morpheus","job":"leader","id":"417","createdAt":"2021-10-20T07:27:17.815Z"}
print("^^^^^^^^", validate_schemas.create_emp_record_201_new(json.loads(r.text)))
# json_data = json.loads(response.text)

# try:
#     validate_schemas.create_emp_record_201_new(json.loads(r.text))
#     raise AssertionError('MultipleInvalid not raised')
# except MultipleInvalid as e:
#     exc = e
#     print(exc)

print("*****************", r)
