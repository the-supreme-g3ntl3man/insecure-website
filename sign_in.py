from nicegui import ui
import json
from home import * 
from redirect import * 
@ui.page('/')
def sign_in_index():
    def redirect_sign_up():
        redirect('/sign_up')
    def notification(response , username):
        if response == 'error':
            ui.notification('Incorrect Username or Password !' , color='red')
        else:
            ui.notification(f'Welcome {username} !')
            redirect('/home')
    def check_credentials():
        user = username.value
        passw = password.value
        with open('passwords.json' , 'r') as file:
            data = json.load(file)
            file.close()
        if user in data:
            if data[user] == passw:
                notification('success' , user)
            else:
                notification('error', user)
        else:
            notification('error', user)
    ui.page_title('Sign_in')
    ui.markdown("#Sign_in")
    username = ui.input('Username :')
    password = ui.input('Password :')
    with ui.row():
        ui.button('Submit' , on_click=check_credentials)
        ui.button('Don't Have an Account?' , on_click=redirect_sign_up)
    
sign_in_index()
