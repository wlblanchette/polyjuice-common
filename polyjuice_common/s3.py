from typing import Callable

from polyjuice_common.common import safe_access

TEST_PROJECT_ID = "s3://ab-283419117448-s2t-audio/TEST_PROJECT/"
AUDIO_BUCKET_NAME = "ab-283419117448-s2t-audio"
PROJECTS_BASE_PATH = "project-files"

def get_project_path(project_id=TEST_PROJECT_ID, *segments):
  return "/".join([PROJECTS_BASE_PATH, project_id, *segments])

def get_project_from_key(s3_key: str):
  if s3_key.startswith(PROJECTS_BASE_PATH):
    return s3_key.split('/')[1] if s3_key.split('/') else None
  return None

def handle_s3_notification_events(fn: Callable):
  def inner(*args, **kwargs):
    event = args[0]
    bucket_name = safe_access(event, ['Records', 0, 's3', 'bucket', 'name'])
    key = safe_access(event, ['Records', 0, 's3', 'object', 'key'])
    kwargs["bucket_name"] = bucket_name
    kwargs["key"] = key
    fn(*args, **kwargs)
  return inner