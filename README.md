Physical Layer
├── Bit
├── Signal
├── Link (Physical Medium)
├── Medium (Copper/Fiber/Wireless)
├── Encoder (Bits → Signal)
├── Decoder (Signal → Bits)
├── Transmitter
├── Receiver
├── Bandwidth
├── Propagation Delay
├── Transmission Delay
├── Attenuation
├── Noise
├── Port
├── Interference
├── Collision Detection
├── Half/Full Duplex
├── Clock / Synchronization
└── Error Injection

                    Physical Layer
┌──────────────────────────────────────────────────────┐
│                                                      │
│  Transmitter               Receiver                  │
│      │                        ▲                      │
│      ▼                        │                      │
│   Encoder                  Decoder                  │
│      │                        ▲                      │
│      ▼                        │                      │
│              Physical Ports                         │
│                                                      │
│  Port 0      Port 1      Port 2      Port n         │
└────┬──────────┬───────────┬───────────┬──────────────┘
     │          │           │
     ▼          ▼           ▼
   Link AB    Link AC     Link AD
     │          │           │
     ▼          ▼           ▼
 Copper      Fiber      Wireless

Data Link Layer
├── Frame
├── MAC Address
├── Frame Builder
├── Frame Parser
├── Framing
├── Error Detection (Parity → Checksum → CRC)
├── Flow Control
├── ARQ
├── MAC Protocols
├── Switching Support
└── LLC Interface

data_link_layer/
│
├── frame.py
├── mac_address.py
├── frame_builder.py
├── frame_parser.py
├── data_link_layer.py
├── frame_type.py
└── constants.py


DataLinkLayer/
│
├── framing/
│   ├── bit_stuffing.py
│   └── byte_stuffing.py
│
├── error_detection/
│   ├── parity.py
│   ├── checksum.py
│   └── crc.py
│
├── error_control/
│   ├── stop_and_wait.py
│   ├── go_back_n.py
│   └── selective_repeat.py
│
├── flow_control/
│   ├── stop_and_wait.py
│   └── sliding_window.py
│
└── data_link_layer.py