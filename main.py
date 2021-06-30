from kivymd.app import MDApp
from kivymd.uix.picker import MDDatePicker, MDThemePicker, MDTimePicker
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase
from kivy.core.window import Window


Window.size = (365, 600)


class DMRE(MDApp):
    # def build(self):
    #     return Builder.load_string(KV)
    def build(self):
        self.load_kv("main.kv")

    def on_start(self):
        # self.theme_cls.primary_palette = '#00E5FF'
        print("starting...")
        #initialize GPS


    def get_time(self, instance, time):
        self.root.ids.time_picker_label.text = str(time)

    def show_example_time_picker(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(time=self.get_time)
        time_dialog.open()

    def get_date(self, date_obj):
        self.root.ids.date_picker_label.text = str(date_obj)

    def show_example_date_picker(self):
        date_dialog = MDDatePicker(callback=self.get_date)
        date_dialog.open()

    def show_example_theme_picker(self):
        MDThemePicker().open()




DMRE().run()
