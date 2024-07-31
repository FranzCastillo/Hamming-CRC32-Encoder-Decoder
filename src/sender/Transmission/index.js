const transmit = (message, algorithm, socket, noiseRate) => {
    const noise_message = noise(message, noiseRate);
    console.log('Transmitting message:', noise_message);
    const data = {
        algorithm: algorithm,
        message: noise_message
    }
    socket.write(JSON.stringify(data));
    console.log('Message transmitted');
}

const noise = (message, noiseRate) => {
    return message.map(code => {
        return code.split('').map(bit => {
            if (Math.random() < noiseRate) {
                return bit === '0' ? '1' : '0';
            }
            return bit;
        }).join('');
    });
}

export default transmit;
