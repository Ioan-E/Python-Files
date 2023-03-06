## Requirements for Final Project (Python Development Class)

#### Equilibrium App

We will build an app that will help us register all our desired and actual activities across 5 life domains: physical, intellectual, emotional, social and spiritual. These can be translated into 5 classes that will help us describe each life domain. We will start with a **mutable mapping class** called PersonalDevelopment, from which Physical, Intellectual, Emotional, Social and Spiritual classes will **inherit**. 

​		`class PersonalDevelopment ():`

A life domain class can be created starting from a name, a dictionary of activities and frequencies, and an attribute related to the life domain (eg. for Physical domain, it can be the body mass index(BMI), Spiritual - spiritual_views, Social - emotional quotient (EQ), Intellectual - field_of_interest, Social - dictionary of friends):

​		`new_physical_object = Physical ('Mihai\'s physical activities, {'sleeping':56, 'exercising':4}, 23}`

We will also have a DomainsCollection class, which is a **sequence** type class. It will hold all our objects created above and once created, it cannot be updated:

​		`class DomainsCollection():`

Each class should have `__str__` and `__repr__` methods

We will build a **mixin class**, called MixinPrint, which will be used by Physical, Intellectual, Social, Emotional and Spiritual classes in order to nicely print their content. 

Create a function called check_status that will let you compare two DomainsCollection objects so that we know how we did on each field. The function will return a list with a two-members tuple for each field. The first member of the tuple is the domain's name of the desired state and the second member is a string representing the relationship between the desired and the actual state ('equal', 'lesser', 'greater'). In order to make the comparison between objects, **overload the operators** ==, !=, >, < in the PersonalDevelopment class.  

​		`check_status(desired_domains_collection, actual_domains_collection)`

We will use a **decorator** in order to nicely print the returned result of the function check_status.

For each of the five children of PersonalDevelopement class, we should be able to write a report in a file. Build a context manager that will allow you to open and close files and use it in a method called save_state:

​		`save_state(...):`

​			`with context_manager_name....`

We will build a **generator factory ** to help us get one friend at a time from our dictionary of friends, to whom we should suggest using our Equilibrium app. Normally, the app should pick a friend monthly, but for the sake of the example, we'll transform the unit so that a month=2s. After you recommend the app to all your friends, you should display a thank you message. 

For each component that we build, we have to add use cases and some tests to showcase the functionality and test that it meets all the requirements.

In a new file, separated from the **showcasing code**, you will add **tests** for the implementation.

Last, but not least, we will use **standard logging**, configured with the DEBUG level, in order to mark the essential pin points of our application. 

