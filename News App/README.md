## News App

### Description

The app connects to five news sites and delivers the news in a basic UI. Provides an interface using Qt module. Can search for news based on keywords.

application.py provides the logic, including mixins, context manager, generators and the GUI and search code. playground.py provides some examples. Also logging is available.

This was my first app for which I had to look for and decide what are the best tools to deliver the results. It is a particularly hard task as Python is providing a lot of options. To solve this I've used a method from market research. First I've looked for as many options as possible - qualitative research. Then I briefly researched the documentation and tutorials - piloting. For the most relevant tools I've checked how others implemented them and tried to see if I can use a similar approach - quantitative research. Finally, I was able to make a decision and, even better, I was already familiar with how to use the desired tool.

Another challenge was learning to use Qt. The documentation proved to be very useful. I was able to understand the main functionalities I need and to apply them one at a time. This way I've developed the UI step by step.

Finally, the project is able to connect to five news sites and deliver the main headlines in a user-friendly environment. 

### How to run and use the project

1. Fork the repository.
2. Clone the forked repository.
3. Go to playground.py, uncomment the last line.
4. Use the GUI to read the news.

At this point (31.03.2023) only two website connections are still working.
