# Chat_APP

# 🔹 Multi-Client Chat Application (Python + CustomTkinter)

This is a **real-time chat application** built using **Python, sockets, and CustomTkinter**.  
It allows multiple clients to connect to a **central server** and communicate with each other.

---

## 📌 Features
✔ **Multi-client support** (Server can handle multiple clients).  
✔ **Graphical User Interface (GUI)** with `customtkinter`.  
✔ **Real-time messaging** with auto-scrolling chat window.  
✔ **Broadcasting** (Messages are shared among all clients).  
✔ **Handles disconnections** gracefully.  
✔ **Non-blocking GUI** (Runs server and receiving messages in background threads).  

---

## 🛠️ Technologies Used
- **Python** (Socket Programming)
- **CustomTkinter** (For GUI)
- **Threading** (For handling multiple clients)
- **Tkinter** (For popups and GUI elements)

---
### **1️⃣ Start the Server**
Run the following command:
```bash
python server.py
2️⃣ Start Multiple Clients
python client.py
📂 File Structure
📂 Chat-App
│── 📜 server.py       # Server script (Handles clients)
│── 📜 client.py       # Client script (Connects to server)
│── 📜 README.md       # Project documentation
│── 📜 requirements.txt # Required dependencies
