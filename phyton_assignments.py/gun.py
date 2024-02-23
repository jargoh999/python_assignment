
class InvalidPinException(Exception):
    pass


class Gun:
    __bullet = 0
    __pin = ""

    def reload(self):
        while self.__bullet < 40:
            self.__bullet += 1
        return f"barrel is full boss"

    def check_barrel(self) -> int:
        return self.__bullet

    def set_pin(self, pin: str) -> None:
        self.__pin = pin

    def get_pin(self) -> str:
        return self.__pin

    def shoot(self, pin: str) -> None:
        if self.__bullet > 0 and pin == self.get_pin():
            self.__bullet -= 1
            print(">>>>>>>>>>>>")
        else:
            raise InvalidPinException("enter a valid pin ozuo")

        if self.__bullet < 1:
            print("reloading ---")
            self.reload()


