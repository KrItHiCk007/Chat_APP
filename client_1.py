import customtkinter
import tkinter as tk
from tkinter import messagebox
import socket
import threading

# Set Theme
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# Create Window
root = customtkinter.CTk()
root.title("Client Chat")
root.geometry("600x700")

ip = "127.0.0.1"
port = 5000

# Create Client Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))

# Function to Listen for Incoming Messages
def receive_messages():
    while True:
        try:
            response = s.recv(1024).decode()
            if not response:
                break
            chat_box.insert(tk.END, f"\nServer: {response}")
            chat_box.see(tk.END)
        except:
            chat_box.insert(tk.END, "\nConnection Lost.")
            break

# Start Listening Thread
threading.Thread(target=receive_messages, daemon=True).start()

# Send Message to Server
def send_message():
    sender_message = message_entry.get().strip()
    if sender_message == "":
        messagebox.showwarning("Warning", "Please enter a message!")
        return

    s.send(sender_message.encode())  # Send message to server

    # Display Sent Message
    chat_box.insert(tk.END, f"\nYou: {sender_message}")
    chat_box.see(tk.END)
    message_entry.delete(0, tk.END)  # Clear input field after sending

# Main Frame
main_frame = customtkinter.CTkFrame(master=root, width=580, height=590, fg_color="#b2babb", corner_radius=20)
main_frame.grid(row=0, column=0, padx=10, pady=10)

# Chat Box (for displaying messages)
chat_box = customtkinter.CTkTextbox(
    master=main_frame, width=560, height=560, font=("Arial", 16, "bold"),
    text_color="white", corner_radius=10, wrap="word", scrollbar_button_color="gray"
)
chat_box.grid(row=0, column=0, padx=10, pady=10)

# Message Frame
message_frame = customtkinter.CTkFrame(master=root, width=560, height=50, corner_radius=20, fg_color="#d0d3d4")
message_frame.grid(row=1, column=0, padx=10, pady=10)

# Message Entry Field
message_entry = customtkinter.CTkEntry(
    master=message_frame, width=400, height=30, border_width=1, border_color="white",
    font=("Arial", 16, "bold"), placeholder_text="Enter The Message . . . ", corner_radius=20
)
message_entry.place(relx=0.4, rely=0.5, anchor='center')

# Send Button
send_button = customtkinter.CTkButton(
    master=message_frame, text_color="white", text="SEND", font=("Arial", 16, "bold"),
    border_width=1, border_color="white", fg_color="green", width=100, height=30, corner_radius=10,
    command=send_message
)
send_button.place(relx=0.9, rely=0.5, anchor="center")

# Run the App
root.mainloop()
