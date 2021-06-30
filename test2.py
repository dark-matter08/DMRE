from kivy.lang import Builder
from kivymd.app import MDApp

KV = """
<MyTile@SmartTileWithStar>
    size_hint_y: None
    height: "240dp"


ScrollView:

    MDGridLayout:
        cols: 3
        adaptive_height: True
        padding: dp(4), dp(4)
        spacing: dp(4)

        MyTile:
            stars: 5
            source: "1.jpg" # put your source

        MyTile:
            stars: 5
            source: "2.jpg" # put your source

        MyTile:
            stars: 5
            source: "3.jpg" # put your source
"""


class Example(MDApp):
    def build(self):
        return Builder.load_string(KV)


Example().run()
