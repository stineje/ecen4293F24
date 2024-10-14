from abc import ABC, abstractmethod


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("TextBox")


class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")


def draw(control):
    control.draw()


ddl = DropDownList()
textbox = TextBox()
print(isinstance(ddl, UIControl))
draw(ddl)
draw(textbox)
