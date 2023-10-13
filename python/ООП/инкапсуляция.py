class Kettle:

    def turn_on(self):
        self._boil()
        self.__check_temperature()
        self.beep()

    def _boil(self):
        print('Нагревание воды')

    def __check_temperature(self):
        print('Проверяем температуру воды')

    def beep(self):
        print('Подаем звуковой сигнал')

    def turn_off(self):
        print('Автоматическое выключение')


my_kettle = Kettle()
#  Можем обращаться к методам с уровнем инкапсуляции protected "_boil"
my_kettle._boil()
#  Не можем обращаться к методам с уровнем инкапсуляции private "__check_temperature"
my_kettle.__check_temperature()
