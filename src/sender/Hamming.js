function generateParityMatrix(m, n) {
    //generate the parity matrix
    const matrix = []
    for (let i = 0; i<m; i++) {
        const row = [];
        //generate the parity bits
        for (let j = 0; j <n; j++) {
            row.push(((j + 1) >> i) & 1);
        }
        matrix.push(row);
    }
    return matrix;
}

function calculateParityBits(dataBits, parityMatrix) {
    const parityBits = [];
    //calculate the parity bits
    for (const row of parityMatrix) {
        let parity = 0;
        //calculate the parity for each row
        for (let i = 0; i < row.length; i++) {
            parity ^= row[i] *dataBits[i]

        }
        parityBits.push(parity)
    }
    return parityBits;
}


const hamming = (dataBits, n, m) => {
    //check if the length of dataBits is correct
    if (dataBits.length !== m) {
        throw new Error(`The length of dataBits must be ${m}`);
    }

    const parityMatrix = generateParityMatrix(n-m, n);

    const parityBits = calculateParityBits(dataBits, parityMatrix)

    const hammingCode =[]
    let dataIndex = 0
    let parityIndex = 0
    //generate the hamming code
    for (let i =0; i< n; i++) {
        if (Math.pow(2, parityIndex) === i+1) {
            hammingCode[i] = parityBits[parityIndex]
            parityIndex++
        } else {
            hammingCode[i] = dataBits[dataIndex]
            dataIndex++
        }
    }

    return hammingCode
}

export default hamming