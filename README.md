# Hamming-CRC32-Encoder-Decoder
## Report
You can check the report and tests for this repository online [here](https://docs.google.com/document/d/1suE6GTUsWVVAKPhyM6-UCBvslsPxMMcaSF4wiAJZ4AE/edit?usp=sharing).
## How to run?
### Sender
The sender end was implemented in JS. You need ``npm`` or ``yarn`` to run the sender.
#### Hamming(N,M)
```bash
npm run start hamming <N> <M>
````
#### CRC32
```bash
npm run start crc32 <POLYNOMIAL>
```
### Receiver
The receiver end was implemented in Python.
#### Hamming(N,M)
```bash
python src/receiver/Main.py HAMMING --n=<N> --m=<M>
```
#### CRC32
```bash
python src/receiver/Main.py CRC32 --generator=<POLYNOMIAL>
```

