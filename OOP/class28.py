class Text(str):
    def duplicate(self):
        return self + self


text = Text("ECEN429 rocks!")
print(text.duplicate())
