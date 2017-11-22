"""make thoughts.
this module is responsible for thinking.
"""

from mind.thought import thought

def think(given):
  # print(given)
  # return True
  return thought(' '.join(given.on), 'express.printterm')