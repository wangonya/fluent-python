from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 100, (0,1))

if __name__ == '__main__':
    print(f"city = {City}")
    print(f"tokyo = {tokyo}")
    print(f"tokyo.population = {tokyo.population}")
    print(f"tokyo.coordinates = {tokyo.coordinates}")

    print(f"tokyo._asdict() = {tokyo._asdict()}")
