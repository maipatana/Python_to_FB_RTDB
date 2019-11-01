import tkinter as tk
import time  # For rest

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('./ใส่ชื่อ Credential ของเรา.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'ใส่ url ของ Database ของเรา'
})

ref = db.reference('coordinates')

root = tk.Tk()

root.title('Touch to FB')
root.geometry('600x400')
#root.wm_attributes('-fullscreen','true')

def motion(event):
    x, y = event.x, event.y
    ref.push({
    'x': x,
    'y': y
    })
    print('{}, {}'.format(x, y))
    time.sleep(1)

root.bind('<Motion>', motion)
root.mainloop()

