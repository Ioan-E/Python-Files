from collections import Counter

class Room:
    def __init__(self, name, size):
        self.name = name
        self.size = size
    
    def __str__(self):
        return f'{self.name}, {self.size}m'


class House:
    '''Builds a House from Room class'''

    def __init__(self, available_space=100):
        self.rooms = []
        self.available_space = available_space

    def add_rooms(self, *args):
        for room in args:
            if self.size() + room.size > self.available_space:
                raise NotEnoughSpaceError(
                    f'{room.name} needs {room.size}; \
                    only {self.available_space - self.size()} available')
            else:
                self.rooms.append(room)
    
    def __add__(self, room):
        if self.size() + room.size > self.available_space:
                raise NotEnoughSpaceError(
                    f'{room.name} needs {room.size}; \
                    only {self.available_space - self.size()} available')
        else:
            output = House(self.available_space)
            output.rooms = self.rooms
            output.rooms.append(room)
            return output
        
        #     self.rooms.append(room)
        # return self                                       #this is the implementation for __iadd__

    def size(self):
        return sum(room.size for room in self.rooms)        #this is a generator

    def __str__(self):
        string = str(self.__class__.__name__) + ':'         #what's inside str provides the correct name based on class name
        for room in self.rooms:
            string += f'\n{str(room)}'
        return string
    
    def calculate_tax(self):
        tax = self.size() * 100
        return tax


class SingleFamilyHouse(House):
    '''Inherits from House. Calculates taxes.'''

    def __init__(self, available_space = 200):
        super().__init__(available_space)

    def calculate_tax(self):
        if self.size() < 150:
            tax = self.size() * 100 * 1.2
        else:
            tax = 150 * 100 * 1.2 + (self.size() - 150) * 100 * 1.5
        return tax


class TownHouse(House):
    '''Inherits from House. Calculates taxes.'''

    def __init__(self, available_space = 100):
        super().__init__(available_space)


class Apartment(House):
    '''Inherits from House. Calculates taxes.'''

    def __init__(self, available_space = 80):
        super().__init__(available_space)

    def calculate_tax(self):
        tax = self.size() * 100 * 0.75
        # return super().calculate_tax() * 0.75             #this way we use calculation from House
        return tax


class Neighborhood:
    '''Builds a Neighbourhood from House'''

    total_size = 0

    def __init__(self):                                     
        # self.name = name
        self.houses = []
    
    def add_houses(self, *args):
        for house in args:
            self.houses.append(house)
            Neighborhood.total_size += house.size()
    
    def __add__(self, house):
        output = Neighborhood()
        output.houses = self.houses
        output.houses.append(house)
        Neighborhood.total_size += house.size()
        return output

    def size(self):
        return sum(house.size() for house in self.houses)

    def house_types(self):                                  #Counter generates a dictionary that counts the elements of an interable
        '''Provides a dictionary with all the houses inside Neighbourhood'''

        return Counter(type(one_house).__name__
                       for one_house in self.houses)
    
    def calculate_tax(self):
        return sum([one_house.calculate_tax()
                   for one_house in self.houses])

    def find_with_room(self, **kwargs):
        '''Looks for a house with one or several required rooms'''

        return {one_house
                for one_house in self.houses
                for one_room in one_house.rooms
                if vars(one_room) == kwargs}                #compares two dictionaries

class NotEnoughSpaceError(Exception):
        pass



# r1 = Room('master bedroom', 25)
# r2 = Room('bathroom', 5)
# r3 = Room('living room', 30)
# r4 = Room('kitchen', 20)

# h1 = House()
# h1.add_rooms(r1, r2, r3, r4)
# h1 = h1 + r1
# h1 += r2
# print(h1)
# print(h1.size())

# h2 = House(30)
# h2.add_rooms(r1,r2)
# print(h2.size())

# n1 = Neighborhood()
# n1 = n1 + h1 + h2
# n1.add_houses(h1, h2)
# print(n1.size())
# print(Neighborhood.total_size)
# print(n1.house_types())

# n2 = Neighborhood()
# n2.add_houses(h1, h1, h2, h2)
# print(n2.size())

# print(Neighborhood.total_size)

# h1 = Apartment()
# print(h1.available_space)
# print(h1)

# h = Apartment()
# bedroom = Room('bedroom', 10)
# kitchen = Room('kitchen', 9)
# bathroom = Room('bathroom', 3)
# h.add_rooms(bedroom, kitchen, bathroom)
    
# h.calculate_tax() == 1650
# print(h.calculate_tax())

# for house in n2.find_with_room(name = 'living room', size = 30):
#     print(house)