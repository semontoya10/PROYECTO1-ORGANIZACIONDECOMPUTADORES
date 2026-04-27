load ALU.hdl,
output-file ALU.out,
compare-to ALU.cmp,
output-list x%B1.16.1 y%B1.16.1 zx%B2.1.2 nx%B2.1.2 zy%B2.1.2 ny%B2.1.2 f%B2.1.2 no%B2.1.2 out%B1.16.1 zr%B2.1.2 ng%B2.1.2 result%B2.1.2;

// Normal ALU addition: x=5, y=3 (5+3=8)
set x %B0000000000000101, // 5
set y %B0000000000000011, // 3
set zx 0, set nx 0, set zy 0, set ny 0, set f 1, set no 0,
eval, output;

// Normal ALU AND: x=5, y=3 (5 AND 3 = 1)
set x %B0000000000000101,
set y %B0000000000000011,
set zx 0, set nx 0, set zy 0, set ny 0, set f 0, set no 0,
eval, output;

// Shifter Left: x=0101010101010101 (0x5555) -> should be 1010101010101010 (0xAAAA), result=0
set x %B0101010101010101,
set y %B0000000000000000,
set zx 0, set nx 0, set zy 0, set ny 0, set f 0, set no 1, // no=1 activa Shifter, f=0 Izquierda
eval, output;

// Shifter Right: x=0101010101010101 (0x5555) -> should be 0010101010101010 (0x2AAA), result=1
set x %B0101010101010101,
set y %B0000000000000000,
set zx 0, set nx 0, set zy 0, set ny 0, set f 1, set no 1, // no=1 activa Shifter, f=1 Derecha
eval, output;

// Shifter Right: x=1000000000000001 -> should be 0100000000000000, result=1
set x %B1000000000000001,
set y %B0000000000000000,
set zx 0, set nx 0, set zy 0, set ny 0, set f 1, set no 1,
eval, output;
