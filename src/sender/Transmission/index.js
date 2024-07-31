import seedrandom from 'seedrandom';

const transmit = (message, algorithm, socket, noiseRate, seed) => {
    const noise_message = noise(message, noiseRate, seed);
    console.log('Transmitting message:', noise_message);
    const data = {
        algorithm: algorithm,
        message: noise_message
    };
    socket.write(JSON.stringify(data));
    console.log('Message transmitted');
}

const noise = (message, noiseRate, seed) => {
    const rng = seedrandom(seed);
    return message.map(code => {
        return code.split('').map(bit => {
            if (rng() < noiseRate) {
                return bit === '0' ? '1' : '0';
            }
            return bit;
        }).join('');
    });
}

export default transmit;
