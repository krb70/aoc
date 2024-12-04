
import re
from pathlib import Path

txt = Path('d3.txt').read_text()

prodsum = lambda x: sum((int(m.group(1))*int(m.group(2))) for m in re.finditer(r"(?msi)mul\((\d{1,3}),(\d{1,3})\)", x))
print(prodsum(txt))

txt = re.sub(r"(?msi)don't\(\)(.*?)do\(\)", "", 'do()' + txt + 'do()')
print(prodsum(txt))
