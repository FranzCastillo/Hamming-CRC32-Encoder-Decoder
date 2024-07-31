const binary_encode = (message) => {
    const binaryMessage = message.split('').map(char => {
        const binary = char.charCodeAt(0).toString(2);
        return binary.padStart(8, '0') + ' ';
    }).join('');
    return binaryMessage;
}

export default binary_encode;
