# tdd_mock_request
Small example to use the patch decorator to mock requests


dependencies
for python2.7.x:

  requests
  
  mock
  
for python3:
  requests
  
  
Exercise to practice api requests mocking

MainClass().make_call() calls the post_request static method of RequestClass and return the value returned from post_request

In order to unit test MainClass, I've mocked the return value of post_request
