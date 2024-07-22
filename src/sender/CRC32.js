function crc32(data, generator) {
    let paddedData = data + '0'.repeat(generator.length - 1);
    let dataArray = paddedData.split('').map(Number);
    let generatorArray = generator.split('').map(Number);

    // XOR operation
    for (let i = 0; i <= dataArray.length - generatorArray.length; ) {
        for (let j = 0; j < generatorArray.length; j++) {
            dataArray[i + j] ^= generatorArray[j];
        }
        while (i < dataArray.length && dataArray[i] !== 1) {
            i++;
        }
    }
    
    // Return the remainder
    return dataArray.slice(-generatorArray.length + 1).join('');
}

export default crc32;