import importlib
from mind.thought import thought

class action(thought):
  def do(action, act_on):
    if(type(act_on) != thought):
      act_on = thought(act_on)
    
    todo = action.split('.')[-1]

    try:
      action = importlib.import_module('actions.'+ action)
      # (act_on)

    except ImportError:
      print("\n[ok]: I don't know how to act - " + action + '.\n')
      # return thought('raise', 'EXIT_FAILURE')
      return thought('')

    try:
      return getattr(action, todo).do(act_on)

    except AttributeError:
      print("\n[ok]: I know how to act - " + action.act + " but don't want to - " + todo)