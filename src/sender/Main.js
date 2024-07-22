import { promises as fs } from 'fs';
import hamming74 from './Hamming.js';

async function main () {
    try {
        const data = await fs.readFile('src/data/to_encode.txt', 'utf8');
        console.log('Reading the file...');

        const codes = data.split('\n').filter(Boolean);

        const args = process.argv.slice(2);

        const encoder = "hamming" | "crc";

        let encodedCodes;

        if (args.length > 0) {
            if (args[0] === "crc") {
                console.log('Using CRC encoder');
                //TODO: Implement CRC encoder
            } else {
                console.log('Using Hamming encoder');
                encodedCodes = codes.map(code => {
                    const bits = code.split('').map(Number);
                    return hamming74(bits).join('');
                });
            }
        }

        console.log('Encoded codes:', encodedCodes);

        await fs.writeFile('src/data/to_decode.txt', encodedCodes.join('\n'));
        console.log('File has been written');
    } catch (err) {
        console.error('Error:', err);
    }
}

main();