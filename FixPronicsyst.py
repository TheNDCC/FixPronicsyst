# Instrucciones de uso
# Agregar una carpeta "csv" y una carpeta "output" junto al archivo python
# Agregar el archivo csv en la carpeta csv
# Ejecutar python csv_report_fix.py
# Generará un archivo nuevo modificado en la carpeta output

import os
import re
import csv

csv_dir = "csv/"
output_dir = "static/"

files = os.listdir(csv_dir)
if not files:
    print("No se encontraron archivos CSV en el directorio.")
    exit()

for file_name in files:
    input_file_path = os.path.join(csv_dir, file_name)
    with open(input_file_path, newline="", encoding="utf-8") as csvfile:
        csv_rows = csv.reader(csvfile, delimiter=";", quotechar='"')
        output_csv = []
        first_row = False
        
        for row in csv_rows:
            row = [col.replace("<p>", "").replace("</p>", "").strip() for col in row]

            for products in row[-1].split("\n"):
                quantity = re.search(r"\((.*?)\)", products)
                products = re.sub(r"\(.*?\)", "", products).strip()
                columns = [products]

                if quantity:
                    columns.append(quantity.group(1))
                elif not first_row:
                    columns.append("Diferencia")
                    first_row = True

                output_csv.append(row[:-1] + columns)

    output_file_path = os.path.join(output_dir, file_name)
    with open(output_file_path, mode="w", newline="", encoding="utf-8") as new_file:
        writer = csv.writer(new_file)
        writer.writerows(output_csv)

    print(f"Archivo procesado y guardado en {output_file_path}")