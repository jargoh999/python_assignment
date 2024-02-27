from Diaries import Diaries
from entry import Entry


class EntryIdNotFoundException(Exception):
    def __init__(self, message):
        super().__init__(message)


class IncorrectPasswordException(Exception):
    def __init__(self, message):
        super().__init__(message)


def main():
    di = Diary("AYO", "PASSWORD")
    di.createEntry("title", "body")
    di.createEntry("title1", "body1")
    di.createEntry("title2", "body2")
    dee = Diaries()
    dee.add_diary(di)
    print(dee)


class Diary:
    isLocked = False
    entries = []
    entryId = 1

    def __init__(self, userName=None, password=None):
        self.password = password
        self.userName = userName

    def is_locked(self):
        return self.isLocked

    def lockDiary(self) -> None:
        self.isLocked = True

    def unlockDiary(self, password):
        if self.isValid(password):
            self.isLocked = False
        else:
            raise IncorrectPasswordException("oga your password is incorrect")

    def isValid(self, password):
        return password == self.password

    def createEntry(self, title, body):
        entry = Entry(self.entryId, title, body)
        self.entries.append(entry)
        self.entryId += 1

    def getNumberOfEntryInDiary(self):
        return len(self.entries)

    def findEntryById(self, entryId):
        for entry in self.entries:
            if entry.getId() == entryId:
                return entry
        raise EntryIdNotFoundException("these id wey u enter no dey here oh oga")

    def deleteEntry(self, entryId):
        self.entries.remove(self.findEntryById(entryId))

    def updateEntry(self, entryId, newTitle, newBody):
        entryToUpdate = self.findEntryById(entryId)
        entryToUpdate.setBody(newBody)
        entryToUpdate.setTitle(newTitle)

    def getUserName(self):
        return self.userName

    def __repr__(self):
        return str(self.entries)


if __name__ == "__main__":
    diary = Diary()
    main()
