from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import RectangularRippleBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.properties import ColorProperty, NumericProperty, StringProperty, ObjectProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.behaviors import CircularRippleBehavior
from kivy.uix.image import Image


# Window.size = (365, 600)


# ============ Screens ===============

class RootScreen(MDScreen):
    pass

class RegisterScreen(MDScreen):
    pass

class SettingScreen(MDScreen):
    pass

class HomeScreen(ThemableBehavior, MDScreen):
    pass

class ChatScreen(ThemableBehavior, MDScreen):
    pass

class ListingScreen(ThemableBehavior, MDScreen):
    pass

class NotificationsScreen(ThemableBehavior, MDScreen):
    pass

class ProfileScreen(ThemableBehavior, MDScreen):
    pass

# ====================== tool bar ==================================
class DMREToolbar(ThemableBehavior, MDBoxLayout):
    # scr_manager = ObjectProperty()
    # nav_bar = ObjectProperty()
    """`Toolbar` for `DMRE` screen."""

    bottom_manu_open = False
    """Open or closed box."""

    search = False
    path_to_icon_menu = StringProperty()
    path_to_icon_logo = StringProperty()
    title = StringProperty("DMRE")

    def set_title_animation_text(self, text):
        """Animates text from `Title old` to `Title new`."""

        def set_new_text(*args):
            self.ids.title.text = text
            Animation(color=self.theme_cls.text_color, d=0.2).start(
                self.ids.title
            )

        anim = Animation(color=(0, 0, 0, 0), d=0.2)
        anim.bind(on_complete=set_new_text)
        anim.start(self.ids.title)

    def set_search_field(self):
        def set_focus_search_field(interval):
            self.ids.search_field.focus = focus

        if not self.search:
            self.search = True
            size = 0
            opacity = 1
            opacity_button_tune = 0
            disabled = False
            focus = True
            title = "SEARCH"
        else:
            self.search = False
            size = dp(42)
            opacity = 0
            opacity_button_tune = 1
            disabled = True
            focus = False
            title = self.title

        Animation(size=(size, size), opacity=opacity_button_tune, d=0.2).start(
            self.ids.button_tune
        )
        # Animation(size=(size, size), d=0.2).start(self.ids.button_logo)
        Animation(size=(size, size), d=0.2).start(self.ids.button_menu)
        self.set_title_animation_text(title)
        self.ids.search_field.disabled = disabled
        Animation(opacity=opacity, d=0.2).start(self.ids.search_field)
        Clock.schedule_once(set_focus_search_field, 0.3)

# ====================== nav bar bottom ============================

class NavigationItem(ThemableBehavior, ButtonBehavior, BoxLayout):
    duration = NumericProperty(0.3)
    button_width = NumericProperty(dp(120))
    button_height = NumericProperty(dp(40))
    text = StringProperty()
    icon = StringProperty()
    icon_color = ColorProperty()


    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_release(self):
        for button in self.parent.children:
            if button == self:
                continue
            button._button_shrink()

        self._button_expand()
        return super().on_release()

    def _button_expand(self):
        label_anim = Animation(
            opacity=1, transition="in_sine", duration=self.duration
        )
        label_anim.start(self.ids._label)

        anim = Animation(
            width=self.button_width,
            t="linear",
            duration=self.duration,
            icon_color=self.theme_cls.text_color,
        )
        anim.start(self)

    def _button_shrink(self):

        label_anim = Animation(
            opacity=0, transition="out_sine", duration=self.duration
        )
        label_anim.start(self.ids._label)

        but_anim = Animation(
            width=self.height,
            t="linear",
            duration=self.duration,
            icon_color=self.theme_cls.disabled_hint_text_color,
        )
        but_anim.start(self)

class NavigationBar(ThemableBehavior, BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_resize=self._update)
        Clock.schedule_once(lambda x: self.set_current(None))
        Clock.schedule_once(lambda x: self._update())
        self.theme_cls.primary_palette = 'Indigo'


    def _update(self, *args):
        self.width = Window.width
        buttons = self.ids._button_box.children
        button_sizes = (
            (len(buttons) - 1) * buttons[0].button_height
        ) + buttons[0].button_width
        space = self.width - button_sizes
        spacing = space / (len(buttons) + 1)
        self.ids._button_box.spacing = spacing
        self.ids._button_box.padding = [spacing, 0, spacing, 0]

    def set_current(self, index):
        if not index:
            index = -1
        button = self.ids._button_box.children[index]
        button.dispatch("on_release")

    def add_widget(self, widget, index=0, canvas=None):
        if issubclass(widget.__class__, NavigationItem):
            return self.ids._button_box.add_widget(widget)
        else:
            return super().add_widget(widget, index=(index), canvas=canvas)

class RallyListItem(ThemableBehavior, RectangularRippleBehavior, MDBoxLayout):
    text = StringProperty()
    secondary_text = StringProperty()
    tertiary_text = StringProperty()
    bar_color = ColorProperty((1, 0, 0, 1))

class RallySeeAllButton(RectangularRippleBehavior, MDBoxLayout):
    pass

# ==================================================================

class PreviousImage(CircularRippleBehavior, ButtonBehavior, Image):
    description = StringProperty()
    _root = ObjectProperty()

# ========================= Listing Classes ========================

class PropertyListItem(ThemableBehavior, MDBoxLayout):
    prop_title = StringProperty()
    prop_location = StringProperty()
    prop_price = StringProperty()
    prop_image = StringProperty()
    prop_auction_type = StringProperty()
    prop_views = StringProperty()

class DetailButton(CircularRippleBehavior, ButtonBehavior):
    description = StringProperty()
    _root = ObjectProperty()

class DMRE(MDApp):
    # def build(self):
    #     return Builder.load_string(KV)
    def build(self):
        self.load_kv("test.kv")

    def on_start(self):
        print("===========================================================")
        print("======================== starting =========================")
        print("===========================================================")

        #Get properties form db
        print(Window.size)


        # Add Properties to Page
        properties = [["Dallas, United States", "876 restaurants", "0.jpg", "30000", "Rent", "100"], ["Cordoba, Argentina", "124 restaurants", "1.jpg", "30000", "Rent", "100"], ["Portland, United States", "495 restaurants", "2.jpg", "30000", "Rent", "100"], ["Paris, France", "683 restaurants", "3.jpg", "30000", "Rent", "100"], ["Seoul, South Korea", "782 restaurants", "0.jpg", "30000", "Rent", "100"], ["Seattle, United States", "123 restaurants", "1.jpg", "30000", "Rent", "100"], ["Nashville, United States", "556 restaurants", "2.jpg", "30000", "Rent", "100"], ["Atlanta, United States", "456 restaurants", "3.jpg", "30000", "Rent", "100"]]

        properties_screen = self.root.ids.root_screen.ids.real_estate_items
        print(properties_screen)

        for i in properties:
            prop_title = i[0]
            prop_location = i[1]
            prop_price = i[3]
            prop_image = i[2]
            prop_auction_type = i[4]
            prop_views = i[5]

            properties_screen.add_widget(
                PropertyListItem(
                    prop_title = prop_title,
                    prop_location = prop_location,
                    prop_price = f"XAF {prop_price}",
                    prop_image = prop_image,
                    prop_auction_type = prop_auction_type,
                    prop_views = prop_views
                    )
            )

    def call_from_nav_item(self, for_item):
        nav_item = NavigationItem()
        home_item = self.root.ids.root_screen.ids.home_item

        if(for_item == "set_all_inactive"):
            # NavigationItem.icon_color = home_item.theme_cls.disabled_hint_text_color
            pass
        else:
            NavigationItem.on_release(home_item)





DMRE().run()
