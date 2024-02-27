import random
import csv
from datetime import datetime, timedelta

# Fungsi untuk menghasilkan data acak
def generate_data():
    # Pilih well secara acak antara 'a' dan 'b'
    well = random.choice(['a', 'b'])
    
    # Generate tanggal secara acak antara 2020-2024
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2024, 12, 31)
    date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    
    # Pilih produksi minyak secara acak antara 0 dan 100
    prod_oil = random.randint(0, 100)
    
    return {'well': well, 'date': date.strftime('%d-%m-%Y'), 'prod_oil': prod_oil}

# Inisialisasi jumlah data yang ingin dibuat
num_data = 1000

# Generate data dan simpan ke dalam list
data = [generate_data() for _ in range(num_data)]

# Simpan data ke dalam file CSV
with open('data.csv', mode='w', newline='') as file:
    fieldnames = ['well', 'date', 'prod_oil']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    for row in data:
        writer.writerow(row)