import importlib
from mind.thought import thought

def do(action, act_on):
  if(type(act_on) != thought):
    act_on = thought(act_on)

  todo = action.split('.')[-1]
  try:
    action = importlib.import_module('actions.'+ action)
    return getattr(action, todo)(act_on)
    # return True

  except ImportError:
    print("\n[ok]: I don't know how to act - " + action + "." + todo + '\n')
    # return thought('raise', 'EXIT_FAILURE')
    return thought('')