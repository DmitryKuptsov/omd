class JsonToPy():
    def __init__(self, json_object):
        for i in json_object:
            self.__dict__[i] = json_object[i]


lesson_str = {"title": "python",
              "price": 5, "location": {
                "address": "город Москва, Лесная, 7",
                "metro_stations": ["Белорусская"]}}


class ColorizeMixin:
    def __repr__(self) -> str:
        return f'\033[1;33;40m {self.title} | {self.price} ₽'


class Advert(ColorizeMixin, JsonToPy):
    def __init__(self, json_object):
        super().__init__(json_object)
        self.location = JsonToPy(json_object['location'])
        if self.__dict__.get('price') is None:
            self.price = 0
        elif self.price < 0:
            raise ValueError('must be >= 0')


if __name__ == '__main__':
    Advert1 = Advert(lesson_str)
    print(Advert1.location.address)
    print(Advert1.price)
    print(Advert1)
