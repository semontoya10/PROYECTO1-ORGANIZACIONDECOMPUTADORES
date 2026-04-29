import sys
import os


DEST = {
    "000": "",
    "001": "M",
    "010": "D",
    "011": "MD",
    "100": "A",
    "101": "AM",
    "110": "AD",
    "111": "AMD"
}

JUMP = {
    "000": "",
    "001": "JGT",
    "010": "JEQ",
    "011": "JGE",
    "100": "JLT",
    "101": "JNE",
    "110": "JLE",
    "111": "JMP"
}

COMP = {
    "0101010":"0",
    "0111111":"1",
    "0111010":"-1",
    "0001100":"D",
    "0110000":"A",
    "1110000":"M",
    "0001101":"!D",
    "0110001":"!A",
    "1110001":"!M",
    "0001111":"-D",
    "0110011":"-A",
    "1110011":"-M",
    "0011111":"D+1",
    "0110111":"A+1",
    "1110111":"M+1",
    "0001110":"D-1",
    "0110010":"A-1",
    "1110010":"M-1",
    "0000010":"D+A",
    "1000010":"D+M",
    "0010011":"D-A",
    "1010011":"D-M",
    "0000111":"A-D",
    "1000111":"M-D",
    "0000000":"D&A",
    "1000000":"D&M",
    "0010101":"D|A",
    "1010101":"D|M"
}


class HackDisassembler:

    def __init__(self, filename):
        self.filename = filename

    def decode_line(self, line):

        if len(line) != 16 or any(c not in "01" for c in line):
            raise ValueError("Línea inválida")

        if line[0] == "0":
            value = int(line[1:], 2)
            return f"@{value}"

        elif line[:3] == "111":
            comp_bits = line[3:10]
            dest_bits = line[10:13]
            jump_bits = line[13:16]

            comp = COMP.get(comp_bits)
            dest = DEST.get(dest_bits)
            jump = JUMP.get(jump_bits)

            if comp is None:
                raise ValueError("Comp inválido")

            instruction = ""

            if dest:
                instruction += dest + "="

            instruction += comp

            if jump:
                instruction += ";" + jump

            return instruction

        else:
            raise ValueError("Instrucción inválida")

    def disassemble(self):

        output = self.filename.replace(".hack", "Dis.asm")

        with open(self.filename, "r") as infile, open(output, "w") as outfile:

            for line_num, line in enumerate(infile, 1):
                line = line.strip()

                if not line:
                    continue

                try:
                    asm = self.decode_line(line)
                    outfile.write(asm + "\n")
                except Exception:
                    print(f"Error en línea {line_num}")
                    return


if __name__ == "__main__":

    if len(sys.argv) != 3 or sys.argv[1] != "-d":
        print("Uso: python HackAssembler.py -d archivo.hack")
        sys.exit(1)

    disassembler = HackDisassembler(sys.argv[2])
    disassembler.disassemble()
