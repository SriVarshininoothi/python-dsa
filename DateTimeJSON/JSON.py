
#Convert into python

import json
x = '{"name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(x)



# Python into json

import json
x={"name":"John","age":30,"city":"New York"}
y = json.dumps(x)
print(y)


