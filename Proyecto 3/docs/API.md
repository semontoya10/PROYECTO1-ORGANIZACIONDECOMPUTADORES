# Hack Assembler - API Documentation

This document describes the internal functions of the `HackAssembler.py` script.

## Core Functions

### `clean_line(line)`
**Description**: Cleans a single line of assembly code.
- **Parameters**: `line` (str) - The raw line from the file.
- **Returns**: `str` - The cleaned line without comments or leading/trailing whitespace.

### `first_pass(lines)`
**Description**: Performs the first pass of the assembly process to identify labels.
- **Parameters**: `lines` (list) - List of cleaned assembly lines.
- **Side Effects**: Updates the global `symbols` dictionary with label locations.

### `to_binary(n)`
**Description**: Converts an integer to a 16-bit binary string.
- **Parameters**: `n` (int) - The number to convert.
- **Returns**: `str` - A 16-bit binary representation.

### `parse_c_instruction(line)`
**Description**: Parses a C-instruction into its three components: destination, computation, and jump.
- **Parameters**: `line` (str) - A cleaned C-instruction string.
- **Returns**: `tuple` - `(dest, comp, jump)` mnemonics.

### `assemble(lines)`
**Description**: Performs the second pass of the assembly process.
- **Parameters**: `lines` (list) - List of cleaned assembly lines.
- **Returns**: `list` - A list of 16-bit binary strings.

### `main()`
**Description**: Entry point of the script. Handles file I/O and orchestrates the assembly process.

## Global Tables

- `dest_table`: Mapping for the `dest` field.
- `comp_table`: Mapping for the `comp` field.
- `jump_table`: Mapping for the `jump` field.
- `symbols`: Predefined and dynamic symbols.
