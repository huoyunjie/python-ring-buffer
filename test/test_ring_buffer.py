import unittest
import random

import pytest

from ring_buffer import RingBuffer

class TestRingBuffer(unittest.TestCase):
    
    def test_initialize_params(self):
        '''
        Test that buffer init params are returned
        correctly
        '''
        random_size = random.randrange(1, 100)
        buffer = RingBuffer(random_size)

        self.assertEqual(buffer.get_capacity(), random_size)
        self.assertFalse(buffer.is_full())
        self.assertTrue(buffer.is_empty())
        self.assertEqual(buffer.get_buffer_fill(), 0)

    def test_push(self):
        '''
        Test that buffer push works
        '''
        random_size = random.randrange(1, 100)
        buffer = RingBuffer(random_size)

        buffer.push(0)

    def test_pop(self):
        '''
        Test that buffer pop returns pushed value
        '''
        random_size = random.randrange(1, 100)
        buffer = RingBuffer(random_size)

        buffer.push(0)
        returned_element = buffer.pop()

        self.assertEqual(returned_element, 0)

    def test_push_full_fail(self):
        '''
        Test that pushing into a full
        buffer raises Runtime Exception
        and the "buffer full" message
        '''
        with pytest.raises(RuntimeError, message='Buffer is full!'):
            random_size = random.randrange(1, 100)
            buffer = RingBuffer(random_size)
            for i in xrange(0, random_size + 1):
                buffer.push(i)

    def test_pop_empty_fail(self):
        '''
        Test that popping from an empty buffer
        results in RuntimeException being raised
        along with "Buffer empty" exception message
        '''
        with pytest.raises(RuntimeError, message='Buffer is empty!'):
            random_size = random.randrange(1, 100)
            buffer = RingBuffer(random_size)
            buffer.pop()

if __name__ == '__main__':
    unittest.main()