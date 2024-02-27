import unittest
from entry import Entry

from Diary import EntryIdNotFoundException, Diary


class DiaryTest(unittest.TestCase):
    diary = Diary("ayo", "password")

    def test_that_diary_is_unlocked_is_locked_is_false(self):
        diary = Diary("ayo", "password")
        self.assertFalse(diary.is_locked())

    def test_that_diary_can_be_locked_diary_is_locked(self):
        diary = Diary("ayo", "password")
        self.assertFalse(diary.is_locked())
        self.diary.lockDiary()
        self.assertTrue(self.diary.is_locked())

    def test_that_diary_can_be_unlocked_diary_is_unlocked(self):
        diary = Diary("ayo", "password")
        self.diary.lockDiary()
        self.assertTrue(self.diary.is_locked())
        self.diary.unlockDiary("password")
        self.assertFalse(self.diary.is_locked())


class DiaryFunctionTest(unittest.TestCase):
    def setUp(self):
        self.diary = Diary("ayo", "1234")
        self.diary.entries.clear()
    def test_that_entry_can_be_created_entry_is_created(self):
            self.diary.lockDiary()
            self.assertTrue(self.diary.is_locked())
            self.diary.unlockDiary("1234")
            self.assertFalse(self.diary.is_locked())
            self.diary.createEntry("title", "body")
            self.assertEqual(1, self.diary.getNumberOfEntryInDiary())

    def test_that_entry_can_be_found(self):
            self.diary.lockDiary()
            self.assertTrue(self.diary.is_locked())
            self.diary.unlockDiary("1234")
            self.assertFalse(self.diary.is_locked())
            self.diary.createEntry("title", "body")
            self.diary.createEntry("title1", "body1")
            entryToReturn = self.diary.findEntryById(1)
            self.assertEqual(self.diary.entries[0], entryToReturn)
            self.assertRaises(EntryIdNotFoundException, lambda: self.diary.findEntryById(-1))

    def test_that_entry_can_be_deleted(self):
            self.diary.lockDiary()
            self.assertTrue(self.diary.is_locked())
            self.diary.unlockDiary("1234")
            self.assertFalse(self.diary.is_locked())
            self.diary.createEntry("title", "body")
            self.diary.createEntry("title1", "body1")
            self.diary.deleteEntry(1)
            self.assertEqual(1, self.diary.getNumberOfEntryInDiary())

    def test_that_entry_can_be_updated(self):
            self.diary.lockDiary()
            self.assertTrue(self.diary.is_locked())
            self.diary.unlockDiary("1234")
            self.assertFalse(self.diary.is_locked())
            self.diary.createEntry("title", "body")
            self.diary.createEntry("title1", "body1")
            self.diary.updateEntry(1, "newTitle", "newBody")
            self.assertEqual(self.diary.entries[0].getBody(), "newBody")

    def test_that_negative_id_cant_be_found(self):
            diary = Diary("ayo", "password")
            self.diary.lockDiary()
            self.assertTrue(self.diary.is_locked())
            self.diary.unlockDiary("1234")
            self.assertFalse(self.diary.is_locked())
            self.diary.createEntry("title", "body")
            self.diary.createEntry("title1", "body1")
            self.assertRaises(EntryIdNotFoundException, lambda: self.diary.findEntryById(-1))

    def test_add_three_entry_remove_one_find_the_removed_entry(self):
            self.diary.lockDiary()
            self.assertTrue(self.diary.is_locked())
            self.diary.unlockDiary("1234")
            self.assertFalse(self.diary.is_locked())
            self.diary.createEntry("title", "body")
            self.diary.createEntry("title1", "body1")
            self.diary.createEntry("title2", "body2")
            self.diary.deleteEntry(2)
            self.assertRaises(EntryIdNotFoundException, lambda: self.diary.findEntryById(2))
