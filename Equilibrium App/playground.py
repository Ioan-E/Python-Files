from application import (
    PersonalDevelopment,
    Physical,
    Spiritual,
    Emotional,
    Social,
    Intellectual,
    DomainsCollection,
    check_status,
    i_am_a_decorator,
    i_am_a_generator,
)
import datetime
from time import sleep
from inspect import getgeneratorstate

user_dict_of_friends = {
    "Dan": ("0722222222", datetime.datetime(1988, 12, 5).strftime("%x")),
    "Larisa": ("0745111111", datetime.datetime(1991, 7, 5).strftime("%x")),
    "Mihaela": ("0744333333", datetime.datetime(1968, 5, 11).strftime("%x")),
    "Dan Adrian": ("0721555555", datetime.datetime(1966, 11, 9).strftime("%x")),
}

# Creating objects from Physical, Spiritual, Emotional, Social and Intelectual classes, desired and actual states
# Showcasing the inheritance of multiple methods from PersonalDevelopment class

user_DP = Physical(
    "Desired Physical", {"sleep": 56, "nutrition": 10500, "physical_exercise": 7}, 23.0
)
user_DSp = Spiritual(
    "Desired Spiritual", {"charity": 1, "meditation": 7, "contemplation": 1}, "buddhist"
)
user_DE = Emotional(
    "Desired Emotional",
    {
        "identifying_emotions_in_self": 1,
        "identifying_emotions_in_others": 3,
        "managing_self_emotions": 3,
        "managing_relationships": 7,
    },
    120,
)
user_DSo = Social(
    "Desired Social",
    {"monthly_message": 4, "monthly_meeting": 1, "randomly_calls": 2},
    user_dict_of_friends,
)
user_DI = Intellectual(
    "Desired Intellectual",
    {
        "daily_reading": 50,
        "memory_exercises": 10,
        "foreign_language": 105,
        "online_classes": 1,
    },
    "computer science",
)

user_AP = Physical(
    "Actual Physical", {"sleep": 50, "nutrition": 10000, "physical_exercise": 6}, 24.0
)
user_ASp = Spiritual(
    "Actual Spiritual", {"charity": 1, "meditation": 7, "contemplation": 1}, "buddhist"
)
user_AE = Emotional(
    "Actual Emotional",
    {
        "identifying_emotions_in_others": 3,
        "managing_self_emotions": 3,
        "managing_relationships": 7,
    },
    120,
)
user_ASo = Social(
    "Actual Social",
    {"monthly_message": 6, "monthly_meeting": 3, "randomly_calls": 2},
    user_dict_of_friends,
)
user_AI = Intellectual(
    "Actual Intellectual",
    {
        "daily_reading": 15,
        "memory_exercises": 10,
        "foreign_language": 105,
        "online_classes": 1,
        "group study": 1,
    },
    "computer science",
)

# # Showcasing the MixinPrint and the overwriting of the __str__ method

print(f"{user_DP} \n{user_DSp} \n{user_DE} \n{user_DSo} \n{user_DI}")

# # Showcasing the __repr__ method

# print(user_DI.__repr__(), '\n')

# Creating objects from DomainsCollection class

user_DCollection = DomainsCollection(
    "user's Desired Collection", (user_DP, user_DSp, user_DE, user_DSo, user_DI)
)
user_ACollection = DomainsCollection(
    "user's Actual Collection", (user_AP, user_ASp, user_AE, user_ASo, user_AI)
)

# Showcasing the __str__ method

# print(user_DCollection)

# Showcasing the operators overloading

# print(f'Desired state on physical is greater than actual state: {user_DP > user_AP}')
# print(f'Desired state on spiritual is equal with actual state: {user_DSp == user_ASp}')
# print(f'Desired state on emotional is greater than actual state: {user_DE > user_AE}')
# print(f'Desired state on social is lesser than actual state: {user_DSo < user_ASo}')
# print(f'Desired state on social is lesser than actual state: {user_DSo < user_ASo}')
# print(f'Desired state on intellectual is lesser than actual state: {user_DI < user_AI}')

# Showcasing the decorated function check_status

# check_status(user_DCollection, user_ACollection)

# Showcasing the usage of context manager to open and close files - for output, see the .txt file created in folder

# user_DP.save_state()

# Schowcasing the usage of generator

gen = i_am_a_generator(user_dict_of_friends)

# The code block below should be included in a coroutine in order not to block the execution of the app main functionalities
# while True:
# try:
#     print(getgeneratorstate(gen))
#     print(f'Please recommend \u001b[35mEquilibrium\u001b[0m app to your friend, {next(gen)}')
#     sleep(2)
# except StopIteration:
#     print('Thank you for recommending us to all your friends!\u2665')
#     print(getgeneratorstate(gen))
#     break
