from nicegui import ui
from sign_up import *
from sign_in import *

def redirect(link):
    ui.navigate.to(link , new_tab=False)
ui.run()