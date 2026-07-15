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