from datetime import datetime


class Entry:
    def __init__(self, id, title, body):
        self.id = id
        self.title = title
        self.body = body
        self.dateCreated = datetime.now().date()
        self.timeCreated = datetime.now().time().replace(microsecond=0)

    def getId(self):
        return self.id

    def getDateCreated(self):
        return self.dateCreated

    def setBody(self, body):
        self.body = body

    def getBody(self):
        return self.body

    def getTimeCreated(self):
        return self.timeCreated

    def setTitle(self, title):
        self.title = title

    def getTitle(self):
        return self.title

    def __repr__(self):
        return f"{self.id}  {self.body}  {self.title}  {self.dateCreated} {self.timeCreated}"


if __name__ == "__main__":
    entry = Entry(1, "am", "a")
    entry1 = Entry(1, "am a ", "boy")
    print(entry)
    print(entry1)
