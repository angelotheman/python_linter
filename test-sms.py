#!/usr/bin/python3
"""
Testing with different number
"""
def test_file():
  """
  This would have indentation issues etc
  """
      print("This is a wrong indentation")

def long_columns():
  """
  This would test for long characters above 79
  """
  print("This is a very very long script which si actually meant to violate the pycodestyle script. This is why it is over 80 lines so that the script would break")

def main():
  test_file()

if __name__ == '__main__':
  main()
