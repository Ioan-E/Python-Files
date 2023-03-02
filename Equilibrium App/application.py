import logging
import datetime

logging.basicConfig(level=logging.DEBUG, filename=f'{datetime.datetime.now().strftime("%Y-%m-%d")}_Equilibrium_log.log', filemode='w')
logger = logging.getLogger(__name__)

class PersonalDevelopment:
    '''Parent class. Mutable mapping type. It has 5 children classes: Physical, Spiritual, Emotional, Social, Intellectual.'''
    def __init__(self, name = None, dict_of_activities = None):
        self.name = name
        self.dict_of_activities = dict_of_activities
        
    def __getitem__(self, activity):
        return self.dict_of_activities[activity]
        
    def __setitem__(self, activity, goal):
        self.dict_of_activities[activity] = goal
    
    def __iter__(self):
        return iter(self.dict_of_activities)
    
    def __delitem__(self, activity):
        del self.dict_of_activities[activity]
        
    def __len__(self):
        return len(self.dict_of_activities)
    


    def __eq__(self, other):
        '''Operator == overloading. The method compares two instances of the PersonalDevelopment class
            :param other:
            :return: boolean flag weather self and other are the same or not
            Two PersonalDevelopment objects are equal if they have identical list of activities and identical frequencies for each activity'''
        for activity, frequency in self.dict_of_activities.items():
            if activity not in other.dict_of_activities:
                return False
            else:
                if frequency != other.dict_of_activities[activity]:
                    return False
        return True


    def __ne__(self, other):
        '''Operator != overloading. The method compares two instances of the PersonalDevelopment class
            :param other:
            :return: the negation of the __eq__ method returned boolean
            Two PersonalDevelopment objects are not equal if they do not have identical list of activities and they do not have
            identical frequencies for each activity'''        
        return not self.__eq__(other)
    
    def __lt__(self, other):
        self_set = set(self.dict_of_activities.keys())
        other_set = set(other.dict_of_activities.keys())
        if not self_set.issubset(other_set):
            return False
        else:
            intersection_set = self_set & other_set
            for element in intersection_set:
                if self.dict_of_activities[element] > other.dict_of_activities[element]:
                    return False
        return True
                       
    def __gt__(self, other):
        return not self.__eq__(other) and not self.__lt__(other)
    
    def save_state(self):
        '''Method to write in a file the activities implemented in a field'''
        file_name = f'{datetime.datetime.now().strftime("%Y-%m-%d")}_{self.name}.txt'
        with i_am_a_context_manager(file_name) as file:
            logger.info(f'Writing list of activities in {file_name}')
            file.write('Placeholder for list of activities')



class MixinPrint:
    '''Mixin class. Its only purpose is to make a nice print for Physical, Spiritual, Emotional, Social and Intellectual classes, using the
        overwriting of __str__ method in child class'''
    def __init__(self):
        pass
    
    def __str__(self, name='No_name', dict_of_activities={'no_activity': 0}, **kwargs):
        logger.debug(f'Performing MixinPrint for {name}')
        star_line = '*' * (len(name) + 4) + '\n'
        string = f'{star_line} \n{name} \n\n{star_line} \n'
        for index, (keys, values) in enumerate(dict_of_activities.items(), start=1):
            string += f'{index}. {keys}: {values} \n'
        for indexx, (k,v) in enumerate(kwargs.items(), index+1):
            string += f'{indexx}. {k}: {v}\n'
        string += f'\n{star_line}\n'
        return (string)


class Physical(PersonalDevelopment, MixinPrint):
    '''Inherits from PersonalDevlopment class and MixinPrint class'''
    def __init__(self, name, dict_of_activities, BMI):
        logger.debug(f'Creating Physical object named {name}')
        super().__init__(name, dict_of_activities)
        self.BMI = BMI
               
    def __getitem__(self, activity):
        return super().__getitem(self, activity)
        
    def __setitem__(self, activity, goal):
        super().setitem__(self, activity, goal)
    
    def __iter__(self):
        return super().__iter__(self)
    
    def __delitem__(self, activity):
        super().__delitem__(self, activity)
        
    def __len__(self):
        return super().__len__(self)
    
    def __eq__(self, other):
        return super().__eq__(other)
    
    def __ne__(self, other):
        return not self.__eq__(other)
           
    def __gt__(self, other):
        return not self.__eq__(other) and not self.__lt__(other)
    
    def __lt__(self,other):
        return super().__lt__(other) 
    
    def save_state(self):
        super().save_state()
           
    def items(self):
        return self.dict_of_activities.items()
    
    def keys(self):
        return self.dict_of_activities.keys()
    
    def values(self):
        return self.dict_of_activities.values()
    
    def __str__(self):
        return super().__str__(self.name, self.dict_of_activities, BMI=self.BMI)
    
    def __repr__(self):
        return (f'The representation of the object Physical is: ({self.name}, {self.dict_of_activities}, {self.BMI}')
        
    
class Spiritual(PersonalDevelopment, MixinPrint):
    '''Inherits from PersonalDevlopment class and MixinPrint class'''    
    def __init__(self, name, dict_of_activities, spiritual_views):
            logger.debug(f'Creating Spiritual object named {name}')
            super().__init__(name, dict_of_activities)
            self.spiritual_views = spiritual_views
        
    def __getitem__(self, activity):
        return super().__getitem(self, activity)
        
    def __setitem__(self, activity, goal):
        super().setitem__(self, activity, goal)
    
    def __iter__(self):
        return super().__iter__(self)
    
    def __delitem__(self, activity):
        super().__delitem__(self, activity)
        
    def __len__(self):
        return super().__len__(self)
    
    def __eq__(self, other):
        return super().__eq__(other)
    
    def __ne__(self, other):
        return not self.__eq__(other)
           
    def __gt__(self, other):
        return not self.__eq__(other) and not self.__lt__(other)
    
    def __lt__(self,other):
        return super().__lt__(other) 
    
    def save_state(self):
        super().save_state()
    
    def items(self):
        return self.dict_of_activities.items()
    
    def keys(self):
        return self.dict_of_activities.keys()
    
    def values(self):
        return self.dict_of_activities.values()
    
    def __str__(self):
        return super().__str__(self.name, self.dict_of_activities, spiritual_views=self.spiritual_views)
    
    def __repr__(self):
        return (f'The representation of the object Spiritual is: ({self.name}, {self.dict_of_activities}, {self.spiritual_views}')


class Emotional(PersonalDevelopment, MixinPrint):
    '''Inherits from PersonalDevlopment class and MixinPrint class'''    
    def __init__(self, name, dict_of_activities, EQ):
            logger.debug(f'Creating Emotional object named {name}')
            super().__init__(name, dict_of_activities)
            self.EQ = EQ
    
    def __getitem__(self, activity):
        return super().__getitem__(self, activity)
        
    def __setitem__(self, activity, goal):
        super().setitem__(self, activity, goal)
    
    def __iter__(self):
        return super().__iter__(self)
    
    def __delitem__(self, activity):
        super().__delitem__(self, activity)
        
    def __len__(self):
        return super().__len__(self)
        
    def __eq__(self, other):
        return super().__eq__(other)
    
    def __ne__(self, other):
        return not self.__eq__(other)
           
    def __gt__(self, other):
        return not self.__eq__(other) and not self.__lt__(other)
    
    def __lt__(self,other):
        return super().__lt__(other) 
    
    def save_state(self):
        super().save_state()
    
    def items(self):
        return self.dict_of_activities.items()
    
    def keys(self):
        return self.dict_of_activities.keys()
    
    def values(self):
        return self.dict_of_activities.values()
    
    def __str__(self):
        return super().__str__(self.name, self.dict_of_activities, EQ=self.EQ)
    
    def __repr__(self):
        return (f'The representation of the object Emotional is: ({self.name}, {self.dict_of_activities}, {self.EQ}')
    

class Social(PersonalDevelopment, MixinPrint):
    '''Inherits from PersonalDevlopment class and MixinPrint class'''
    def __init__(self, name, dict_of_activities, dict_of_friends):
            logger.debug(f'Creating Social object named {name}')
            super().__init__(name, dict_of_activities)
            self.dict_of_friends = dict_of_friends
    
    def __getitem__(self, activity):
        return super().__getitem__(self, activity)
        
    def __setitem__(self, activity, goal):
        super().setitem__(self, activity, goal)
    
    def __iter__(self):
        return super().__iter__(self)
    
    def __delitem__(self, activity):
        super().__delitem__(self, activity)
        
    def __len__(self):
        return super().__len__(self)
    
    def __eq__(self, other):
        return super().__eq__(other)
        
    def __ne__(self, other):
        return not self.__eq__(other)
           
    def __gt__(self, other):
        return not self.__eq__(other) and not self.__lt__(other)
    
    def __lt__(self,other):
        return super().__lt__(other) 
    
    def save_state(self):
        super().save_state()
    
    def items(self):
        return self.dict_of_activities.items()
    
    def keys(self):
        return self.dict_of_activities.keys()
    
    def values(self):
        return self.dict_of_activities.values()
    
    def __str__(self):
        return super().__str__(self.name, self.dict_of_activities, dict_of_friends=self.dict_of_friends)
    
    def __repr__(self):
        return (f'The representation of the object Social is: ({self.name}, {self.dict_of_activities}, {self.dict_of_friends}')
    

class Intellectual(PersonalDevelopment, MixinPrint):
    '''Inherits from PersonalDevlopment class and MixinPrint class'''        
    def __init__(self, name, dict_of_activities, field_of_interest):
        logger.debug(f'Creating Intellectual object named {name}')
        super().__init__(name, dict_of_activities)
        self.field_of_interest = field_of_interest
        
    def __getitem__(self, activity):
        return super().__getitem__(self, activity)
        
    def __setitem__(self, activity, goal):
        super().setitem__(self, activity, goal)
    
    def __iter__(self):
        return super().__iter__(self)
    
    def __delitem__(self, activity):
        super().__delitem__(self, activity)
        
    def __len__(self):
        return super().__len__(self)
       
    def __eq__(self, other):
        return super().__eq__(other)
    
    def __ne__(self, other):
        return not self.__eq__(other)
           
    def __gt__(self, other):
        return not self.__eq__(other) and not self.__lt__(other)
    
    def __lt__(self,other):
        return super().__lt__(other) 
    
    def save_state(self):
        super().save_state()
    
    def items(self):
        return self.dict_of_activities.items()
    
    def keys(self):
        return self.dict_of_activities.keys()
    
    def values(self):
        return self.dict_of_activities.values()
    
    def __str__(self):
        return super().__str__(self.name, self.dict_of_activities, field_of_interest=self.field_of_interest)
    
    def __repr__(self):
        return (f'The representation of the object Intellectual is: ({self.name}, {self.dict_of_activities}, {self.field_of_interest}')


class DomainsCollection():
    '''Sequence-like class(tuple). Holds PersonalDevelopment objects'''
    def __init__(self, name, domains_collection):
        logger.debug(f'Creating DomainsCollection object named {name}')
        self.name = name
        self.domains_collection = domains_collection
        
    def __getitem__(self, index):
        return self.domains_collection[index]

    def __len__(self):
        return len(self.domains_collection)
    
    def __str__(self):
        domains_names_list = []
        for domain in self.domains_collection:
            domains_names_list.append(domain.name)
        return (f'{self.name} contains the following domains: {domains_names_list}')
    
    def __repr__(self):
        return (f'The representation of the object {self} is {self.name} = {self.domains_collection}')


 
def i_am_a_decorator(function):
    '''This function will be used to decorate the check_status function'''
    logger.debug(f'Decorating {function.__name__}')
    def inner_function(*args):
        printing_list = function(*args)
        for domain, status in printing_list:
            if status == 'equal':
                print(f'\n \u001b[32m\u2b9e\u001b[0m Congrats! \n You reached your goal on {domain}! \n Keep up the good work!')
            elif status == 'greater':
                print(f'\n \u001b[36m\u2b9d\u001b[0m Wow! \n You exceeded the expectations on {domain}! \n Keep it all in equilibrium!')
            else:
                print(f'\n \u001b[31m\u2b9f\u001b[0m You did not reach your goal this week on {domain}! \n Level up next week!' + '\n')
        return function
        
    return inner_function


@i_am_a_decorator
def check_status(desired_state_collection, actual_state_collection):
    '''Function compares two DomainsCollection objects, member by member
        :param desired_state_collection, actual_state_collection
        :return: a list with five tuples: desired state - status of the actual state compared with the desired state'''
    logger.info("Looking for differences between desired state and actual state activities")
    logger.debug(f'Desired state collection is {desired_state_collection.name} and actual state is {actual_state_collection.name}')
    printing_list = []
    for index in range(5):
        if desired_state_collection[index] == actual_state_collection[index]:
            printing_list.append((desired_state_collection[index].name, 'equal'))
        elif desired_state_collection[index] > actual_state_collection[index]:
            printing_list.append((desired_state_collection[index].name, 'lesser'))
        else:
            printing_list.append((desired_state_collection[index].name, 'greater'))
    return printing_list


     
class i_am_a_context_manager():
    '''Implementation of a context manager that opens a file in __enter__ method (in order to write something in it) and
    closes it in __exit__ method. No errors expected. The context manager is used in the method save_state in every of the five children
    classes of PersonalDevelopment'''
    def __init__(self, file_name):
        self.file_name = file_name
    
    def __enter__(self):
        logger.debug(f'Opening {self.file_name} to write activities')
        self.file = open(self.file_name, 'w')
        return self.file
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        logger.debug(f'Closing {self.file_name}')
        self.file.close()
        
# Implementation of a generator factory that will yield a key from a dictionary - called in playground.py      
def i_am_a_generator(dict_of_friends):
    logger.debug("Generating one friend at a time from the friends dictionary")
    for friend in dict_of_friends.keys():
        yield friend
    
            