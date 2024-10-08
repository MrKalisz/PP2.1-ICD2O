import os.path
import sys
import PP1_10

def test_q1_1(capsys):

	try:
		exists = os.path.exists("PP1_10.py")
		assert exists
	except:
		sys.exit()

	input_values = ['6.25']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_10.input = mock_input

	PP1_10.q1()
	captured = capsys.readouterr()
	assert captured.out == "Input a number: 2.5\n"

def test_q2_1(capsys):

	try:
		exists = os.path.exists("PP1_10.py")
		assert exists
	except:
		sys.exit()

	input_values = ['5']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_10.input = mock_input

	PP1_10.q2()
	captured = capsys.readouterr()
	assert captured.out == "Input a number: 2\n"

def test_q3_1(capsys):

	try:
		exists = os.path.exists("PP1_10.py")
		assert exists
	except:
		sys.exit()

	input_values = ['9']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_10.input = mock_input

	PP1_10.q3()
	captured = capsys.readouterr()
	assert captured.out == "Input a number: 9\n"

def test_q4_1(capsys):

	try:
		exists = os.path.exists("PP1_10.py")
		assert exists
	except:
		sys.exit()

	input_values = ['0']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_10.input = mock_input

	PP1_10.q4()
	captured = capsys.readouterr()
	assert captured.out == "Input a number: 0\n"

def test_q5_1(capsys):

	try:
		exists = os.path.exists("PP1_10.py")
		assert exists
	except:
		sys.exit()

	input_values = ['0', '5']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_10.input = mock_input

	PP1_10.q5()
	captured = capsys.readouterr()
	assert captured.out == "Input a number: Input another number: 0\n"

def test_q1_2(capsys):

	try:
		exists = os.path.exists("PP1_10.py")
		assert exists
	except:
		sys.exit()

	input_values = ['9']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_10.input = mock_input

	PP1_10.q1()
	captured = capsys.readouterr()
	assert captured.out == "Input a number: 3.0\n"

def test_q2_2(capsys):

	try:
		exists = os.path.exists("PP1_10.py")
		assert exists
	except:
		sys.exit()

	input_values = ['9']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_10.input = mock_input

	PP1_10.q2()
	captured = capsys.readouterr()
	assert captured.out == "Input a number: 3\n"

def test_q3_2(capsys):

	try:
		exists = os.path.exists("PP1_10.py")
		assert exists
	except:
		sys.exit()

	input_values = ['8.5']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_10.input = mock_input

	PP1_10.q3()
	captured = capsys.readouterr()
	assert captured.out == "Input a number: 8\n"

def test_q4_2(capsys):

	try:
		exists = os.path.exists("PP1_10.py")
		assert exists
	except:
		sys.exit()

	input_values = ['2.3']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_10.input = mock_input

	PP1_10.q4()
	captured = capsys.readouterr()
	assert captured.out == "Input a number: 3\n"

def test_q5_2(capsys):

	try:
		exists = os.path.exists("PP1_10.py")
		assert exists
	except:
		sys.exit()

	input_values = ['5', '10']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_10.input = mock_input

	PP1_10.q5()
	captured = capsys.readouterr()
	assert captured.out == "Input a number: Input another number: 25\n"

def test_q1_3(capsys):

	try:
		exists = os.path.exists("PP1_10.py")
		assert exists
	except:
		sys.exit()

	input_values = ['25']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_10.input = mock_input

	PP1_10.q1()
	captured = capsys.readouterr()
	assert captured.out == "Input a number: 5.0\n"

def test_q2_3(capsys):

	try:
		exists = os.path.exists("PP1_10.py")
		assert exists
	except:
		sys.exit()

	input_values = ['17']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_10.input = mock_input

	PP1_10.q2()
	captured = capsys.readouterr()
	assert captured.out == "Input a number: 4\n"

def test_q3_3(capsys):

	try:
		exists = os.path.exists("PP1_10.py")
		assert exists
	except:
		sys.exit()

	input_values = ['8.1']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_10.input = mock_input

	PP1_10.q3()
	captured = capsys.readouterr()
	assert captured.out == "Input a number: 8\n"

def test_q4_3(capsys):

	try:
		exists = os.path.exists("PP1_10.py")
		assert exists
	except:
		sys.exit()

	input_values = ['1.7']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_10.input = mock_input

	PP1_10.q4()
	captured = capsys.readouterr()
	assert captured.out == "Input a number: 2\n"

def test_q5_3(capsys):

	try:
		exists = os.path.exists("PP1_10.py")
		assert exists
	except:
		sys.exit()

	input_values = ['3', '5']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_10.input = mock_input

	PP1_10.q5()
	captured = capsys.readouterr()
	assert captured.out == "Input a number: Input another number: 7\n"

