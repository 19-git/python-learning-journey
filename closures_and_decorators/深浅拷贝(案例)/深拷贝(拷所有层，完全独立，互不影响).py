import copy
user = {"id":1, "info":{"score":[90,85]}}

user_copy = copy.copy(user)
user_deep = copy.deepcopy(user)

user["info"]["score"][0] = 85


print(user)
print(user_copy)
print(user_deep)

"""
{"id":1, "info":{"score":[85,85]}}
{"id":1, "info":{"score":[85,85]}}
{"id":1, "info":{"score":[90,85]}}
"""