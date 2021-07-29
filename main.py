from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.theming import ThemableBehavior
from kivy.uix.behaviors.touchripple import TouchRippleBehavior
from kivymd.uix.behaviors import RectangularRippleBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screen import MDScreen
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.properties import ColorProperty, NumericProperty, StringProperty, ObjectProperty, BooleanProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.behaviors import CircularRippleBehavior
from kivy.uix.image import Image
from kivymd.uix.textfield import MDTextField
from functools import partial
import db
import json


Window.size = (365, 600)


# ============ Screens ===============

class RootScreen(MDScreen):
    pass

class RegisterScreen(MDScreen):
    def next(self):
        app = MDApp.get_running_app()
        self.ids.slide.load_next(mode="next")
        self.ids.name.text_color = app.theme_cls.primary_color
        self.ids.progress.value = 100
        self.ids.name_icon.text_color = app.theme_cls.primary_color
        self.ids.name_icon.icon = "check-decagram"

    def next1(self):
        app = MDApp.get_running_app()
        self.ids.slide.load_next(mode="next")
        self.ids.contact.text_color = app.theme_cls.primary_color
        self.ids.progress1.value = 100
        self.ids.contact_icon.text_color = app.theme_cls.primary_color
        self.ids.contact_icon.icon = "check-decagram"



    def previous(self):
        self.ids.slide.load_previous()
        self.ids.name.text_color = 0, 0, 0, 1
        self.ids.progress.value = 0
        self.ids.name_icon.icon = "numeric-1-circle"
        self.ids.name_icon.text_color = 0, 0, 0, 1

    def previous1(self):
        self.ids.slide.load_previous()
        self.ids.contact.text_color = 0, 0, 0, 1
        self.ids.progress1.value = 0
        self.ids.contact_icon.icon = "numeric-2-circle"
        self.ids.contact_icon.text_color = 0, 0, 0, 1

class LoginScreen(MDScreen):
    scale_house_small = NumericProperty(1)
    lbl_h1_y = NumericProperty(50)
    lbl_login_y = NumericProperty(70)
    login_field_y = NumericProperty(90)
    login_password_y = NumericProperty(110)
    btn_login_y = NumericProperty(130)
    state = False

    def anime_house_small(self):
        anim = (
            Animation(scale_house_small = 0.8, d=0.8)
            + Animation(scale_house_small = 1, d=0.8)
        )
        anim.repeat = True
        anim.start(self)

    def anime_rest_screen(self):
        Animation(y = dp(350), d=0.8, t="in_out_cubic").start(self.ids.house_big)
        Animation(
            lbl_h1_y = 0,
            lbl_login_y = 0,
            login_field_y = 0,
            login_password_y = 0,
            btn_login_y = 0,
            d=1.2,
            t="in_out_cubic"
        ).start(self)
        Animation(opacity = 1, d=0.8).start(self.ids.lbl_h1)
        Animation(opacity = 1, d=0.8).start(self.ids.lbl_login)
        Animation(opacity = 1, d=0.8).start(self.ids.login_field)
        Animation(opacity = 1, d=0.8).start(self.ids.login_password)
        Animation(opacity = 1, d=0.8).start(self.ids.btn_login)
        Animation(opacity = 1, d=0.8).start(self.ids.lbl_register)
        self.state = True

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
    title_text = StringProperty("DMRE")

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
    prop_views = StringProperty()
    prop_auction_type = StringProperty()
    auc_color = StringProperty()

class FloatingButton(RectangularRippleBehavior, ButtonBehavior, MDFloatLayout):
    pass

# ============================ Forms ===============================
class FormButton(RectangularRippleBehavior, ButtonBehavior, MDFloatLayout):
    text = StringProperty()
    icon = StringProperty()

class PasswordField(TouchRippleBehavior, MDTextField):
    password_mode = BooleanProperty(True)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            touch.grab(self)
            self.ripple_duration_in = 0.9
            self.ripple_scale = 0.4
            self.ripple_show(touch)
            if self.icon_right:
                # icon position based on the KV code for MDTextField
                icon_x = (self.width + self.x) - (self._lbl_icon_right.texture_size[1]) - dp(8)
                icon_y = self.center[1] - self._lbl_icon_right.texture_size[1] / 2
                if self.mode == "rectangle":
                    icon_y -= dp(4)
                elif self.mode != 'fill':
                    icon_y += dp(8)

                # not a complete bounding box test, but should be sufficient
                if touch.pos[0] > icon_x and touch.pos[1] > icon_y:
                    if self.password_mode:
                        self.icon_right = 'eye'
                        self.password_mode = False
                        self.password = self.password_mode
                    else:
                        self.icon_right = 'eye-off'
                        self.password_mode = True
                        self.password = self.password_mode


                    # try to adjust cursor position
                    cursor = self.cursor
                    self.cursor = (0,0)

                    Clock.schedule_once(partial(self.set_cursor, cursor))

        return super(PasswordField, self).on_touch_down(touch)

    def on_touch_up(self, touch):
        if touch.grab_current is self:
            touch.ungrab(self)
            self.ripple_duration_out = 0.4
            self.ripple_fade()
            return True
        return False

    def set_cursor(self, pos, dt):
        self.cursor = pos

class DMRE(MDApp):
    # def build(self):
    #     return Builder.load_string(KV)
    def build(self):
        self.load_kv("main.kv")

    def on_start(self):
        print("=================================================================")
        print("=========================== starting ============================")
        print("=================================================================")

        # ====================== Initializing Database =========================
        global cur, con
        cur, con = db.db_connector()

        # ============== Check if there is any active session ==================
        with open("session.txt", "r+") as file:
            content = file.read()
            print(f"--------{content}-------")
            if content == "":
                self.root.current = "register_screen"
            else:
                print(self.root)
                self.root.current = "root_screen"
        # ======================================================================
        # ================== Get all properties on app starting ================
        if(con):
            print("True")
            self.get_app_properties(cur, con)
        else:
            print("false")

        # ======================================================================

    def call_from_nav_item(self, for_item):
        nav_item = NavigationItem()
        home_item = self.root.ids.root_screen.ids.home_item

        if(for_item == "set_all_inactive"):
            # NavigationItem.icon_color = home_item.theme_cls.disabled_hint_text_color
            pass
        else:
            NavigationItem.on_release(home_item)

    def get_app_properties(self,cur, con):
        properties_screen = self.root.ids.root_screen.ids.real_estate_items

        # check if data is json filename
        print("=============== Check if Json Cache is Empty ==============")
        with open('assets/properties/properties.json', 'r+') as file:
            content = file.read()
            if content == "":
                print("============= Cache empty, getting from DB ================")
                self.prop_data_from_db(cur, con, content, properties_screen)

            else:
                print("================ Reading from Json Cache ==================")
                properties = json.loads(content)
                properties = json.loads(properties)
                print("============ Checking for new data from DB ================")
                db_count = db.get_properties_count(cur, con)
                db_count = int(db_count)
                json_count = len(properties)
                print(f"=== db_count: {db_count} & json_count: {json_count}===")

                if db_count > json_count:
                    print("=========== Found new data, getting from db ===========")
                    self.prop_data_from_db(cur, con, content, properties_screen)
                else:
                    print("=========== No new data, display from JSON ============")
                    self.prop_data_from_json(cur, con, properties, properties_screen)

    def data_to_json(self, properties):
        # ============================ Converting Tuple to Json and saving to properties.json======================
        print("=================================================================")
        print("======================= writting to Json File ===================")
        properties_json = json.dumps(properties)
        # print(properties_json)
        with open('assets/properties/properties.json', 'w+', encoding='utf-8') as file:
            json.dump(properties_json, file)

    def write_file_bin_to_photo(self, data, filename):
        # Convert binary data to proper format and write it on Hard Disk
        with open(filename, 'wb') as file:
            file.write(data)

    def prop_data_from_db(self, cur, con, content, properties_screen):
        properties = db.get_properties(cur, con)
        if properties == "No connection, Try again later":
            properties = json.loads(content)
            properties = json.loads(properties)
            self.prop_data_from_json(cur, con, properties, properties_screen)
        else:
            properties_to_json = []
            for i in properties:
                # print(f"----{i}")
                i = list(i)
                prop_id = i[0]
                prop_title = i[1]
                prop_desc = i[2]
                prop_category = i[3]
                prop_location = i[4]
                prop_price = i[5]
                prop_dateadded = i[7]
                prop_status = i[8]
                prop_uploadedby = i[9]
                prop_auction_type = i[10]
                prop_condition = i[11]
                prop_availability = i[12]
                prop_views = i[13]

                auc_color = ""
                if(prop_auction_type == "Rent"):
                    auc_color = "#f57e71"
                else:
                    auc_color = "#71f5bc"
                # ==================================================================
                # ===================== Image Cleaning Block =======================
                # ==================================================================
                # ======= writting image blob data to file prop_{prop_id} ==========

                self.write_file_bin_to_photo(i[6], f"assets/properties/prop_{prop_id}.jpg")

                # ================ replacing image binary for json =================
                i[6] = f"assets/properties/prop_{prop_id}.jpg"
                i[7] = str(i[7])
                # ================= Assigning image to variable ====================
                prop_image = i[6]
                # ==================================================================
                properties_to_json.append(i)

                properties_screen.add_widget(
                    PropertyListItem(
                        prop_title = prop_title,
                        prop_location = prop_location,
                        prop_price = f"XAF {prop_price}",
                        prop_image = prop_image,
                        prop_auction_type = prop_auction_type,
                        prop_views = str(prop_views),
                        auc_color = auc_color
                        )
                )

            self.data_to_json(properties_to_json)

    def prop_data_from_json(self, cur, con, properties, properties_screen):
        for i in properties:
            prop_id = i[0]
            prop_title = i[1]
            prop_desc = i[2]
            prop_category = i[3]
            prop_location = i[4]
            prop_price = i[5]
            prop_image = i[6]
            prop_dateadded = i[7]
            prop_status = i[8]
            prop_uploadedby = i[9]
            prop_auction_type = i[10]
            prop_condition = i[11]
            prop_availability = i[12]
            prop_views = i[13]

            auc_color = ""
            if(prop_auction_type == "Rent"):
                auc_color = "#f57e71"
            else:
                auc_color = "#71f5bc"

            properties_screen.add_widget(
                PropertyListItem(
                    prop_title = prop_title,
                    prop_location = prop_location,
                    prop_price = f"XAF {prop_price}",
                    prop_image = prop_image,
                    prop_auction_type = prop_auction_type,
                    prop_views = str(prop_views),
                    auc_color = auc_color
                    )
            )



DMRE().run()
