from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from contents.data import LESSONS, BRANCHES, CONTENT

# Main Menu Screen
class MainMenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        self.label = Label(text="Course Index", size_hint=(0.8, 0.1), pos_hint={'center_x': 0.5, 'top': 1}, font_size=Window.width * 0.05)
        layout.add_widget(self.label)

        for i, lesson in enumerate(LESSONS):
            btn = Button(text=lesson, size_hint=(0.8, 0.1), pos_hint={'center_x': 0.5, 'top': 0.9 - i * 0.1}, padding=(0, 20))
            btn.bind(on_release=self.open_lesson)
            layout.add_widget(btn)

        self.add_widget(layout)
        Window.bind(on_resize=self._update_font_size)

    def open_lesson(self, instance):
        print(f"Opening lesson: {instance.text}")
        self.manager.current = "lesson_screen"
        self.manager.get_screen("lesson_screen").load_lesson(instance.text)

    def _update_font_size(self, *args):
        self.label.font_size = Window.width * 0.05
        for child in self.children[0].children:
            if isinstance(child, Button):
                child.font_size = Window.width * 0.04


# Lesson Screen
class LessonScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = FloatLayout()
        self.add_widget(self.layout)
        Window.bind(on_resize=self._update_font_size)

    def load_lesson(self, lesson_title):
        print(f"Loading lesson: {lesson_title}")
        self.layout.clear_widgets()

        self.label = Label(
            text=lesson_title,
            size_hint=(0.8, 0.1),
            pos_hint={'center_x': 0.5, 'top': 1},
            font_size=Window.width * 0.05,
            text_size=(Window.width * 0.8, None),
            halign='center',
            valign='middle'
        )
        self.label.bind(size=self._update_text_size)
        self.layout.add_widget(self.label)

        for i, branch in enumerate(BRANCHES.get(lesson_title, [])):
            btn = Button(text=branch, size_hint=(0.8, 0.1), pos_hint={'center_x': 0.5, 'top': 0.9 - i * 0.1}, padding=(0, 20))
            btn.bind(on_release=self.open_branch)
            self.layout.add_widget(btn)

        back_btn = Button(text="Back", size_hint=(0.8, 0.1), pos_hint={'center_x': 0.5, 'top': 0.1}, background_color=(1, 0, 0, 1), padding=(0, 20))
        back_btn.bind(on_release=self.go_back)
        self.layout.add_widget(back_btn)

    def open_branch(self, instance):
        print(f"Opening branch: {instance.text}")
        self.manager.current = "content_screen"
        self.manager.get_screen("content_screen").load_content(instance.text)

    def go_back(self, instance):
        print("Going back to main menu")
        self.manager.current = "main_menu"

    def _update_font_size(self, *args):
        self.label.font_size = Window.width * 0.05
        for child in self.layout.children:
            if isinstance(child, Button):
                child.font_size = Window.width * 0.04

    def _update_text_size(self, instance, value):
        instance.text_size = (instance.width, None)
        instance.texture_update()
        instance.height = instance.texture_size[1]


# Content Screen
class ContentScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = FloatLayout()
        self.add_widget(self.layout)
        Window.bind(on_resize=self._update_font_size)

    def load_content(self, branch_title):
        print(f"Loading content for branch: {branch_title}")
        self.layout.clear_widgets()

        self.label = Label(
            text=CONTENT.get(branch_title, "No content available."),
            size_hint=(0.8, 0.8),
            pos_hint={'center_x': 0.5, 'top': 1},
            font_size=Window.width * 0.05,
            text_size=(Window.width * 0.8, None),
            halign='center',
            valign='middle'
        )
        self.label.bind(size=self._update_text_size)
        self.layout.add_widget(self.label)

        back_btn = Button(text="Back", size_hint=(0.8, 0.1), pos_hint={'center_x': 0.5, 'top': 0.1}, background_color=(1, 0, 0, 1), padding=(0, 20))
        back_btn.bind(on_release=self.go_back)
        self.layout.add_widget(back_btn)

    def go_back(self, instance):
        print("Going back to lesson screen")
        self.manager.current = "lesson_screen"

    def _update_font_size(self, *args):
        self.label.font_size = Window.width * 0.05
        for child in self.layout.children:
            if isinstance(child, Button):
                child.font_size = Window.width * 0.04

    def _update_text_size(self, instance, value):
        instance.text_size = (instance.width, None)
        instance.texture_update()
        instance.height = instance.texture_size[1]


# Ensure the classes are exported correctly
__all__ = ['MainMenuScreen', 'LessonScreen', 'ContentScreen']
