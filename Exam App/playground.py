from application import (
    Questions,
    Exam,
    AnswersMixin,
    IWantAnswers,
    prepare_exam,
    pretty_print_exam,
    TimeMyApp,
)

first_questions = Questions({
                'What is business management?': [['a book', 'a field of study', 'a movie'], 2, 'Ionut'],
                'What is SWOT?': [['an analytical tool', 'a military force', 'a solution to business problems'], 1, 'Ada']
})

# # Proof of: "questions will provide predefined questions to be asked during an exam (mutable mapping)."
# # Proof of: "the questions and only the questions should be printed (str).""
# # Proof of: "aditional info in order to understand the question should be printed as well (repr)."
print(first_questions)
print(repr(first_questions))
print(len(first_questions))
print(first_questions['What is SWOT?'])
print(first_questions.get_answers('What is business management?'))
print(first_questions.get_correct_answer('What is business management?'))
first_questions['How many forces are in The Porter Model?'] = [['1', '3', '5'], 3, 'Ionut']
first_questions['What is the first stage in the consolidation process?'] = [['scale', 'opening', 'focus'], 2, 'Ada']
print(first_questions)
print(first_questions.get_answers('How many forces are in The Porter Model?'))

# # Proof of "an alternative option for adding questions should be provided (operator overloading)."
# more_questions = Questions(first_questions + ('What is the first marketing P?', 'price', 'people', 'product', 3, 'Ionut'))
# print (more_questions)


# # Proof of "if a students asks for sample questions they should be provided (generator)."
# sample_questions = first_questions.get_sample_questions()
# sample_question1 = next(sample_questions)
# print (sample_question1)
# sample_question2 = next(sample_questions)
# print (sample_question2)


examen = Exam({
        'What is business management?': [['a book', 'a field of study', 'a movie'], 2, 'Ionut'],
        'What is SWOT?': [['an analytical tool', 'a military force', 'a solution to business problems'], 1, 'Ada'],
        'How many forces are in The Porter Model?': [['1', '3', '5'], 3, 'Ionut']
 })


# # Proof of "exams should generate a 3 questions short exam (quiz) with 
# # questions that inherit from the questions (sequence, inheritance)."
# # Proof of "a draft of the exam should be printed (str)."
# # Proof of "More info regarding the exam class should be provided, and also the date of the exam creation (repr)."
# print (examen['What is SWOT?'])
# print (examen)
# print (repr(examen))
# print(examen.get_answers('What is business management?'))
# print(examen.get_correct_answer('What is business management?'))


# Proof of "because the exam could be checked by someone different than the author there 
# will be a way to receive only the correct answers (mixin).
# cheeky = IWantAnswers(examen)
# cheeky.correct_exam_answers()

# Proof of "the appearance of the exams will be improved making sure the exam has title, name, and date (decorator)."
# prepare_exam(examen)


# # Proof of "When printing an exam the running time should be provided (context manager)."
# # Proof of "Also an error catcher should output the error and a message to further learn context managers :)"
with TimeMyApp():
    print (examen)
with TimeMyApp():
    print ('just_cheking')