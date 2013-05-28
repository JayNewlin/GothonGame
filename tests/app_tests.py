from nose.tools import *
from bin.app import *
from tests.tools import assert_response

def test_index():
	# test our first GET request to /game
	resp = app.request("/game")
	assert_response(resp)
	resp = app.request("/")
	assert_response(resp, status="303")


	# make sure default values work for the form
	#resp = app.request("/hello", method="POST")
	#assert_response(resp, contains="Nobody")

	# test that we get expected values
	#data = {'name': 'Jay', 'greet': 'Hiya'}
	#resp = app.request("/hello", method="POST", data=data)
	#assert_response(resp, contains="Jay")
