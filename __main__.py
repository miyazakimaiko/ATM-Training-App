from user_main_menu import run_user_main_menu
from login_menu import show_login_menu_title, login_user

show_login_menu_title()

user = login_user()

if user:
    from user_main_menu import run_user_main_menu
    run_user_main_menu(user)