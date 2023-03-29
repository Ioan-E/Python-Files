## Exam app

### Description

This app takes questions as a dict and builds an exam. Uses descriptors to update the Questions class. Provides extensive __repr__ and a Mixin to find all correct answers.

The application.by holds the logic, the playground.py several examplesm, requirement.txt are for a long description of the expectations and test uses unittests to check the implementation. Also logging is used to log application.py use.

The app uses mixins and decorators to add functionality to the Exam Class. A context manager was expected but only a dummy one was implemented. A better one will be created in the future.

### How to run and use the project

1. Fork the repository.
2. Clone the forked repository
3. Open playground.py and add questions for an Exam object. Use print() to see the exam. Use IWantAnswers() to check the correct answers.
