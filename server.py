import socket
import threading
import customtkinter
import tkinter as tk

# Set Theme
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# Create Window
root = customtkinter.CTk()
root.title("Server Chat")
root.geometry("600x700")

ip = "127.0.0.1"
port = 5000

# Create Server Socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip, port))
server.listen(5)  # Allow multiple connections

clients = []  # Store connected clients

# Broadcast Message to All Clients
def broadcast(message, sender_socket=None):
    for client in clients:
        if client != sender_socket:  # Don't send message back to sender
            try:
                client.send(message.encode())
            except:
                clients.remove(client)

# Handle Each Client in a Separate Thread
def handle_client(client_socket, address):
    chat_box.insert(tk.END, f"\nClient Connected: {address}")
    clients.append(client_socket)

    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            chat_box.insert(tk.END, f"\nClient {address}: {message}")
            chat_box.see(tk.END)
            broadcast(f"Client {address}: {message}", client_socket)  # Send to all clients
        except:
            break

    chat_box.insert(tk.END, f"\nClient {address} Disconnected.")
    clients.remove(client_socket)
    client_socket.close()

# Accept Clients in a New Thread
def accept_clients():
    while True:
        client_socket, client_address = server.accept()
        threading.Thread(target=handle_client, args=(client_socket, client_address), daemon=True).start()

# Start Accepting Clients
threading.Thread(target=accept_clients, daemon=True).start()

# Function for Sending Messages from Server
def send_message():
    server_message = message_entry.get().strip()
    if server_message == "":
        return

    chat_box.insert(tk.END, f"\nServer: {server_message}")
    chat_box.see(tk.END)
    broadcast(f"Server: {server_message}")  # Send message to all clients
    message_entry.delete(0, tk.END)  # Clear input field

# GUI Setup
main_frame = customtkinter.CTkFrame(master=root, width=580, height=590, fg_color="#b2babb", corner_radius=20)
main_frame.grid(row=0, column=0, padx=10, pady=10)

chat_box = customtkinter.CTkTextbox(
    master=main_frame, width=560, height=560, font=("Arial", 16, "bold"),
    text_color="white", corner_radius=10, wrap="word", scrollbar_button_color="gray"
)
chat_box.grid(row=0, column=0, padx=10, pady=10)

message_frame = customtkinter.CTkFrame(master=root, width=560, height=50, corner_radius=20, fg_color="#d0d3d4")
message_frame.grid(row=1, column=0, padx=10, pady=10)

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

root.mainloop()
