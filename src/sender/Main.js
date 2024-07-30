import rl from 'readline-sync';
import binary_encode from './Presentation/index.js';
import hamming from './Link/Hamming.js';
import crc32 from './Link/CRC32.js';
import net from 'net';
import transmit from './Transmission/index.js';
import dotenv from 'dotenv';

async function main () {
    try {
        dotenv.config();
        const args = process.argv.slice(2);
        const algorithm = args[0];
        const ip = process.env.SOCKET_IP
        const port = process.env.SOCKET_PORT
        const generator = process.env.CRC_POLY;
        const noiseRate = process.env.NOISE_RATE;
        
        const socket = new net.Socket();

        socket.connect(port, ip, () => {
            console.log('Connecting to the server on '+ip+':'+port);
        });
        socket.on('error', (err) => {
            console.error('Error: ' + err);
        });
        
        while(true){
            let valid = true;
            const message = rl.question('Enter the message or type "EXIT" to leave: ')
            if(message === 'EXIT'){
                break;
            }
            const encodedMessage = binary_encode(message);
            console.log('Binary encoded message:', encodedMessage);

            let codes = encodedMessage.split(' ');
            codes = codes.filter(code => code.length > 0);

            let encoded = [];

            if (algorithm === "crc") {
                encoded = codes.map(code => {
                    const checksum = crc32(code, generator).toString(16);
                    return code+checksum;
                })
                console.log('Encoded codes:', encoded);

            } else if (algorithm === "hamming") {
                encoded = codes.map(code => {
                    const trimmedCode = code.replace('\r', '');
                    const bits = trimmedCode.split('').map(Number);
                    const first_half = bits.slice(0, 4);
                    const second_half = bits.slice(4, 8);
                    const first_result = hamming(first_half, 7, 4).join('')
                    const second_result = hamming(second_half, 7, 4).join('')
                    return first_result + second_result;
                });
                console.log('Encoded codes:', encoded);
            } else {
                console.log('Invalid algorithm');
                valid = false;
            }

            if(valid){
                transmit(encoded, algorithm, socket, noiseRate);
            }
            
        }
    } catch (err) {
        console.error('Error:', err);
    }
}

main();