import os

# Rules

COMP = {
    "0": "0101010",
    "1": "0111111",
    "-1": "0111010",
    "D": "0001100",
    "A": "0110000",
    "!D": "0001101",
    "!A": "0110001",
    "-D": "0001111",
    "-A": "0110011",
    "D+1": "0011111",
    "A+1": "0110111",
    "D-1": "0001110",
    "A-1": "0110010",
    "D+A": "0000010",
    "D-A": "0010011",
    "A-D": "0000111",
    "D&A": "0000000",
    "D|A": "0010101",
    "M": "1110000",
    "!M": "1110001",
    "-M": "1110011",
    "M+1": "1110111",
    "M-1": "1110010",
    "D+M": "1000010",
    "D-M": "1010011",
    "M-D": "1000111",
    "D&M": "1000000",
    "D|M": "1010101",
}

DEST = {
    "null": "000",
    "M": "001",
    "D": "010",
    "MD": "011",
    "A": "100",
    "AM": "101",
    "AD": "110",
    "AMD": "111",
}

JMP = {
    "null": "000",
    "JGT": "001",
    "JEQ": "010",
    "JGE": "011",
    "JLT": "100",
    "JNE": "101",
    "JLE": "110",
    "JMP": "111",
}

Header = ["000", "111"]

TABLE = {
    "SP": 0,
    "LCL": 1,
    "ARG": 2,
    "THIS": 3,
    "THAT": 4,
    "COUNT": 16,
    "SCREEN": 16384,
    "KBD": 24576,
    "R0": 0,
    "R1": 1,
    "R2": 2,
    "R3": 3,
    "R4": 4,
    "R5": 5,
    "R6": 6,
    "R7": 7,
    "R8": 8,
    "R9": 9,
    "R10": 10,
    "R11": 11,
    "R12": 12,
    "R13": 13,
    "R14": 14,
    "R15": 15,
}


def parser(command):
    command = command.replace(' ', '')

    if command[0] == "@":
        label = command[1:]

        if label.isdigit():
            num = int(label)
        elif label in TABLE:
            num = TABLE[label]
        else:
            TABLE[label] = TABLE['COUNT']
            TABLE['COUNT'] += 1
            num = TABLE[label]

        ret = Header[0] + format(num, '013b')

    else:
        if ';' not in command:
            jmp_bin = JMP["null"]
        else:
            jmp_bin = JMP[command[-3:]]

        line = command.split(";")[0]

        if '=' in line:
            dst, comp = line.split("=")
            dst_bin = DEST[dst]
            comp_bin = COMP[comp]
        else:
            dst_bin = DEST["null"]
            comp_bin = COMP[line]

        ret = Header[1] + comp_bin + dst_bin +jmp_bin

    return ret


def pre(path):
    
    count = 1
    for line in open(path):
        line = line.strip()
        if line[:2] == "////": continue
        if len(line) == 0: continue
        if line[0] == "(":
            TABLE[line[1:-1]] = count
        else:
            count += 1
