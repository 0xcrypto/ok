"""make thoughts.
this module is responsible for thinking.

# How thinking works
Thinking depends on arbitrary data provided to think. 
"""
from mind.thought import thought
from actions.analyze import analyze
from actions.action import action
import random

class think(action):
  def do(given):
    return thought(given.on[1:], given.on[0], posX=random.random(), posY=random.random(), posZ=random.random(), posT=random.random() )
    # return analyze.do(thought('', 'ignore', posX=random.random(), posY=random.random(), posZ=random.random(), posT=random.random()),
    # thought(' '.join(given.on), 'express.printterm', posX=random.random(), posY=random.random(), posZ=random.random(), posT=random.random()))