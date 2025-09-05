# Fully functional Bitcoin-inspired blockchain in Python
This project is a from-scratch implementation of a fully functional blockchain in Python, built to explore the inner workings of Bitcoin. It includes:

🪙 Wallet functionality (key generation & management)

🔐 Elliptic Curve Cryptography (ECC) implemented from scratch for public/private keys & transaction signing

📜 Transaction validation and memory pool management

⛏️ Mining & consensus with conflict resolution between miners

🔄 Peer-to-peer networking for node communication & block propagation

⚡ Multiprocessing to utilize all CPU cores for mining and validation

⚠️ Note: ECC involves advanced math — feel free to skip that part if you’re just exploring the blockchain basics.

![image](https://user-images.githubusercontent.com/86418669/179878631-d2f3dde8-56f4-46a3-acb5-3d07183b7afa.png)


# Steps to clone and run it locally
**Make sure your python version is Python 3.10.12.**
1. git clone https://github.com/anni1236012/Blockchain-Implementation-in-Python-from-Scratch
2. cd Bitcoin 
3. pip install -r requirements.txt
4. **Windows** user search sys.path.append("/Users/Vmaha/Desktop/Bitcoin") and replace all it with your system path. 
   **On Linux machine**, make sure you copy the complete path from /home/username/Desktop/Bitcoin
5. Open VSCODE and go to blockchain.py file inside the core directory and run it. If you get any error related to config file then try to run it in debug mode. Click on run -> Start debugging. You don't have to set the breakpoint. Sometimes config.ini does not work in batch mode. Keep that in mind.
6. Goto http://127.0.0.1:5900/ and your Blockchain is up and running now.
