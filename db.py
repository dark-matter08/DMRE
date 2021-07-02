import mysql.connector
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton, MDFlatButton

ENV = "Development"

def show_alert_dialog( message):
    global dialog
    dialog = MDDialog(
        title = "Connecting...",
        text = message,
        pos_hint = {"center_x": .5, "center_y": .5},
        size_hint_x = .8,
        size_hint_y = .1,
        buttons=[
            MDRaisedButton(
                text="OK"
            ),
        ],
    )

    # dialog.buttons = (button)
    dialog.open()

if (ENV == "Development"):
    def db_connector():
        print("=============== Trying offline servers... ==============")
        try:
            con = mysql.connector.connect(
            user = "root",
            password = "",
            host = "localhost",
            database = "dmre"
            )
            cur = con.cursor()
            print("====================")
            print("Offline DB Connected")
            print("====================")
        except Exception as e:
            print("===================")
            print(e)
            print("===================")
            show_alert_dialog("No connection!")
            cur = ""
            con = ""
            print("===================")
            print("====== Error ======")
            print("===================")
        return cur, con
else:
    def db_connector():

        try:
            # try connecting to remote db
            pass
            print("============== Trying online servers... ===============")
            con = mysql.connector.connect(
            user = "ndelgiyy_copa",
            password = "Nixo2018",
            host = "premium154.web-hosting.com",
            port = 5522,
            database = "ndelgiyy_dmre"
            )
            cur = con.cursor()

            print("===================")
            print("Online DB Connected")
            print("===================")

        except Exception as e:
            print("===================")
            print(e)
            print("===================")
            # try connecting to local db
            # ssh key password: ~41Kt5D^XRs@
            print("=============== Trying offline servers... ==============")
            try:
                con = mysql.connector.connect(
                user = "root",
                password = "",
                host = "localhost",
                database = "dmre"
                )
                cur = con.cursor()
                print("====================")
                print("Offline DB Connected")
                print("====================")
            except Exception as e:
                print("===================")
                print(e)
                print("===================")
                show_alert_dialog("No connection!")
                cur = ""
                con = ""
                print("===================")
                print("====== Error ======")
                print("===================")


        return cur, con

def get_properties(cur, con):
    try:
        cur.execute("SELECT * FROM property WHERE status=%s",(1,))
        properties = cur.fetchall()
        # print(properties[0][1])

        return properties

    except Exception as e:
        print(e)
        return "No connection, Try again later"
        # show_alert_dialog(f"Check your Connection to the server and try again later")

def get_properties_count(cur, con):
    try:
        cur.execute("SELECT * FROM property WHERE status=%s",(1,))
        properties = cur.fetchall()
        properties_count = cur.rowcount
        # print(properties[0][1])

        return properties_count

    except Exception as e:
        print(e)
        return "No connection, Try again later"
        # show_alert_dialog(f"Check your Connection to the server and try again later")
# cur, con = db_connector()
# get_properties(cur, con)
