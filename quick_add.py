#!/usr/bin/env python3
from time import strftime

from todoist_helper.ui import UI
from todoist_helper.todoist_push import push


ui = UI()
ui.quick_add()
ui.mainloop()

task = ui.task.get()
if task:
    push(task)
