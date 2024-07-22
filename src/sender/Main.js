import { promises as fs } from 'fs';
import hamming74 from './Hamming.js';
import crc32 from './CRC32.js';

async function main () {
    try {
        const data = await fs.readFile('src/data/to_encode.txt', 'utf8');
        console.log('Reading the file...');

        const codes = data.split('\n').filter(Boolean);

        const args = process.argv.slice(2);

        let encodedCodes;

        if (args.length > 0) {
            if (args[0] === "crc") {
                console.log('Using CRC encoder');
                if (args.length < 2) {
                    throw new Error('Generator polynomial is not provided, use: yarn start crc <generator>');
                }
                const generator = args[1];
                encodedCodes = codes.map(code => {
                    return crc32(code, generator).toString(16);
                });
                
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