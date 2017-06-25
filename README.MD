# Design kvalifikacie
Zvolil som classovy design. Program bude obsahovat triedy pre timy, kola a potom hlavny program
## Zoznam tried
* team

Trieda reprezentuje jednotlive timy. Obsahuje ich ranking a bilanciu bodov (vynuluje sa pred kazdym kolom)

* round

Trieda reprezentuje jednotlive kola, ktorych spravanie sa ale v zavislosti do kola moze menit podla toho, ako prebieha kvalifikacia

Obsahuje zoznam timov v danom kole, zoznam zapasov s vysledkom, ale aj priebeh hry

## Hlavny program

Vytvoria sa instancie triedy team a round, ktore mozu overridenut aj niektore metody. Vitazi z jednotlivych kol su potom priradeni do dalsich, kde sa rozdelia do skupin 
(tiez instancie triedy round).

