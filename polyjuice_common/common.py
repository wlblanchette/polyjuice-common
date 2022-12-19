import json
from typing import List

def safe_access(dictionary: dict, properties: List):
  result = dictionary
  for p in properties:
    try:
      result = result[p]
    except:
      return None
  return result

def decorate_log_event(fn):
  def inner(*args, **kwargs):
    event = args[0]
    print('[decorate_log_event] event:', json.dumps(event))
    fn(*args, **kwargs)
  return inner