# LPRS1 Disasembler

Ovaj projekat predstavlja disasembler za **LPRS1 asembler**, napisan od strane kolega sa odsjeka za RT-RK, koji je korišten na istoimenom predmetu na 4. semestru studijskog programa Računarstvo i automatika na Fakultetu tehničkih nauka u Novom Sadu.

# Biblioteke

Projekat je napisan u Pythonu 3 i ne zavisi ni od jedne spoljne biblioteke.

# Upotreba

### MacOS/Linux

Prvo je potrebno dodijeliti datoteci <code>lprs1disassembler.py</code> dozvolu za izvršavanje pomoću komande:<br>
```bash
chmod +x lprs1disassembler.py
```

A zatim ga je moguće pokrenuti:<br>
```bash
./lprs1disassembler.py example/instr_rom.vhdl
```

### Windows
Disasembler se na Windowsu pokreće kao i svaki drugi Python program:<br>
```bash
python lprs1disassembler.py example/instr_rom.vhdl
```

## Ulazna datoteka

Disassembler na ulazu očekuje putanju ka kompletnoj <code>instr_rom.vhdl</code> datoteci koju LPRS1 assembler popunjava instrukcijama tokom asembliranja.

## Data ROM datoteka (opciono)

Moguće je priložiti i <code>data_ram.vhdl</code> datoteku pomoću koje disasembler popunjava <code>.data</code> sekciju izlazne datoteke. Putanju ka <code>data_ram.vhdl</code> datoteci treba priložiti pomoću opcija <code>-drf</code> ili <code>--data-ram-file</code>.

Disasembler nije u mogućnosti da sazna u kojem zapisu (da li u decimalnom ili heksadecimalnom) su vrijednosti iz <code>.data</code> sekcije bile zadane u originalnom kodu, pa zbog toga sve vrijednosti predstavlja u decimalnom zapisu.

## Izlazna datoteka (opciono)
Disasembler će generisanu datoteku smjestiti u folder <code>out</code>. Podrazumijevani naziv izlazne datoteke je <code>disassembled.asm</code>, ali ga je moguće prilagoditi tako što se proslijedi dodatni argument, pomoću opcije <code>-o</code> ili <code>--output</code>, koji predstavlja željeni naziv izlazne datoteke.

### MacOS/Linux
```bash
./lprs1disassembler.py example/instr_rom.vhdl -o output.asm
```

### Windows
```bash
python lprs1disassembler.py example/instr_rom.vhdl -o output.asm
```

# Kontakt

Autor ovog projekta je **Andrej Vujić**, student 2. godine studijskog programa Računarstvo i automatika.
