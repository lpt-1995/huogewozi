import yaml


class Animal:
    name: str = "小黑"
    colour: str = "黑色"
    age: int = 4
    sex: str = "公"

    def call(self):
        print(f"{self.name} 会叫")

    def run(self):
        print(f"{self.name} 会跑")

    def __init__(self, name, colour, age, sex):
        self.name = name
        self.colour = colour
        self.age = age
        self.sex = sex


class Cat(Animal):
    hair = "短毛"

    def __init__(self, hair, name, colour, age, sex):
        self.hair = hair
        super().__init__(name, colour, age, sex)

    def skill1(self):
        print(f"{self.name}技能是抓老鼠")

    def call(self):
        print(f"{self.name}喵喵叫")


class Dog(Animal):
    hair = "长毛"

    def __init__(self, hair, name, colour, age, sex):
        self.hair = hair
        super().__init__(name, colour, age, sex)

    def skill2(self):
        print(f"{self.name}技能是会看家")

    def call(self):
        print(f"{self.name}喵喵叫")


if __name__ == '__main__':
    with open("animal.yaml", encoding="UTF-8") as f:
        animal = yaml.safe_load(f)
        hair = animal['cat']['hair']
        name = animal['cat']['name']
        color = animal['cat']['colour']
        age = animal['cat']['age']
        gender = animal['cat']['sex']

mm = Cat("长毛", "阿狸", "黄白条纹", "3", "母")
mm.skill1()
print(f"{mm.name}的毛发是{mm.hair},颜色是{mm.colour},今年{mm.age}岁,性别是{mm.sex}")

gg = Dog("短毛", "阿黄", "黄色", "3", "公")
gg.skill2()
print(f"{gg.name}的毛发是{gg.hair},颜色是{gg.colour},今年{gg.age}岁,性别是{gg.sex}")
