"""
Kahoot hacker app
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class Kahoothekerapp(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box(style=Pack(direction=COLUMN, a))
        left_box = toga.Box(style=Pack(direction=ROW, flex=0.5))
        right_box = toga.Box(style=Pack(direction=ROW, flex=0.5))

        url_label = toga.Label("URL >>", style=Pack(flex=0.3))
        url_input = toga.TextInput(style=Pack(flex=0.7))

        enter_button = toga.Button("ENTER", style=Pack(flex=1))    


        left_box.add(url_label); left_box.add(url_input)
        main_box.add(left_box); main_box.add(right_box)
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return Kahoothekerapp()
