
import unittest


def classify_triangle(a, b, c):

    if a == b == c:
        return 'equilateral'

    elif a == b or a == c or b == c:
        return 'isosceles'

    elif a*a + b*b == c*c:
        return 'right'

    else:
        return 'scalene'


def main():
    print('')
    print('Now lets check our sample input:')
    print('---------------------------------------')
    print(classify_triangle(10, 1, 2))
    print(classify_triangle(1, 1, 1))
    print(classify_triangle(3, 45, 5))
    print(classify_triangle(2, 2, 2))
    print(classify_triangle(1, 3, 4))


class RunTests(unittest.TestCase):
    def test_classify_triangle(self):
        self.assertEqual(classify_triangle(1, 1, 1), "equilateral")
        self.assertEqual(classify_triangle(2, 3, 4), "scalene")
        self.assertEqual(classify_triangle(2, 2, 3), "isosceles")
        self.assertEqual(classify_triangle(6, 8, 10), "right")
        self.assertEqual(classify_triangle(2, 8, 10), "right")
        print('')

if __name__ == "__main__":
    unittest.main(exit = False, verbosity = 2)
    main()