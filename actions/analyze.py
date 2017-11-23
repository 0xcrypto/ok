from actions.action import action

class analyze(action):
  def do(firstthought, secondthought):
    # binary decision on positioning the thought.
    thinkingFirst = firstthought.position['x'] > secondthought.position['x']
    thinkingFirst = (firstthought.position['y'] > secondthought.position['y']) != thinkingFirst
    thinkingFirst =(firstthought.position['z'] > secondthought.position['z']) != thinkingFirst
    thinkingFirst =(firstthought.position['t'] > secondthought.position['t']) != thinkingFirst
    return firstthought if thinkingFirst else secondthought
