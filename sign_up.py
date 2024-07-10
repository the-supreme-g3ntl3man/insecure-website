from nicegui import ui
import json
@ui.page('/sign_up')
def sign_up_index():
    def redirect():
        ui.navigate.to('/')
    def notification(response):
        if response == 'error:password_match':
            ui.notification('Passwords Do not match' , color='red')
        elif response =='error:username_found':
            ui.notification('Username Already Taken' , color='red')
        elif response == 'error_password':
            ui.notification('You need a Password !' , color='red')
        else:
            ui.notification('Account Created SuccessFully !')
            ui.navigate.to('/' , new_tab=False)
    def create_account(data , user , passw):
        with open('passwords.json' , 'w') as file:
            data[user] = passw
            json.dump(data , file , indent=2)
            file.close()
    def check_credentials():
        user = username.value
        passw = password.value
        passw1 = retype_password.value
        if len(passw) == 0:
            notification('error:password')
        elif passw != passw1:
            notification('error:password_match')
        else:
            with open('passwords.json' , 'r') as file:
                data = json.load(file)
                file.close()
            if user in data:
                notification('error:username_found')
            else:
                create_account(data , user , passw)
                notification("success")
    ui.page_title('Sign_up')
    ui.markdown('#Sign_up')
    username = ui.input('Username :')
    password = ui.input('Password :')
    retype_password = ui.input('Retype Password :')
    with ui.row():
        ui.button('Submit' , on_click=check_credentials)
        ui.button('Have an account ?',on_click=redirect)
    ui.run()
sign_up_index()
