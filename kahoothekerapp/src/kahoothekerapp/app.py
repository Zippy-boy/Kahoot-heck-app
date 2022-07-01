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
        self.main_box = toga.Box(style=Pack(direction=COLUMN))
        veiw_box = toga.Box(style=Pack(direction=ROW))
        left_box = toga.Box(style=Pack(direction=COLUMN, flex=0.45, padding_top=20))
        self.right_box = toga.Box(style=Pack(direction=ROW, flex=0.45, padding_top=20))

        TITLE = toga.Label(
            "Kahoot heker app",
            style=Pack(padding=5, font_size=20, alignment="top", text_align="center"),
        )

        url_label = toga.Label(
            "Enter the end of the url",
            style=Pack(flex=1, font_size=15, alignment="top", text_align="center"),
        )
        self.url_input = toga.TextInput(
            style=Pack(
                flex=1, padding=20, font_size=15, alignment="top", text_align="center"
            )
        )
        url_explain_label = toga.Label(
            "Look at the host screen\n and take the end of the url\n shown at the end and click the\n ENTER button\n then resize the window",
            style=Pack(flex=1, font_size=15, text_align="center"),
        )
        url_image = toga.ImageView(image="UDumb.png", style=Pack(flex=1, height=70))

        enter_button = toga.Button(
            "ENTER",
            style=Pack(flex=1, padding=20, font_size=15),
            on_press=self.enter_button_pressed,
        )

        self.question_label = toga.Label(
            "", style=Pack(font_size=10, text_align="left")
        )
        self.awners_label = toga.Label("", style=Pack(font_size=10, text_align="right"))

        left_box.add(url_label)
        left_box.add(self.url_input)
        left_box.add(url_explain_label)
        left_box.add(url_image)
        left_box.add(enter_button)
        self.right_box.add(self.question_label)
        self.right_box.add(self.awners_label)
        veiw_box.add(left_box)
        veiw_box.add(self.right_box)
        self.main_box.add(TITLE)
        self.main_box.add(toga.Divider())
        self.main_box.add(veiw_box)
        self.main_window = toga.MainWindow(title=self.formal_name, size=(1500, 500))
        self.main_window.content = self.main_box
        self.main_window.show()

    def enter_button_pressed(self, widget):
        import requests

        thekahootid = self.url_input.value

        url = "https://create.kahoot.it/details/" + thekahootid

        kahoot_id = url.split("/")[-1]
        answers_url = f"https://create.kahoot.it/rest/kahoots/{kahoot_id}/card/?includeKahoot=true"
        data = requests.get(answers_url).json()

        for q in data["kahoot"]["questions"]:
            try:
                for choice in q["choices"]:
                    try:
                        if choice["correct"]:
                            break
                    except:
                        pass
            except:
                pass
            self.question_label.text = (
                self.question_label.text
                + "\n\n"
                + (q["question"].replace("&nbsp;", " ")).strip()
            )
            self.awners_label.text = (
                self.awners_label.text
                + "\n\n"
                + "{}".format(choice["answer"].replace("&nbsp;", " "))
            )
            print(
                "Q: {:<70} A: {} ".format(
                    q["question"].replace("&nbsp;", " "),
                    choice["answer"].replace("&nbsp;", " "),
                )
            )


def main():
    return Kahoothekerapp()
