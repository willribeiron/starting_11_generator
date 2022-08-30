
# Tottenham Hotspur's starting 11 generator
The program generates starting 11s from a CSV with informations about Tottenham Hotspur's squad.
The user chooses a tactical formation from 4 available and the program generates the starting 11.
The generate_team function uses the 'random' library and also have the FIFA video-game players' overalls (a point system) as a 'weight' parameter, the higher the overall, the higher the chances of the player being selected. 


# Tactical formations
The user has to choose 1 among 4 tactical formation options, which are '3-4-3', '3-5-2', '4-4-2' and '4-3-3'.
The numbers in the formations basically work as the parameters of the generate_team function.

Options:
-
'3-4-3':
- 3 centre-backs
- 2 wing-backs
- 2 midfielders
- 3 strikers

'3-5-2':
- 3 centre-backs
- 2 wing-backs
- 3 midfielders
- 2 strikers

'4-4-2':
- 4 centre-backs
- 2 wing-backs
- 2 midfielders
- 2 strikers

'4-3-3':
- 2 centre-backs
- 2 wing-backs
- 3 midfielders
- 3 strikers