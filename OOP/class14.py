class Sqrt:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags)


sqrt = Sqrt()
sqrt.add('python')
sqrt.add('Python')
sqrt.add('square root')
sqrt["python"]
sqrt["python"] = 10
print(sqrt.tags)
