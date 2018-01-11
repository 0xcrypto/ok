"""Store in mind."""

from typing import Iterator
import sqlite3 as sql
import random
from actions.action import action

class memory(action):
  def __init__(self):
    super()

    createTable = '''CREATE TABLE IF NOT EXISTS thoughts (
      thought_id integer PRIMARY KEY,
      inputdata text NOT NULL,
      action text NOT NULL,
      posX integer NOT NULL,
      posY integer NOT NULL,
      posZ integer NOT NULL,
      posT text NOT NULL
      );
    '''

    self.conn = sql.connect('memories.db')
    self.cursor = self.conn.cursor()
    self.allowedActs = ['memorize', 'recall', 'forget', 'rememorize']
    self.cursor.execute(createTable)
    return self.conn.commit()

  def memorize(self, data):
    print(data)
    return thought('know', '')

  def do(self, act_on):
    return getattr(self, act_on.on[0])(act_on.on[1:])
  

# def saveMem(thought: thought):

  