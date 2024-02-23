from unittest import TestCase
from gun import Gun
from gun import InvalidPinException


class TestGun(TestCase):
    def test_shoot(self):
        test_gun = Gun()
        assert 0 == (test_gun.check_barrel())
        test_gun.set_pin("1234")
        test_gun.reload()
        test_gun.shoot("1234")
        self.assertEqual(39, (test_gun.check_barrel()))

    def test_reload(self):
        test_second_gun = Gun()
        assert 0 == test_second_gun.check_barrel()
        test_second_gun.reload()
        self.assertEqual(40, test_second_gun.check_barrel())

    def test_that_exception_is_thrown(self):
        test_second_gun = Gun()
        test_second_gun.reload()
        test_second_gun.set_pin("ayo")
        self.assertEqual(40, test_second_gun.check_barrel())
        with self.assertRaises(InvalidPinException) as message:
            test_second_gun.shoot("dayo")
