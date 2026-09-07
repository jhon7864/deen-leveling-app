"""
Deen Leveling — Kivy front-end.

This is a minimal but real, buildable mobile UI using Kivy, styled with
the same emerald/gold/parchment palette as the HTML mockup. It's wired
to placeholder data for now — swap the TODO-marked spots for calls into
the `deen_leveling` Python package (User, SalahTracker, etc.) once
you're ready to connect real logic.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.properties import StringProperty, NumericProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout

KV = """
#:import dp kivy.metrics.dp

<SalahPill@BoxLayout>:
    prayer_name: "Fajr"
    done: False
    orientation: "vertical"
    padding: dp(4), dp(10)
    spacing: dp(6)
    canvas.before:
        Color:
            rgba: (0.79, 0.64, 0.29, 0.22) if self.done else (0.93, 0.90, 0.83, 1)
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [14]
    Widget:
        size_hint_y: None
        height: dp(30)
        canvas:
            Color:
                rgba: (0.79, 0.64, 0.29, 1) if root.done else (0.85, 0.82, 0.74, 1)
            Ellipse:
                pos: self.center_x - dp(15), self.top - dp(30)
                size: dp(30), dp(30)
    Label:
        text: root.prayer_name
        font_size: "11sp"
        bold: True
        color: (0.17, 0.14, 0.10, 1)
        size_hint_y: None
        height: dp(16)

<HomeScreen>:
    BoxLayout:
        orientation: "vertical"
        padding: dp(22), dp(30)
        spacing: dp(4)
        canvas.before:
            Color:
                rgba: (0.97, 0.95, 0.91, 1)
            Rectangle:
                pos: self.pos
                size: self.size

        Label:
            text: "Deen Leveling"
            font_size: "13sp"
            color: (0.42, 0.38, 0.32, 1)
            size_hint_y: None
            height: dp(18)
            halign: "left"
            text_size: self.size

        Label:
            text: "Assalamu alaikum, " + app.user_name
            font_size: "22sp"
            bold: True
            color: (0.17, 0.14, 0.10, 1)
            size_hint_y: None
            height: dp(34)
            halign: "left"
            text_size: self.size

        # --- Level card ---
        BoxLayout:
            size_hint_y: None
            height: dp(90)
            padding: dp(16)
            spacing: dp(14)
            canvas.before:
                Color:
                    rgba: (0.07, 0.21, 0.14, 1)
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [20]

            Label:
                text: str(app.baraka_percent) + "%"
                color: (0.90, 0.81, 0.58, 1)
                bold: True
                size_hint_x: None
                width: dp(60)

            BoxLayout:
                orientation: "vertical"
                Label:
                    text: "STEADFAST BEGINNER"
                    font_size: "11sp"
                    bold: True
                    color: (0.90, 0.81, 0.58, 1)
                    halign: "left"
                    text_size: self.size
                    size_hint_y: None
                    height: dp(16)
                Label:
                    text: str(app.total_baraka) + " Baraka"
                    font_size: "18sp"
                    color: (1, 1, 1, 1)
                    halign: "left"
                    text_size: self.size
                    size_hint_y: None
                    height: dp(24)
                Label:
                    text: str(app.baraka_to_next) + " to next level"
                    font_size: "11sp"
                    color: (1, 1, 1, 0.6)
                    halign: "left"
                    text_size: self.size
                    size_hint_y: None
                    height: dp(16)

        Label:
            text: "Today's Salah"
            font_size: "13sp"
            bold: True
            color: (0.42, 0.38, 0.32, 1)
            size_hint_y: None
            height: dp(30)
            halign: "left"
            text_size: self.size
            padding_y: dp(10)

        # --- Salah row ---
        BoxLayout:
            size_hint_y: None
            height: dp(78)
            spacing: dp(8)
            SalahPill:
                prayer_name: "Fajr"
                done: True
                on_touch_down: if self.collide_point(*args[1].pos): self.done = not self.done
            SalahPill:
                prayer_name: "Dhuhr"
                done: True
                on_touch_down: if self.collide_point(*args[1].pos): self.done = not self.done
            SalahPill:
                prayer_name: "Asr"
                done: False
                on_touch_down: if self.collide_point(*args[1].pos): self.done = not self.done
            SalahPill:
                prayer_name: "Maghrib"
                done: False
                on_touch_down: if self.collide_point(*args[1].pos): self.done = not self.done
            SalahPill:
                prayer_name: "Isha"
                done: False
                on_touch_down: if self.collide_point(*args[1].pos): self.done = not self.done

        # --- Qada strip ---
        BoxLayout:
            size_hint_y: None
            height: dp(46)
            padding: dp(14), 0
            canvas.before:
                Color:
                    rgba: (0.87, 0.82, 0.68, 1)
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [14]
            Label:
                text: "Prayers to catch up on"
                font_size: "13sp"
                color: (0.17, 0.14, 0.10, 1)
                halign: "left"
                text_size: self.size
            Label:
                text: str(app.qada_owed)
                font_size: "13sp"
                bold: True
                color: (0.79, 0.64, 0.29, 1)
                size_hint_x: None
                width: dp(24)

        Widget:
            size_hint_y: None
            height: dp(16)

        # --- Quran card ---
        BoxLayout:
            orientation: "vertical"
            size_hint_y: None
            height: dp(120)
            padding: dp(16)
            spacing: dp(6)
            canvas.before:
                Color:
                    rgba: (0.09, 0.23, 0.16, 1)
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [18]

            BoxLayout:
                size_hint_y: None
                height: dp(22)
                Label:
                    text: "Qur'an"
                    color: (1, 1, 1, 1)
                    font_size: "16sp"
                    halign: "left"
                    text_size: self.size
                Label:
                    text: str(app.quran_streak) + " day streak"
                    color: (0.90, 0.81, 0.58, 1)
                    font_size: "12sp"
                    bold: True
                    halign: "right"
                    text_size: self.size

            Label:
                text: "Al-Baqarah, page 12"
                color: (1, 1, 1, 0.65)
                font_size: "12sp"
                halign: "left"
                text_size: self.size
                size_hint_y: None
                height: dp(16)

            Button:
                text: "Log today's reading"
                bold: True
                background_normal: ""
                background_color: (0.79, 0.64, 0.29, 1)
                color: (0.07, 0.21, 0.14, 1)
                size_hint_y: None
                height: dp(40)
                on_release: app.log_quran()

ScreenManager:
    HomeScreen:
        name: "home"
"""


class HomeScreen(Screen):
    pass


class DeenLevelingApp(App):
    user_name = StringProperty("Yusuf")
    total_baraka = NumericProperty(86)
    baraka_percent = NumericProperty(86)
    baraka_to_next = NumericProperty(14)
    qada_owed = NumericProperty(2)
    quran_streak = NumericProperty(4)

    def build(self):
        return Builder.load_string(KV)

    def log_quran(self):
        # TODO: wire this to deen_leveling.user.User.log_quran_reading(...)
        self.total_baraka += 3
        self.quran_streak += 1


if __name__ == "__main__":
    DeenLevelingApp().run()
