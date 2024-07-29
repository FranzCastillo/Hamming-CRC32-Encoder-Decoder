function generateParityMatrix(m, n) {
    // generate the parity matrix
    const matrix = []
    for (let i = 0; i < m; i++) {
        const row = [];
        // generate the parity bits
        for (let j = 0; j < n; j++) {
            row.push(((j + 1) >> i) & 1);
        }

        matrix.push(row);
    }
    return matrix;
}

function calculateParityBits(dataBits, parityMatrix, n) {
    const parityBits = [];
    // calculate the parity bits
    for (const row of parityMatrix) {
        let sum = 0;
        // calculate the parity for each row
        for (let i = 0; i < row.length; i++) {
            if (row[i] === 1) {
                sum += dataBits[n-1-i];
            }
        }
        if (sum % 2 === 0) {
            parityBits.push(0);
        } else {
            parityBits.push(1);
        }
    }
    return parityBits;
}

const hamming = (dataBits, n, m) => {
    // check if the length of dataBits is correct
    if (dataBits.length !== m) {
        throw new Error(`The length of dataBits must be ${m}`);
    }

    const parityMatrix = generateParityMatrix(n - m, n);

    // Initialize fullBits array with undefined values
    const fullBits = Array(n).fill(undefined);
    let pointerIndex = n-1;
    let dataIndex = dataBits.length - 1;

    // Insert data bits in their positions, skipping parity bit positions
    for (let i = 0; i < n; i++) {
        if (Math.pow(2, Math.floor(Math.log2(i + 1))) === i + 1) {
            fullBits[pointerIndex] = 0; // Temporary placeholder for parity bits
        } else {
            fullBits[pointerIndex] = dataBits[dataIndex];
            dataIndex--;
        }
        pointerIndex--;
    }
    // Calculate parity bits
    const parityBits = calculateParityBits(fullBits, parityMatrix, n);
    // Insert calculated parity bits into their correct positions
    let parityIndex = 0;
    let parityPointer = n-1;

    for (let i = 0; i < n; i++) {
        if (Math.pow(2, Math.floor(Math.log2(i + 1))) === i + 1) {
            fullBits[parityPointer] = parityBits[parityIndex];
            parityIndex++;
        }
        parityPointer--;
    }

    return fullBits;
}

export default hamming