
const hamming74 = (bits) => {
    const p1 = bits[0] ^ bits[1] ^ bits[3];
    const p2 = bits[0] ^ bits[2] ^ bits[3];
    const p3 = bits[1] ^ bits[2] ^ bits[3];

    return [p1, p2, bits[0], p3, bits[1], bits[2], bits[3]];
}

export default hamming74;
