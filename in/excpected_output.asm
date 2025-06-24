// Ovo je primjer je zadatak sa laboratorijske vježbe broj 10,
// sa predmeta Logičko projektovanje računarskih sistema 1.
// Autor: Andrej Vujić (RA130/2023)

.data
0x1A // Rezultat
0x20 // Status flag da je program zavrsen (na kraju upisati 1)
5 // N (broj elemenata niza)
-1
-2
-3
-4
6

// REGISTRI
// R0 - broj elemenata u nizu
// R1 - cuva stepen dvojke
// R2 - brojac
// R3 - trenutni element
// R4 - suma
// R5 - adresa pocetka niza

.text
begin:
	inc R0, R0
	inc R0, R0
	ld R0, R0 // ucitava vrijednost sa adrese 2 u R0 (to je broj elemenata niza)

	// RACUNANJE pow(2, N)
	inc R1, R1 // postavlja R1 na 1 kako bi se moglo poceti sa stepenovanjem
	
loop_pow:
	sub R7, R0, R2 // R0 - R2, broj elemenata u nizu - trenutni index
	jmpz calc_sum
	
	shl R1, R1 // shiftuje R1 (drugi arg) ulijevo i smjesta rezultat u R1 (prvi arg) sto je ekv. mnozenju sa 2
	
	inc R2, R2 // povecava brojaca za 1
	jmp loop_pow

calc_sum:
	sub R2, R2, R2 // restuj brojac na 0
	
	inc R5, R5
	inc R5, R5
	inc R5, R5
	inc R5, R5 // u R5 je sada adresa pocetka niza
	
loop_sum:
	sub R7, R0, R2 // R0 - R2, broj elemenata niza - trenutni index
	jmpz divide // ako se proslo kroz sve elemente onda treba jos samo da se podijeli sa 4
	
	add R3, R5, R2 // dodaj na adresu pocetka niza trenutni index
	ld R3, R3 // ucitaj trenutni element sa njegove adrese
	
	add R4, R4, R3 // dodaj R3 (trenutni element) na ukupnu sumu
	
	inc R2, R2 // povecava brojac za 1
	jmp loop_sum

divide:
	add R4, R4, R1 // saberi stepen dvojke i izracunatu sumu
	
	// podijeli dobijeni rezultat sa 4 sto je ekv. dijeljenju sa 4
	shr R4, R4
	shr R4, R4
	
	sub R0, R0, R0 // restuj R0 na nulu (adresa na kojoj je adresa za upis rezultata)
	ld R0, R0
	st R4, R0 // upisi rezultat (R4) na adresu u R
	
	sub R1, R1, R1 // resetuj R1 na 0
	inc R1, R1 // R1 je sada 1 (p_done)
	
	sub R0, R0, R0 // restuj R0 na nulu 
	inc R0, R0 // uvecaj R1 za 1 (adresa na kojoj je adresa za upis statusa p_done)
	ld R0, R0
	st R1, R0 // upisi rezultat (R5) na adresu u R
	
end:
	jmp end