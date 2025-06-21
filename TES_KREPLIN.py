import random
from fpdf import FPDF

def generate_line():
    numbers = [str(random.randint(0, 9)) for _ in range(25)]
    line = ""
    for i, num in enumerate(numbers):
       line += num
       if (i + 1) % 5 == 0:
           line += '     ' # jumblah spasi per 5 angka
       else:
           line += '  ' # jumblah spasi per 1 angka
    return line.rstrip()

pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_font("Courier", size=10)

pdf.cell(0, 10, "Tes kreplin", ln=True, align="C")
pdf.ln(10)

for _ in range(50):
   line = generate_line()
   print(line)
   pdf.cell(0, 6, txt=line, ln=True)

pdf.output("tes_kreplin.pdf")

print("\nOutput berhasil ke 'tes_kreplin.pdf'")
