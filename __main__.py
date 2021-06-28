import user_main_menu
import login_menu

login_menu.show_login_menu_title()

user = login_menu.login_user()

if user:
    user_main_menu.run_user_main_menu(user)