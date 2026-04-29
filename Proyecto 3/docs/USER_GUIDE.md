# Hack Assembler - User Guide

## Introduction
This script translates Hack Assembly language code into binary machine code that can be run on the Hack Computer.

## Prerequisites
- Python 3.x installed on your system.

## Usage

To use the assembler, run the following command in your terminal:

```bash
python HackAssembler.py <input_file.asm>
```

### Example
If you have a file named `Add.asm`, run:

```bash
python HackAssembler.py Add.asm
```

This will generate a file named `Add.hack` in the same directory.

## File Structure
- **Input**: `.asm` files containing symbolic Hack instructions.
- **Output**: `.hack` files containing 16-bit binary instructions.

## Error Handling
The assembler currently assumes the input assembly code is syntactically correct. Ensure there are no typos in mnemonics or symbol names.
