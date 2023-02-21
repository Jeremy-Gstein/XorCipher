use std::fs::File;
use std::io::{Read, Write};

// Define the key for the XOR encryption
const XOR_KEY: u8 = 0xAA;

fn main() {
    // Open the input file for reading
    let mut input_file = File::open("input.txt").unwrap();

    // Read the contents of the file into a vector of bytes
    let mut input_data = Vec::new();
    input_file.read_to_end(&mut input_data).unwrap();

    // Perform the XOR encryption on the input data
    let encrypted_data = xor_encrypt(&input_data);

    // Open the output file for writing
    let mut output_file = File::create("output.txt").unwrap();

    // Write the encrypted data to the output file
    output_file.write_all(&encrypted_data).unwrap();
}

// Performs XOR encryption on a slice of bytes using the XOR_KEY
fn xor_encrypt(data: &[u8]) -> Vec<u8> {
    let mut encrypted_data = Vec::new();

    for byte in data {
        let encrypted_byte = byte ^ XOR_KEY;
        encrypted_data.push(encrypted_byte);
    }

    encrypted_data
}
