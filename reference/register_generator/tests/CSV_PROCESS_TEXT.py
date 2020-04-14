import os
from CSV_PROCESS import CSV_PROCESS

csv_process=CSV_PROCESS()
csv_process.csv_processing(r'C:\Users\x\Desktop\register_generator\csv\csv_text.csv')
csv_process.display()
csv_process.write_csv(r'C:\Users\x\Desktop\register_generator\csv1\csv_text.csv')
