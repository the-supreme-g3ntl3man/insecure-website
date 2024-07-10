from nicegui import ui

@ui.page('/home')

    
def index():
    ui.markdown(f'#Hello World !')
   