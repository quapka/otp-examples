# builtins
import unittest
from unittest import mock

# local
from spacex_tweets import get_page, parse_page, get_tweets, main

class TestSpaceXTweets(unittest.TestCase):
    def test_that_main_exists_if_missing_page(self):
        mock_requests = mock.Mock()
        mock_requests.get = mock.Mock()
        mock_requests.status_code = 400

        with mock.patch('spacex_tweets.requests', new=mock_requests):
            with self.assertRaises(SystemExit):
                main()


if __name__ == '__main__':
    unittest.main()
