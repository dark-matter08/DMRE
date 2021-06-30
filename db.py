import mysql.connector
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
        print(e)
        # show_alert_dialog("No connection!")
        cur = ""
        con = ""
        print("===================")
        print("====== Error ======")
        print("===================")
