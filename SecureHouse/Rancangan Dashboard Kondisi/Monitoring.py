from tkinter import *
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("/indobot/p/temp")
    client.subscribe("/indobot/p/hum")
    client.subscribe("/indobot/p/distance")
    client.subscribe("/indobot/p/motion")
    client.subscribe("/indobot/p/buzzer_status")

def on_message(client, userdata, msg):
    if msg.topic == "/indobot/p/temp":
        update_temp_label(msg.payload.decode())
    elif msg.topic == "/indobot/p/hum":
        update_hum_label(msg.payload.decode())
    elif msg.topic == "/indobot/p/distance":
        update_distance_label(msg.payload.decode())
    elif msg.topic == "/indobot/p/motion":
        update_motion_label(msg.payload.decode())
    elif msg.topic == "/indobot/p/buzzer_status":
        update_buzzer_status_label(msg.payload.decode())

def update_temp_label(temp):
    temp_label.config(text=temp + " °C")

def update_hum_label(hum):
    hum_label.config(text=hum + " %")

def update_distance_label(distance):
    distance_label.config(text=distance + " cm")

def update_motion_label(motion):
    motion_label.config(text=motion)

def update_buzzer_status_label(status):
    buzzer_status_label.config(text=status)

# Create the main window
window = Tk()
window.title("MQTT Dashboard")
window.geometry('1100x600')
window.resizable(False, False)
window.configure(bg="white")

# Load the header image
canvas = Canvas(window, width=3000, height=3000)
canvas.place(x=0, y=0)
img = PhotoImage(file="dashboard.png")
canvas.create_image(0, 0, anchor=NW, image=img)

# Create labels for temperature, humidity, distance, motion, and buzzer status
temp_label = Label(window, text="", font=('Helvetica', 18), bg="white")
temp_label.place(x=435, y=185, anchor=CENTER)

hum_label = Label(window, text="", font=('Helvetica', 18), bg="white")
hum_label.place(x=780, y=185, anchor=CENTER)

distance_label = Label(window, text="", font=('Helvetica', 18), bg="white")
distance_label.place(x=775, y=390, anchor=CENTER)

motion_label = Label(window, text="", font=('Helvetica', 18), bg="white")
motion_label.place(x=435, y=390, anchor=CENTER)

buzzer_status_label = Label(window, text="", font=('Helvetica', 18), bg="white")
buzzer_status_label.place(x=135, y=300, anchor=CENTER)

# MQTT connection setup
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("0.tcp.ap.ngrok.io", 14094, 60)
client.loop_start()

# Start the Tkinter main loop
window.mainloop()





# from tkinter import *
# import paho.mqtt.client as mqtt
# import sqlite3

# # Fungsi untuk membuat tabel jika belum ada
# def create_table():
#     conn = sqlite3.connect('sensor_data.db')
#     cursor = conn.cursor()
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS sensor_data (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             temperature REAL,
#             humidity REAL,
#             distance REAL,
#             motion TEXT,
#             buzzer_status TEXT
#         )
#     ''')
#     conn.commit()
#     conn.close()

# # Fungsi untuk menyimpan data ke dalam database
# def save_to_database(temp, hum, distance, motion, buzzer_status):
#     conn = sqlite3.connect('sensor_data.db')
#     cursor = conn.cursor()
#     cursor.execute('''
#         INSERT INTO sensor_data (temperature, humidity, distance, motion, buzzer_status)
#         VALUES (?, ?, ?, ?, ?)
#     ''', (temp, hum, distance, motion, buzzer_status))
#     conn.commit()
#     conn.close()

# # Fungsi yang dipanggil setiap kali mendapat pesan MQTT
# def on_message(client, userdata, msg):
#     if msg.topic == "/indobot/p/temp":
#         update_temp_label(msg.payload.decode())
#         # Simpan data ke dalam database
#         save_to_database(float(msg.payload.decode()), None, None, None, None)
#     elif msg.topic == "/indobot/p/hum":
#         update_hum_label(msg.payload.decode())
#         # Simpan data ke dalam database
#         save_to_database(None, float(msg.payload.decode()), None, None, None)
#     elif msg.topic == "/indobot/p/distance":
#         update_distance_label(msg.payload.decode())
#         # Simpan data ke dalam database
#         save_to_database(None, None, float(msg.payload.decode()), None, None)
#     elif msg.topic == "/indobot/p/motion":
#         update_motion_label(msg.payload.decode())
#         # Simpan data ke dalam database
#         save_to_database(None, None, None, msg.payload.decode(), None)
#     elif msg.topic == "/indobot/p/buzzer_status":
#         update_buzzer_status_label(msg.payload.decode())
#         # Simpan data ke dalam database
#         save_to_database(None, None, None, None, msg.payload.decode())

# def on_connect(client, userdata, flags, rc):
#     print("Connected with result code "+str(rc))
#     client.subscribe("/indobot/p/temp")
#     client.subscribe("/indobot/p/hum")
#     client.subscribe("/indobot/p/distance")
#     client.subscribe("/indobot/p/motion")
#     client.subscribe("/indobot/p/buzzer_status")

# def update_temp_label(temp):
#     temp_label.config(text=temp + " °C")

# def update_hum_label(hum):
#     hum_label.config(text=hum + " %")

# def update_distance_label(distance):
#     distance_label.config(text=distance + " cm")

# def update_motion_label(motion):
#     motion_label.config(text=motion)

# def update_buzzer_status_label(status):
#     buzzer_status_label.config(text=status)

# # Create the main window
# window = Tk()
# window.title("MQTT Dashboard")
# window.geometry('1100x600')
# window.resizable(False, False)
# window.configure(bg="white")

# # Load the header image
# canvas = Canvas(window, width=3000, height=3000)
# canvas.place(x=0, y=0)
# img = PhotoImage(file="dashboard.png")
# canvas.create_image(0, 0, anchor=NW, image=img)

# # Create labels for temperature, humidity, distance, motion, and buzzer status
# temp_label = Label(window, text="", font=('Helvetica', 18), bg="white")
# temp_label.place(x=435, y=185, anchor=CENTER)

# hum_label = Label(window, text="", font=('Helvetica', 18), bg="white")
# hum_label.place(x=780, y=185, anchor=CENTER)

# distance_label = Label(window, text="", font=('Helvetica', 18), bg="white")
# distance_label.place(x=775, y=390, anchor=CENTER)

# motion_label = Label(window, text="", font=('Helvetica', 18), bg="white")
# motion_label.place(x=435, y=390, anchor=CENTER)

# buzzer_status_label = Label(window, text="", font=('Helvetica', 18), bg="white")
# buzzer_status_label.place(x=135, y=300, anchor=CENTER)

# # MQTT connection setup
# client = mqtt.Client()
# client.on_connect = on_connect
# client.on_message = on_message
# client.connect("0.tcp.ap.ngrok.io", 15408, 60)
# client.loop_start()

# # Start the Tkinter main loop
# window.mainloop()
