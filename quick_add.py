#!/usr/bin/env python3
from todoist_helper.ui import UI


def save(task):
    push(task)


imported = False
while True:
    ui = UI()
    ui.quick_add()
    ui.mainloop()

    if not imported: # it was made because gui window appearance was very slow, now its better
        from todoist_helper.todoist_push import push
        imported = True

    if ui.task.get():
        save(ui.task.get())
        ui.task.set('')
    
    if ui.close_window:
        break
