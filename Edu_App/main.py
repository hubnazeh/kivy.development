from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from uix.screens import MainMenuScreen, LessonScreen, ContentScreen


class CourseApp(App):
    def build(self):
        print("Building the ScreenManager and adding screens")
        sm = ScreenManager()
        sm.add_widget(MainMenuScreen(name="main_menu"))
        sm.add_widget(LessonScreen(name="lesson_screen"))
        sm.add_widget(ContentScreen(name="content_screen"))
        print("Screens added to ScreenManager")
        return sm


if __name__ == "__main__":
    print("Starting CourseApp")
    CourseApp().run()
    print("CourseApp has started")
