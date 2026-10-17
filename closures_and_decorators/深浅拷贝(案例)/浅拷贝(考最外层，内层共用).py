import copy
info = [["张三", 18],1, ["李四", 20]]
info_assignment = info


shallow = copy.copy(info)
deep = copy.deepcopy(info)

info[0][1] = 20
info[1] = 2
info[2] = ["王五", 25]

print(info_assignment)
print(shallow)
print(deep)


"""
[["张三", 20], 2,["王五", 25]]
[["张三", 20], 1,["李四", 20]]
[["张三", 18], 1, ["李四", 20]]
"""