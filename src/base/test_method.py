# coding:utf-8
import unittest
from demo import RunMain
from mock import mock
from mock_demo import mock_test

class TestMethod(unittest.TestCase):

    def setUp(self):
        self.run = RunMain()

    def tearDown(self):
        print('tearDown')

    def test_01(self):
        data = {
            "weatherinfo": {
                "city": "\u00e5\u008c\u0097\u00e4\u00ba\u00ac",
                "cityid": "101010102",
                "img1": "n1.gif",
                "img2": "d2.gif",
                "ptime": "18:00",
                "temp1": "18\u00e2\u0084\u0083",
                "temp2": "31\u00e2\u0084\u0083",
                "weather": "\u00e5\u00a4\u009a\u00e4\u00ba\u0091\u00e8\u00bd\u00ac\u00e9\u0098\u00b4"
            }
        }
        url = 'http://www.weather.com.cn/data/cityinfo/101010100.html'

        # mock返回的数据
        # mock_data = mock.Mock(return_value = data)
        # print(mock_data)
        # self.run.run_main = mock_data

        # 单独封装的mock方法
        mock_test(self.run.run_main,url,'GET',data)

        req = self.run.run_main(url,'GET')
        # print(req['weatherinfo']['cityid'])
        self.assertEqual(req['weatherinfo']['cityid'], '101010102', '正确的代码')

    # def test_02(self):
    #     print('this is 02 方法')

if __name__ == '__main__':
    unittest.main()