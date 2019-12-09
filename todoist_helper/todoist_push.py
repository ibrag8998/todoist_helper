import todoist

from . import config as cf


def push(data):
    api.add_item(data)


api = todoist.TodoistAPI(cf.API_TOKEN)
api.sync()

