#https://github.com/spiritofthenight
import tkinter as tk
import threading
import socket
import sounddevice
import numpy as np
import time

running = False

def start_stream():
    global running
    if running:
        log("Receiver already running")
        return

    ip = entry1.get().strip()
    port = entry2.get().strip()

    if not ip or not port:
        log("Please enter IP and Port first")
        return

    try:
        port = int(port)
    except ValueError:
        log("Port must be a number")
        return

    running = True
    start_btn.config(state="disabled")
    stop_btn.config(state="normal")
    log(f"Receiver started on {ip}:{port}")

    thread = threading.Thread(target=receiver_thread, args=(ip, port), daemon=True)
    thread.start()


def stop_stream():
    global running
    running = False
    log("Stopping receiver...")

    start_btn.config(state="normal")
    stop_btn.config(state="disabled")


def log(msg):
    text_area.insert("end", msg + "\n")
    text_area.see("end")


def clear_log():
    text_area.delete("1.0", "end")


def receiver_thread(ip, port):
    global running

    UDP_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    UDP_socket.bind((ip, port))

    samplerate = 48000
    stream = sounddevice.OutputStream(samplerate=samplerate, channels=1, dtype='float32')
    stream.start()

    count_down = 1800

    log("Waiting for audio...")

    while running:
        try:
            data, addr = UDP_socket.recvfrom(4096)

            pcm16 = np.frombuffer(data, dtype=np.int16)
            audio = pcm16.astype(np.float32) / 32767

            stream.write(audio)

            log(f"Received {len(data)} bytes\n*** STREAMING ***\naudio is: \n{audio}\n")

            count_down -= 1
            if count_down <= 0:
                clear_log()
                count_down = 1800

        except Exception as e:
            log(f"Error: {e}")
            break

    stream.stop()
    stream.close()
    UDP_socket.close()
    log("Receiver stopped")


# gui 

root = tk.Tk()
root.geometry("720x380")
root.title("Audio Receiver")
root.configure(bg="grey")

top_frame = tk.Frame(root, bg="grey")
top_frame.grid(row=0, column=0, sticky="ew", padx=6, pady=6)

tk.Label(top_frame, text="IP of this computer:", bg="grey").grid(row=0, column=0, sticky="w")
entry1 = tk.Entry(top_frame, width=22, fg="green")
entry1.insert(0, "127.0.0.1")
entry1.grid(row=0, column=1, padx=5)

tk.Label(top_frame, text="Bind Port:", bg="grey").grid(row=0, column=2, sticky="w")
entry2 = tk.Entry(top_frame, width=10, fg="green")
entry2.insert(0, "5000")
entry2.grid(row=0, column=3, padx=5)

start_btn = tk.Button(top_frame, text="Start Receiver", bg="lightgreen", width=10, command=start_stream)
start_btn.grid(row=0, column=4, padx=5)

stop_btn = tk.Button(top_frame, text="Stop", bg="tomato", width=10, command=stop_stream, state="disabled")
stop_btn.grid(row=0, column=5, padx=5)

bottom_frame = tk.Frame(root, bg="grey")
bottom_frame.grid(row=1, column=0, sticky="nsew", padx=6, pady=(0,6))

root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

text_area = tk.Text(bottom_frame, height=10, font=("Arial", 8, "bold"), bg="black", fg="lightgreen")
text_area.pack(side="left", fill="both", expand=True)

scroll = tk.Scrollbar(bottom_frame, command=text_area.yview)
scroll.pack(side="right", fill="y")
text_area.config(yscrollcommand=scroll.set)
root.resizable(True, True)


root.mainloop()
