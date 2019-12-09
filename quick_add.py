#!/usr/bin/env python3
from time import strftime

from todoist_helper.ui import UI
from todoist_helper.todoist_push import push


def save(task):
    if task:
        push(task)


while True:
    ui = UI()
    ui.quick_add()
    ui.mainloop()

    save(ui.task.get())
    ui.task.set('')
    
    if ui.close_window:
        break
