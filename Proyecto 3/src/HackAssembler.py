import sys

# TABLAS
dest_table = {
    None: "000", "M": "001", "D": "010", "MD": "011",
    "A": "100", "AM": "101", "AD": "110", "AMD": "111"
}

jump_table = {
    None: "000", "JGT": "001", "JEQ": "010", "JGE": "011",
    "JLT": "100", "JNE": "101", "JLE": "110", "JMP": "111"
}

comp_table = {
    "0":"0101010","1":"0111111","-1":"0111010","D":"0001100","A":"0110000",
    "!D":"0001101","!A":"0110001","-D":"0001111","-A":"0110011",
    "D+1":"0011111","A+1":"0110111","D-1":"0001110","A-1":"0110010",
    "D+A":"0000010","D-A":"0010011","A-D":"0000111",
    "D&A":"0000000","D|A":"0010101",
    "M":"1110000","!M":"1110001","-M":"1110011",
    "M+1":"1110111","M-1":"1110010",
    "D+M":"1000010","D-M":"1010011","M-D":"1000111",
    "D&M":"1000000","D|M":"1010101"
}

# VARIABLES PREDEFINIDAS
symbols = {
    "SP":0,"LCL":1,"ARG":2,"THIS":3,"THAT":4,
    "SCREEN":16384,"KBD":24576
}

# R0-R15
for i in range(16):
    symbols[f"R{i}"] = i


def clean_line(line):
    line = line.split("//")[0].strip()
    return line


def first_pass(lines):
    rom = 0
    for line in lines:
        if line.startswith("("):
            label = line[1:-1]
            symbols[label] = rom
        else:
            rom += 1


def to_binary(n):
    return format(n, '016b')


def parse_c_instruction(line):
    if "=" in line:
        dest, rest = line.split("=")
    else:
        dest = None
        rest = line

    if ";" in rest:
        comp, jump = rest.split(";")
    else:
        comp = rest
        jump = None

    return dest, comp, jump


def assemble(lines):
    output = []
    var_address = 16

    for line in lines:

        # A-INSTRUCTION
        if line.startswith("@"):
            value = line[1:]

            if value.isdigit():
                num = int(value)
            else:
                if value not in symbols:
                    symbols[value] = var_address
                    var_address += 1
                num = symbols[value]

            output.append(to_binary(num))

        # C-INSTRUCTION
        elif not line.startswith("("):
            dest, comp, jump = parse_c_instruction(line)

            comp_bits = comp_table[comp]
            dest_bits = dest_table[dest]
            jump_bits = jump_table[jump]

            output.append("111" + comp_bits + dest_bits + jump_bits)

    return output


def main():
    input_file = sys.argv[1]
    output_file = input_file.replace(".asm", ".hack")

    with open(input_file) as f:
        raw_lines = f.readlines()

    # limpiar
    lines = [clean_line(l) for l in raw_lines if clean_line(l)]

    # primera pasada (labels)
    first_pass(lines)

    # ensamblar
    result = assemble(lines)

    with open(output_file, "w") as f:
        for line in result:
            f.write(line + "\n")


if __name__ == "__main__":
    main()
