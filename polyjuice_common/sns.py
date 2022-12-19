import json
from typing import Callable

from polyjuice_common.common import safe_access

def unpack_sns_message(fn: Callable):
  """
  Unpacks an Sns event's message adds it as a kwarg
  """
  def inner(*args, **kwargs):
    payload = safe_access(args[0], ['Records', 0, 'Sns', 'Message'])
    if payload:
      sns_payload = json.loads(payload)
      return fn(*args, **kwargs, sns_payload=sns_payload)
    print('[unpack_sns_message] Not an Sns payload')
    return None
  return inner