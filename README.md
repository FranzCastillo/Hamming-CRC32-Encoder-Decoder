# Hamming-CRC32-Encoder-Decoder
## Report
You can check the report and tests for this repository online [here](https://docs.google.com/document/d/1PjH5iSQwaEBs2GmQs5_6TaKgdiFgylFIi9rTl6jGY70/edit?usp=sharing).
## How to run?
### Sender
The sender end was implemented in JS. You need ``npm`` or ``yarn`` to run the sender.
#### Hamming
```bash
npm run start hamming
````
#### CRC32
```bash
npm run start crc32
```
The program will ask you to write a message that will be sent to the reciver.

### Receiver
The receiver end was implemented in Python and will be listening for any message sent.
```bash
python src/receiver/Main.py
```

### Environment variables
You will need a .env file with the following:
```
SOCKET_PORT=8080
SOCKET_IP=127.0.0.1
CRC_POLY=1001
NOISE_RATE=0.0001
```
This can be changed acording of the necesity.
