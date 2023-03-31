from application import (
    Questions,
    Exam,
    AnswersMixin,
    IWantAnswers,
    prepare_exam,
    pretty_print_exam,
)
import unittest

class TestQuestions(unittest.TestCase):

    def test_questions_object_attribute_initialization(self):
        
        test_question = Questions({'What is business management?': [['a book', 'a field of study', 'a movie'], 2, 'Ionut']})

        assert hasattr(test_question, 'q_and_a'), 'Questions has no question. It is missing q_and_a'
        self.assertEqual(len(test_question['What is business management?']), 3), 'Not enough info provided for this question'
        self.assertEqual(len(test_question['What is business management?'][0]), 3), 'Not enough answers provided for this question'
        self.assertTrue(test_question['What is business management?'][1] > 0), 'The provided answer index is too small'
        self.assertTrue(test_question['What is business management?'][1] < 4), 'The provided answer index is too big'

    
    def test_setitem(self):

        test_questions = Questions({'What is business management?': [['a book', 'a field of study', 'a movie'], 2, 'Ionut']})
        
        test_questions['How many forces are in The Porter Model?'] = [['1', '3', '5'], 3, 'Ionut']

        assert isinstance(test_questions, Questions), 'Not a correct way to add a question'
        self.assertEqual(len(test_questions['How many forces are in The Porter Model?']), 3), 'Not enough info provided for this question'
        self.assertEqual(len(test_questions['How many forces are in The Porter Model?'][0]), 3), 'Not enough answers provided for this question'
        self.assertTrue(test_questions['How many forces are in The Porter Model?'][1] > 0), 'The provided answer index is too small'
        self.assertTrue(test_questions['How many forces are in The Porter Model?'][1] < 4), 'The provided answer index is too big'


    def test_setitem_alternative(self):

        test_questions = Questions({'What is business management?': [['a book', 'a field of study', 'a movie'], 2, 'Ionut']})
        
        more_test_questions = Questions(test_questions + ('What is the first marketing P?', 'price', 'people', 'product', 3, 'Ionut'))

        assert isinstance(more_test_questions, Questions), 'Not a correct way to add a question'
        self.assertEqual(len(more_test_questions['What is the first marketing P?']), 3), 'Not enough info provided for this question'
        self.assertEqual(len(more_test_questions['What is the first marketing P?'][0]), 3), 'Not enough answers provided for this question'
        self.assertTrue(more_test_questions['What is the first marketing P?'][1] > 0), 'The provided answer index is too small'
        self.assertTrue(more_test_questions['What is the first marketing P?'][1] < 4), 'The provided answer index is too big'


    def test_sample_questions(self):

        test_questions = Questions({
                            'What is business management?': [['a book', 'a field of study', 'a movie'], 2, 'Ionut'],
                            'What is SWOT?': [['an analytical tool', 'a military force', 'a solution to business problems'], 1, 'Ada'],
                            'How many forces are in The Porter Model?': [['1', '3', '5'], 3, 'Ionut']
        })

        test_sample_questions = test_questions.get_sample_questions()
        test_sample_question1 = next(test_sample_questions)
        test_sample_question2 = next(test_sample_questions)

        assert isinstance(test_sample_question1, str), 'This sample is more than just a string'
        self.assertNotEqual(test_sample_question1, test_sample_question2), 'The samples should not be the same'
                    


class TestExam(unittest.TestCase):

    def test_exam_object_attribute_initialization(self):
        
        test_exam = Exam({
        'What is business management?': [['a book', 'a field of study', 'a movie'], 2, 'Ionut'],
        'What is SWOT?': [['an analytical tool', 'a military force', 'a solution to business problems'], 1, 'Ada'],
        'How many forces are in The Porter Model?': [['1', '3', '5'], 3, 'Ionut']
        })

        assert hasattr(test_exam, 'q_and_a'), 'Exam has no questions. It is missing q_and_a'
        self.assertEqual(len(test_exam), 3), 'There should be precisely 3 questions when creating an exam.'

unittest.main()