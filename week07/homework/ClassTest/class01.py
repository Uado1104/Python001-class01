# _*_ coding : UTF-8 _*_
# 开发团队    : 当场发财科技
# 开发人员    : shenglan
# 开发时间    : 2020-08-05   09:01
# 文件名称    : class01  PY
# 开发工具    : PyCharm


class Zoo:
    def __init__(self, name):
        self.name = name
        self.Cat = []

    def add_animal(self, animal):
        if animal in self.Cat:
            raise Exception("重复输入！")
        else:
            self.Cat.append(animal)





class Animal:
    def __init__(self, style, body, character):
        self.style = style
        self.body = body
        self.character = character

    @property
    def is_fierce(self):
        if self.style == "食肉" and (self.body == "中" or self.body == "大") and self.character == "凶猛":
            return True
        else:
            return False
    # style > meat_ate, grass_ate
    # body > small, middle, big
    # character > warm, fierce
    # is_fierce > style == meat_ate, body >= middle, character == fierce


class Cat(Animal):
    voice = "喵喵喵"

    def __init__(self, name, style, body, character):
        super().__init__(style, body, character)
        self.name = name

    @property
    def is_pet(self):
        if self.character == "温顺" and self.body == "小":
            return True
        else:
            return False
    # voice cls_property
    # is_pet


if __name__ == '__main__':
    z = Zoo('时间动物园')
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    z.add_animal("cat1")
    z.add_animal("cat2")
    z.add_animal("cat2")
    have_cat = getattr(z, 'Cat')
    print(have_cat)
    print(cat1.is_pet)