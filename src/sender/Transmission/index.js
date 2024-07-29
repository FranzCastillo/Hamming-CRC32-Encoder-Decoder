const transmit = (message, algorithm, websocket) => {
    const noise_message = noise(message);
    console.log('Transmitting message:', noise_message);
    const data = {
        algorithm: algorithm,
        message: noise_message
    }
    websocket.send(JSON.stringify(data));
    console.log('Message transmitted');
}

const noise = (message) => {
    const noise_rate = 1/100; // 1 in 100 bits will be flipped
    const noise_message = message.map(code => {
        const noise_code = code.split('').map(bit => {
            if (Math.random() < noise_rate) {
                return bit === '0' ? '1' : '0';
            }
            return bit;
        }).join('');
        return noise_code;
    });
    return noise_message;
}

export default transmit;