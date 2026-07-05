Flask LAN File Sharing Flask README

Local Network File Sharing Hub (Flask)

A lightweight, self-hosted web application built with Flask that enables secure and fast file sharing between multiple devices within the same local area network (LAN). By running the server on all available network interfaces, users can create dynamic rooms, upload files, and download shared assets across computers, smartphones, and tablets instantly.



🚀 Features





LAN-Wide Accessibility: Run the server once and access it from any device connected to the same Wi-Fi/Ethernet network.



Dynamic Rooms: Create custom spaces (rooms) to isolate shared files.



Structured Storage: Automatically organizes uploads into subdirectory folders named after the specific room (uploads/<room-name>/).



Secure File Naming: Prevents name collisions by appending unique cryptographic tokens to uploaded files.



Easy Download/Upload: Clean routes for listing, uploading, and downloading shared files via simple HTTP requests.



📂 Directory Structure

Once files are uploaded, they are stored in the following hierarchy:

.
├── app.py                 # Main Flask Application
├── templates/
│   ├── index.html         # Homepage (Room Creation / Entry)
│   └── room.html          # Individual Room Dashboard
└── uploads/               # Main Upload Directory (Auto-generated)
    ├── room-alpha/        # Files specific to "room-alpha"
    │   └── project_a5f2e1d9.pdf
    └── room-beta/         # Files specific to "room-beta"
        └── image_b9d8c7a6.png




🛠️ Installation & Setup

1. Clone the Repository & Navigate to Directory

git clone <repository-url>
cd <repository-folder>


2. Install Dependencies

Make sure you have Python 3 installed. Install Flask and required packages:

pip install Flask Werkzeug


3. Firewall Configuration (Crucial for Local Network Access)

In order for other devices in your local network to connect to your Flask server, you must temporarily disable or configure your system's firewall:





Windows: Turn off Windows Defender Firewall for Private/Public networks, or add an inbound rule for the port you plan to run the app on (default is 5000).



macOS: Go to System Settings > Network > Firewall and turn it off, or configure it to allow incoming connections to Python.



Linux (Ubuntu/Debian): Disable UFW or allow the specific port:

sudo ufw disable

OR

sudo ufw allow 5000/tcp






🏃 Run the Application

To make the server discoverable and accessible to all devices on your local network, you must bind it to all network interfaces (0.0.0.0):

flask run --host=0.0.0.0 --port=5000


Or run it directly using python (make sure to append the host configuration block in your code if running via python app.py):

python app.py




📱 How to Access from Other Devices





Find your Local IP Address on the host machine running the Flask server:





Windows: Open Command Prompt and type ipconfig (Look for IPv4 Address, e.g., 192.168.1.15).



macOS/Linux: Open Terminal and type ifconfig or ip a (Look for inet under your active Wi-Fi or Ethernet adapter).



Connect via Browser:
On any phone, tablet, or secondary computer connected to the same Wi-Fi/LAN, open the browser and type:

http://<your-host-ip>:5000


Example: http://192.168.1.15:5000



🔒 Security Disclaimer

This application is designed strictly for trusted, private local area networks. It does not implement user authorization, access control lists (ACLs), or HTTPS by default. Anyone connected to your Wi-Fi network who knows the local IP address can access the uploaded files. Do not deploy this application publicly on the internet without wrapping it in an authentication layer and configuring SSL/TLS.
