from structure.atom import Atom
from structure.rule import Rule

class RuleReader(object):

  def __init__(self, path='output/test.txt'):
    self.path = path
  
  def __parsing(self, str_rule):
    token = str_rule.split('\t')
    rule = Rule()
    rule.init_measure(int(token[0]), int(token[1]), float(token[2]))
    atoms = token[3].split(' ')
    head = Atom()
    head.from_atom_representation(atoms[0])
    rule.head = head
    for i in range(2, len(atoms)):
      atom_body = Atom()
      atom_body.from_atom_representation(atoms[i])
      rule.body.append(atom_body)
    return rule

  def read(self):
    rules = []
    file_reader = open(self.path, 'r')
    for line in file_reader:
      rule = self.__parsing(line)
      rules.append(rule)
    return rules