import round
import team

Slovensko = team.team("Slovensko", 1)

Cesko = team.team("Cesko", 2)

Ukrajina = team.team("Ukrajina", 3)

kolo = round.round((Slovensko, Cesko, Ukrajina))

kolo.getGames()





