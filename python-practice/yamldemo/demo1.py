import yaml

# document = """               #yaml格式定义一个字典
#   a: 1
#   b:
#     c: 3
#     d: 4
# """
# print(yaml.safe_load(document))  #safe_load的格式将yaml文件转化为python中的对象加格式

a = yaml.safe_load("""     #yaml格式定义一个列表
 - Hesperiidae
 - Papilionidae
 - Apatelodidae
 - Epiplemidae
 """)
print(a)
