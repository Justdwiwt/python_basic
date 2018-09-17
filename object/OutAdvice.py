# ！ /usr/bin/python3
# -*-coding:UTF-8-*-

from object.WeatherSearch import WeatherSearch


class OutAdvice(WeatherSearch):
    def __init__(self, input_daytime):
        WeatherSearch.__init__(self, input_daytime)

    def search_temperature(self):
        vehicle = ''
        if self.input_daytime == 'daytime':
            vehicle = 'bike'
        if self.input_daytime == 'night':
            vehicle = 'taxi'
        return vehicle

    def out_advice(self):
        visible_leave = self.search_visibility()
        if visible_leave == 2:
            print('weather is good , suitable for use %s.' % self.search_temperature())
        elif visible_leave == 9:
            print('weather is bad , you should use %s.' % self.search_temperature)
        else:
            print('weather is beyond my scope , I can not give you any advice')


if __name__ == '__main__':
    check = OutAdvice('daytime')
    check.out_advice()
