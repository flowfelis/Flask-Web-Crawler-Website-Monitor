import unittest
import helpers


class MyTestCase(unittest.TestCase):
    def test_monitor_site_works(self):
        site = helpers.monitor_site('https://www.google.com', 'search')
        result = site[0]
        self.assertEqual(result, '200')

    def test_satisfy_req(self):
        site = helpers.monitor_site('https://www.google.com', 'search')
        result = site[1]
        self.assertEqual(result, 'True')

    def test_down_site(self):
        site = helpers.monitor_site('https://www.randomwebsite.com', 'random')
        result = site[0]
        self.assertEqual(result, 'Down')


if __name__ == '__main__':
    unittest.main()
