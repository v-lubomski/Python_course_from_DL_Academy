# Самостоятельно познакомиться с паттернами Factory (фабрика) и Factory method (фабричный метод)
# и решить следующую задачу:
# «Есть некоторый общий класс родитель Tag, который хранит в себе какой-то HTML тег (например: <tag></tag>).
# От Tag наследуются еще четыре класса Image, Input, Text (т. е <p></p>), Link (т. е <a></a>).
# С использованием указанных паттернов реализовать следующее поведение:
# Должна быть возможность создать необходимый тег, явно его не создавая, т. е не через img = Image(),
# а через фабричный метод или фабрику, например factory.create_tag (name).»

# *Дополнительно:
# Реализовать возможность опциональной передачи атрибутов для тегов, т. е атрибуты могут быть
# (src для image, href для a и. т. д.) , а могут и не быть.


class Tag:
    def __init__(self, attributes_dict=None):
        self.tag = 'tag'
        for k, v in attributes_dict.items():
            setattr(self, k, v)

    def get_html(self):
        return '<{tag}></{tag}>'.format(tag=self.tag)


class Image(Tag):
    def __init__(self, attributes_dict=None):
        super().__init__(attributes_dict)
        self.tag = 'img'

    def get_html(self):
        return '<{}>'.format(self.tag)


class Input(Tag):
    def __init__(self, attributes_dict=None):
        super().__init__(attributes_dict)
        self.tag = 'input'


class Text(Tag):
    def __init__(self, attributes_dict=None):
        super().__init__(attributes_dict)
        self.tag = 'p'


class Link(Tag):
    def __init__(self, attributes_dict=None):
        super().__init__(attributes_dict)
        self.tag = 'a'


class TagFactory:
    @staticmethod
    def create_tag(tag_name, attrs_dict):
        if tag_name == 'image':
            return Image(attrs_dict)
        elif tag_name == 'input':
            return Input(attrs_dict)
        elif tag_name == 'p':
            return Text(attrs_dict)
        elif tag_name == 'a':
            return Link(attrs_dict)
        elif tag_name == '':
            return Tag(attrs_dict)
        else:
            return Tag(attrs_dict)


factory = TagFactory()
elements = {'image': {'name': 'logo', 'src': '/src/logo.jpeg'},
            'input': {'name': 'Кнопка "Подтвердить"', 'alt': 'Подтвердить'},
            'p': {'align': 'center'}, 'a': {'href': 'www.wikipedia.com'}, '': {}}
for tag_name, attrs in elements.items():
    print(factory.create_tag(tag_name, attrs).get_html())


# Определил считывание и установку атрибутов для экземпляров.
# Нужно:
# 1. Формировать полноценный html с атрибутами тега.
# 1.1 Понять, как достать только пользовательские атрибуты из экземпляра.
# 1.2 Описать необходимый функционал в Tag.get_html
# 1.2.1 Добавлять каждый пользовательский атрибут экземпляра с пробелом перед ним к тегу <tag attr="value">
# 2. Сделать расширение (дополнение) функционала из 1.1 в дочернем классе Image - для одиночного тега
