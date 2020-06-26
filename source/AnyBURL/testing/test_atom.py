import sys
sys.path.append('..')
import unittest
from structure.atom import Atom

# class TestCuboid(unittest.TestCase):

def setUp():
  a1 = Atom('A', 'relation', 'B', False, False)
  a2 = Atom('A', 'relation', 'b', False, True)
  a3 = Atom('a', 'relation', 'B', True, False)
  a4 = Atom('a', 'relation', 'b', True, True)
  a5 = Atom('A', 'relation', 'c', False, True)

def more_special():
  a1 = Atom('A', 'relation', 'B', False, False)
  a2 = Atom('A', 'relation', 'b', False, True)
  a3 = Atom('a', 'relation', 'B', True, False)
  a4 = Atom('a', 'relation', 'b', True, True)
  a5 = Atom('A', 'relation', 'c', False, True)
  print('-----------------case 1---------------------')
  print(a1.more_special(a2))
  print(a1.more_special(a3))
  print(a1.more_special(a4))
  print('-----------------case 2---------------------')
  print(a2.more_special(a1))
  print(a2.more_special(a3))
  print(a2.more_special(a4))
  print(a2.more_special(a5))
  print('-----------------case 3---------------------')
  print(a3.more_special(a1))
  print(a3.more_special(a2))
  print(a3.more_special(a4))
  print('-----------------case 4---------------------')
  print(a4.more_special(a1))
  print(a4.more_special(a2))
  print(a4.more_special(a3))
  return True

if __name__ == '__main__':
  more_special()