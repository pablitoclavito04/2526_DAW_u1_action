import subprocess
import sys
from datetime import datetime

def run_tests():
    """Ejecuta tests y devuelve True/False"""
    try:
        result = subprocess.run([sys.executable, "-m", "pytest", "test_main.py"])
        return result.returncode == 0
    except:
        return False

def update_readme_history(success):
    """Añade línea con fecha/hora al historial"""
    try:
        with open("README.md", "r", encoding="utf-8") as f:
            lines = f.readlines()
        
        # Crear nueva entrada
        now = datetime.now().strftime("%d/%m/%Y %H:%M")
        new_entry = f"- {now}: {'✅ PASÓ' if success else '❌ FALLÓ'}\n"
        
        # Buscar sección de historial
        historial_index = -1
        for i, line in enumerate(lines):
            if "## Historial de Tests" in line:
                historial_index = i
                break
        
        if historial_index != -1:
            # Insertar después del título
            lines.insert(historial_index + 1, new_entry)
        else:
            # Crear nueva sección al final
            lines.append("\n## Historial de Tests\n")
            lines.append(new_entry)
        
        # Escribir archivo
        with open("README.md", "w", encoding="utf-8") as f:
            f.writelines(lines)
            
        print("Historial actualizado correctamente")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    passed = run_tests()
    update_readme_history(passed)