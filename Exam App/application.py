import datetime
import time
import random
import logging

logging.basicConfig(level=logging.DEBUG, filename=f'{datetime.datetime.now()}_log.log')
logger = logging.getLogger(' final_project_log')

logger.debug(' Start')

class Questions:
    '''Creates the questions needed for an exam. To instantiate a dictinary with a questionn key, answers, correct answer and user name is expected
        A more detailed description is available on __repr__'''

    def __init__(self, q_and_a):
        self.q_and_a = q_and_a
        logger.info(f' The questions class has been called with the following data: {self.q_and_a}, id: {id(self.q_and_a)}, type: {type(self.q_and_a)}')

    def __str__(self):
        questions_print = ''
        for key in self.q_and_a:
            questions_print = '\n'.join((questions_print, key))
        logger.info(f' The following questions were printed: {questions_print}')
        return questions_print
    
    def __repr__(self):
        questions_extra_info = ''
        nl = '\n'
        extra_i0 = 'This object is a: '
        extra_i1 = 'It contains questions as: '
        extra_i2 = 'And as '
        extra_i3 = ' there is a '
        extra_i4 = ' that contains: \n' \
                    'at [0] a list with the answers: \n' \
                    'at [1] the index for the correct answer (starting at 1) \n' \
                    'at [2] the name of the one who created the question'
        for key in self.q_and_a:
            all_info = self.q_and_a[key][2]
            questions_extra_info = '\n'.join((questions_extra_info, key, 'The above question was created by:', str(all_info)))

        questions_extra_info = (
                        f'{questions_extra_info}{nl}{extra_i0}{type(self)}{nl}'
                        f'{extra_i1}{type(self.q_and_a.keys())}{nl}{extra_i2}{type(self.q_and_a.values())}{extra_i3}{type(self.q_and_a[key])}{extra_i4}'
        )
        return questions_extra_info

    def __iter__(self):
        return iter(self.q_and_a)

    def __contains__(self, item):
        return item in self.q_and_a

    def __len__(self):
        return len(self.q_and_a)

    def __getitem__(self, question):
        return self.q_and_a[question]
    
    def __setitem__(self, question, options):
        self.q_and_a[question] = options
        logger.debug (f' The following question has been added: {question}, id: {id(question)}, type: {type(question)}')
        logger.debug (f' For this question - {question} - the answers are: {options}, id: {id(options)}, type: {type(options)}')

    def __delitem__(self, question):
        del self.q_and_a[question]
        logger.debug (f' The following question has been removed: {question}, id: {id(question)}, type: {type(question)}')

    def keys(self):
        return self.q_and_a.keys()

    def values(self):
        return self.q_and_a.values()

    def items(self):
        return self.q_and_a.items()

    def get_answers(self, question):
        return self.q_and_a[question][0]
    
    def get_correct_answer (self, question):
        correct_answer_position = self.q_and_a[question][1] - 1
        logger.info (f' The correct answer for this question - {question} - was requested.')
        return self.q_and_a[question][0][correct_answer_position]

    def get_sample_questions (self):
        questions_list = list(self.keys())
        random.shuffle(questions_list)
        for question in questions_list:
            yield question
    
    def __add__(self, question):
        only_question = question[0]
        options = [[question[1], question[2], question[3]], question[4], question[5]]
        self.q_and_a[only_question] = options
        logger.debug (f' The following question has been added through +: {question}; type: {type(question)}')
        return self.q_and_a


class Exam(Questions):
    '''Creates an examen based on Questions class. __repr__ provides all the information needed'''
    def __init__(self, q_and_a):
        super().__init__(q_and_a)
        logger.info(f'The exam class has been called with the following data: {self.q_and_a}, id: {id(self.q_and_a)}, type: {type(self.q_and_a)}')
    
    def __str__(self):
        pagina_examen = 'Business Management Exam'
        nl = '\n'
        intro = 'For the following question choose one correct answer:'
        for key in self.q_and_a:
            pagina_examen = f'{pagina_examen}{nl}{nl}{intro}{nl}{key}'
            for answer in self.q_and_a[key][0]:
                pagina_examen = f'{pagina_examen}{nl}{answer}'
        logger.info(f' The following exam was printed: {pagina_examen}')
        return pagina_examen

    def __repr__(self):
        exam_extra_info = 'Business Management exam with the following questions:'
        nl = '\n'
        ans = 'Answers: '
        corr = 'The correct answer is: '
        author = 'Author: '
        extra_i0 = 'This object is a: '
        cre_on = ' created on '
        created_on = datetime.date.today()
        extra_i1 = 'It contains questions as: '
        extra_i2 = 'And as '
        extra_i3 = ' there is a '
        extra_i4 = ' that contains: \n' \
                    'at [0] a list with the answers: \n' \
                    'at [1] the index for the correct answer (starting at 1) \n' \
                    'at [2] the name of the one who created the question'
        for key in self.q_and_a:
            answers = self.q_and_a[key][0]
            correct_answer_position = self.q_and_a[key][1] - 1
            correct_answer = self.q_and_a[key][0][correct_answer_position]
            author_info = self.q_and_a[key][2]
            exam_extra_info = (
                        f'{exam_extra_info}{nl}{key}{nl}{ans}{answers}{nl}'
                        f'{corr}{correct_answer}{nl}{author}{author_info}'
            )
        exam_extra_info = (
                    f'{exam_extra_info}{nl}{extra_i0}{type(self)}{cre_on}{created_on}{nl}'
                    f'{extra_i1}{type(self.q_and_a.keys())}{nl}{extra_i2}{type(self.q_and_a.values())}{extra_i3}{type(self.q_and_a[key])}{extra_i4}'
        )
        return exam_extra_info


class AnswersMixin:
    '''Provides all the right answers'''

    def __init__(self, exam):
        super().__init__(exam)

    def correct_exam_answers (self):
        for key in self.q_and_a:
            correct_answer_position = self.q_and_a[key][1] - 1
            print (self.q_and_a[key][0][correct_answer_position])
        logger.info (f' All the answers were requested')


class IWantAnswers (AnswersMixin, Exam):
    pass
    

def pretty_print_exam(function):

    def wrapper(exam):
        print('''
 ________________________________________________
(************************************************)
(________________________________________________)
        ''')
        print ('Business Management Exam''\n''Name and Surname:''\n''For the following questions choose one correct answer.')
        nl = '\n'
        function(exam)
        print (f'{nl}Exam printed on: {datetime.date.today()}')
        print ('''
 ________________________________________________
(________________________________________________)
        ''')
    logger.debug (f' The following function - {function} - was decorated by pretty_print_exam decorator.')
    return wrapper


@pretty_print_exam
def prepare_exam(exam):             #randomize question and answers(helps in reducing cheating)
    exam_as_question_list = list(exam.keys())
    random.shuffle(exam_as_question_list)
    for question in exam_as_question_list:
        print ('\n',question)
        answers = exam[question][0]
        random.shuffle(answers)
        for answer in answers:
            print (answer)


class TimeMyApp:
    '''Dummy context manager'''
    
    def __enter__(self):
        print('The timer has started')
        self.start = time.time()
        
    def __exit__(self, type, value, traceback):
        self.stop = time.time()
        result = self.stop - self.start
        print(f'It took {result} seconds to stop.')
       
        if type:
            print(f'{type} error occured. Please duble check your code and learn to do better context managers.')
            return True
    
# test_questions = Questions({
#                     'What is business management?': [['a book', 'a field of study', 'a movie'], 2, 'Ionut'],
#                     'What is SWOT?': [['an analytical tool', 'a military force', 'a solution to business problems'], 1, 'Ada'],
#                     'How many forces are in The Porter Model?': [['1', '3', '5'], 3, 'Ionut']
# })
# test_exam = Exam(test_questions)
# print(test_exam)
# correct_answers = IWantAnswers(test_exam)
# correct_answers.correct_exam_answers()
# prepare_exam(test_exam)
# with TimeMyApp() as t:
#     prepare_exam(test_exam)
