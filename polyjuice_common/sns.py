import json
from typing import Callable

from polyjuice_common.common import safe_access

def unpack_sns_message(fn: Callable):
  """
  Unpacks an Sns event's message adds it as a kwarg
  """
  def inner(*args, **kwargs):
    sns_payload = json.loads(safe_access(args[0], ['Records', 0, 'Sns', 'Message']))
    return fn(*args, **kwargs, sns_payload=sns_payload)
  return inner