## In programming, the labor of writing code is not the only element to the process.
## Other important procedures play important roles in the pipeline, and are often overlooked.
##
## Testing
## In order to make sure that our code is working properly, we need to put it through specific tests.
#
# A joke always comes to mind:
"""
A quality assurance engineer walks in a bar. He orders 1 beer. He orders 0 beers. He orders 99999 beers. He orders -1 beers. He orders abccdfad beers.
A customer walks in a bar and asks where the toilet is. The bar explodes, killing everyone in it.
"""
## It goes to show, that as much as we can predict the behaviour and test our code, we should be able to think outside the box and come up with test that push the limits of our functions.

## Unit testing
## Unit testing denotes the focus on individual small units of the software, as opposed to the entire program. It is usually the first step of a testing pipeline, and once we are reasonably confident that the individual components of our program are working correctly, we move on to test how they work together.
## In python, uni testing can be easily implemented using the unittest module.
import unittest

class SampleTest(unittest.TestCase):
    def test_equal(self):
        # In this test case, we are checking whether two given quantites are equal, using the assertEqual() method
        self.assertEqual(2 ** 3 - 1, 7)
        self.assertEqual('Hello, world!', 'Hello, ' + 'world!')
    
    def test_true(self):
        # Similarly, the assertTrue() method is evaluated True or not
        self.assertTrue(2 ** 3 < 3 ** 2)
        for x in range(10):
            self.assertTrue(- x ** 2 <= 0)

#To run the tests
unittest.main()