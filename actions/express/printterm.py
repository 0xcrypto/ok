""" Print on terminal """
from mind.thought import thought

class printterm(thought):
  def do(given):
    print( ' '.join(given.on) )