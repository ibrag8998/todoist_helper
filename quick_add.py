#!/usr/bin/env python3
from todoist_helper.ui import UI
from todoist_helper.todoist_push import push
from todoist_helper import config as cf


def save(task):
    push(task)


while True:
    ui = UI()
    ui.quick_add()
    ui.mainloop()

    if ui.task.get():
        save(ui.task.get())
        ui.task.set('')
    
    if ui.close_window:
        break
