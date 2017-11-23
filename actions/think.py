"""make thoughts.
this module is responsible for thinking.
"""
from mind.thought import thought
from mind import analyze
import random
# from ignore import ignore

def think(given):
  return analyze.analyze(thought('', 'ignore', posX=random.random(), posY=random.random(), posZ=random.random(), posT=random.random()),
    thought(' '.join(given.on), 'express.printterm', posX=random.random(), posY=random.random(), posZ=random.random(), posT=random.random()))
  # return thought(' '.join(given.on), 'express.printterm')