[Day 14 challenge](https://www.codedex.io/daily-challenge/2026-03-15)

Oh snap! Today was Julius Caesar's assasination! ...In 44 BC, that is.

A Caesar Cipher, named after Julius himself, is a simple encryption technique where each letter in a message is shifted by a fixed number of positions in the alphabet.

caesar cipher

For example, with a shift of 3:

a becomes d
b becomes e
c becomes f
...
x becomes a
y becomes b
z becomes c
You can hide all sorts of things using a Caesar Cipher! 🤯

Complete the function that decodes a message that has been encoded using a Caesar Cipher.

It should accept the scrambled message and the shift value, and return the original text.

The message include only lowercase letters and spaces.

Examples

Battle Message

- Input:
message = "dwwdfn dw gdzq"
shift = 3
- Output: "attack at dawn"
The Beatles Conspiracy Theory

- Input:
message = "ymj bfqwzx bfx ufzq"
shift = 5
- Output: "the walrus was paul"
Secret Note

- Input:
message = "ai wlsyph womt kcq gpeww"
shift = 4
- Output: "we should skip gym class"