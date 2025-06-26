# RF Control System using gRPC

This project simulates an RF control interface using gRPC. It includes both a client and a server to set RF parameters such as frequency, gain, and device ID. The backend uses mocked responses to simulate interaction with RF hardware, enabling testing without requiring actual VISA or UHD devices.

---

## 📁 Project Structure

```
rfcontrol/
│
├── proto/
│   └── rfcontrol.proto         # gRPC service and message definitions
│
├── server/
│   └── server.py               # gRPC server with mocked RF control
│
├── client/
│   └── client.py               # gRPC client with CLI input
│
├── docs/
│   └── *.html                  # Auto-generated HTML documentation (via pdoc)
│
└── README.md
```

---

## 🚀 Features

- 📡 **Set RF parameters**: frequency, gain, and device ID
- 🔁 **gRPC Client-Server architecture**
- 🧪 **Mocked hardware API** for demo/testing without physical devices
- 📚 **Auto-generated documentation** using `pdoc`

---

## ⚙️ How to Run

### 1. Install Dependencies

```bash
pip install grpcio grpcio-tools pdoc
```

### 2. Generate gRPC Code from `.proto`

```bash
python -m grpc_tools.protoc -Iproto --python_out=./proto --grpc_python_out=./proto proto/rfcontrol.proto
```

### 3. Run the Server

```bash
python server/server.py
```

### 4. Run the Client (in a separate terminal)

```bash
python client/client.py
```

---

## 📜 Example Interaction

**Client Input:**
```
Device ID: rf001
Frequency (Hz): 2.45e9
Gain (dB): 10
```

**Server Output:**
```
[Server] Received RF config:
Setting frequency to 2450000000.0 Hz and gain to 10.0 dB
```

**Client Output:**
```
Response: RF parameters set successfully. | Success: True
```

---

## 📘 Hardware Integration

This implementation does **not** require any RF hardware. All hardware-related functionality is mocked using `print()` statements to simulate configuration actions. This allows full testing and demonstration in a purely software environment.

---

## 🧾 Documentation

Documentation is auto-generated using [`pdoc`](https://pdoc.dev).

run the following command to read the documentation:

```
start docs\index.html
```

## 📄 License

This project is provided as part of an academic assignment and is intended for educational use.

---

## 🙋‍♀️ Contact

For questions, contact:\
Wasi Ahmad\
Email: wasiahmad0569@gmail.com\
Contact Number: 01797153171