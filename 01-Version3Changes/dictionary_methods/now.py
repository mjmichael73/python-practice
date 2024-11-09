dic = {1: "One", 2: "Two"}
keys = dic.keys()
# keys.sort()  # Error
# keys is dict_keys
values = list(dic.values())
values.sort()

print("Keys are: ", keys)
print("Keys type is: ", type(keys))
print("Values are : ", values)
print("Values type is : ", type(values))