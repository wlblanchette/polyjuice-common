from typing import List

def safe_access(dictionary: dict, properties: List):
  result = dictionary
  for p in properties:
    try:
      result = result[p]
    except:
      return None
  return result