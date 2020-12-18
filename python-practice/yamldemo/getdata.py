import yaml


def get_datas():
    with open('data.yaml', encoding='utf-8') as f:
        datas = yaml.safe_load(f)  # safe_load 将yaml数据流转化为python对象
    return datas


print(get_datas())

a = yaml.safe_dump({'languages': ['Ruby', 'Perl', 'Python'],
                    'websites': {'YAML': 'yaml.org', 'Ruby': 'ruby-lang.org', 'Python': 'python.org',
                                 'Perl': 'use.perl.org'}})  # yaml.safe_dump()  将python对象转化为yaml数据格式
print(a)
