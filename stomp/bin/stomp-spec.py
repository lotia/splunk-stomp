import mock
import unittest
import stomp


class TestStompOutputsHealthy(unittest.TestCase):

    def test_outputs_healthy_makes_correct_socket_calls(self):
        outputs_to_monitor = ['blah-1:8080', 'blah-2:4567']
        with mock.patch('socket.socket'):
            result = stomp.outputs_healthy(outputs_to_monitor)
        self.assertEquals(result, True)


if __name__ == '__main__':
    unittest.main()