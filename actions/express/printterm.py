""" Print on terminal """
from mind.thought import thought

class printterm(thought):
  def do(self, given):
    print( ' '.join(given.on) )