from mock import mock

def mock_test(mock_method,url,method,response_data,request_data=None):
    mock_method = mock.Mock(return_value=response_data)
    res = mock_method(url,method,request_data)
    return res