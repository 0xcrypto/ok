"""make thoughts.
Will accept sensory inputs in future.
"""

from mind.thought import thought

def think(given):
  # print(given)
  # return True
  return thought(' '.join(given.on), 'express.printterm')