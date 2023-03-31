import unittest
from application import (
    Intellectual,
    Emotional,
    DomainsCollection,
    Physical,
    Social,
    Spiritual,
    check_status,
    i_am_a_generator,
)


class TestIntellectual(unittest.TestCase):
    def test_Intellectual_object_attribute_initialization(self):
        name = "test"
        dict_of_activities = {"reading": 2}
        field_of_interest = "astrology"

        test_intellectual = Intellectual(name, dict_of_activities, field_of_interest)

        assert hasattr(
            test_intellectual, "name"
        ), "Intellectual object missing name attribute"
        assert hasattr(
            test_intellectual, "dict_of_activities"
        ), "Intellectual object missing dict_of_activities attribute"
        assert hasattr(
            test_intellectual, "field_of_interest"
        ), "Intellectual object missing field_of_interest attribute"


class TestDomainsCollection(unittest.TestCase):
    def test_DomainsCollection_object_attribute_initialization(self):
        name = "test"
        domains_collection = (
            "Social",
            "Emotional",
            "Intellectual",
            "Physical",
            "Spiritual",
        )

        test_DomainsCollection = DomainsCollection(name, domains_collection)

        assert hasattr(
            test_DomainsCollection, "name"
        ), "DomainsCollection object missing name attribute"
        assert hasattr(
            test_DomainsCollection, "domains_collection"
        ), "DomainsCollection object missing domains_collection attribute"


class TestEmotional(unittest.TestCase):
    def test_lt_operator_overloading(self):
        name_desired = "test_desired"
        name_actual = "test_actual"
        dict_of_activities_desired = {
            "recognizing emotions in self": 1,
            "managing self-emotions": 1,
        }
        dict_of_activities_actual = {
            "recognizing emotions in self": 3,
            "managing self-emotions": 1,
            "managing relationships": 4,
        }
        EQ_desired = 120
        EQ_actual = 120

        test_desired = Emotional(name_desired, dict_of_activities_desired, EQ_desired)
        test_actual = Emotional(name_actual, dict_of_activities_actual, EQ_actual)

        assert test_desired < test_actual, "Overloading operator lt gone bad"


class Test_Check_Status(unittest.TestCase):
    def test_check_status_returns_list(self):
        Ioan_DP = Physical(
            "Desired Physical",
            {"sleep": 56, "nutrition": 10500, "physical_exercise": 7},
            23.0,
        )
        Ioan_DSp = Spiritual(
            "Desired Spiritual",
            {"charity": 1, "meditation": 7, "contemplation": 1},
            "buddhist",
        )
        Ioan_DE = Emotional(
            "Desired Emotional",
            {
                "identifying_emotions_in_self": 1,
                "identifying_emotions_in_others": 3,
                "managing_self_emotions": 3,
                "managing_relationships": 7,
            },
            120,
        )
        Ioan_DSo = Social(
            "Desired Social",
            {"monthly_message": 4, "monthly_meeting": 1, "randomly_calls": 2},
            {},
        )
        Ioan_DI = Intellectual(
            "Desired Intellectual",
            {
                "daily_reading": 50,
                "memory_exercises": 10,
                "foreign_language": 105,
                "online_classes": 1,
            },
            "computer science",
        )

        Ioan_AP = Physical(
            "Actual Physical",
            {"sleep": 50, "nutrition": 10500, "physical_exercise": 7},
            23.0,
        )
        Ioan_ASp = Spiritual(
            "Actual Spiritual",
            {"charity": 1, "meditation": 7, "contemplation": 1},
            "buddhist",
        )
        Ioan_AE = Emotional(
            "Actual Emotional",
            {
                "identifying_emotions_in_others": 3,
                "managing_self_emotions": 3,
                "managing_relationships": 7,
            },
            120,
        )
        Ioan_ASo = Social(
            "Actual Social",
            {"monthly_message": 6, "monthly_meeting": 3, "randomly_calls": 2},
            {},
        )
        Ioan_AI = Intellectual(
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

        Ioan_DCollection = DomainsCollection(
            "Ioanxandra's Desired Collection",
            (Ioan_DP, Ioan_DSp, Ioan_DE, Ioan_DSo, Ioan_DI),
        )
        Ioan_ACollection = DomainsCollection(
            "Ioanxandra's Actual Collection",
            (Ioan_AP, Ioan_ASp, Ioan_AE, Ioan_ASo, Ioan_AI),
        )

        assert type(
            check_status(Ioan_DCollection, Ioan_ACollection) == list
        ), "Check-status does not return a list"


class test_generator(unittest.TestCase):
    def test_generators_yields_correct_values(self):
        gen = i_am_a_generator({"friend1": 1, "friend2": 2, "friend3": 3})

        assert next(gen) == "friend1", "Generator does not yield correct value"
        assert next(gen) == "friend2", "Generator does not yield correct value"
        assert next(gen) == "friend3", "Generator does not yield correct value"


if __name__ == "__main__":
    unittest.main()
