import subprocess
import os

def test_assembler():
    # Caminos relativos
    assembler_path = os.path.join("..", "src", "HackAssembler.py")
    test_file = "Add.asm"
    
    # Crear un archivo de prueba simple
    with open(test_file, "w") as f:
        f.write("@2\nD=A\n@3\nD=D+A\n@0\nM=D\n")
    
    # Ejecutar el ensamblador
    print(f"Running assembler on {test_file}...")
    subprocess.run(["python", assembler_path, test_file])
    
    # Verificar si el archivo .hack fue creado
    hack_file = "Add.hack"
    if os.path.exists(hack_file):
        print(f"SUCCESS: {hack_file} generated.")
        with open(hack_file, "r") as f:
            print("Output content:")
            print(f.read())
    else:
        print(f"FAILED: {hack_file} not generated.")

if __name__ == "__main__":
    test_assembler()
