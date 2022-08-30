import random
import csv

GK = []
CB = []
RWB = []
LWB = []
MF = []
ST = []

with open('elenco.csv', newline='') as csvfile:
    elenco = csv.DictReader(csvfile)
    for jogador in elenco:
        if 'GOL' in jogador['posicao']:
            jogador['posicao'] = '-----GK----- '
            GK.append(jogador)
        if 'ZAG' in jogador['posicao']:
            jogador['posicao'] = '-----Centre-backs----- '
            CB.append(jogador)
        if 'LD' in jogador['posicao']:
            jogador['posicao'] = '-----Right wing-back----- '
            RWB.append(jogador)
        if 'LE' in jogador['posicao']:
            jogador['posicao'] = '-----Left wing-back----- '
            LWB.append(jogador)
        if 'MEIA' in jogador['posicao']:
            jogador['posicao'] = '-----Midfielders----- '
            MF.append(jogador)
        if 'ATA' in jogador['posicao']:
            jogador['posicao'] = '-----Strikers----- '
            ST.append(jogador)


def generate_team(cbs, rwb, mfs, lwb, striker):
    team = []
    goalkeeper = random.choices(GK, weights=[float(x['pontuacao']) for x in GK])
    team.append(goalkeeper[0])
    defenders = []
    for i in range(cbs):
        while len(defenders) != cbs:
            centre_back = random.choices(CB, weights=[float(x['pontuacao']) for x in CB])
            if not centre_back[0] in defenders:
                defenders.append(centre_back[0])
    for i in defenders:
        team.append(i)
    right_wing_back = random.choices(RWB, weights=[float(x['pontuacao']) for x in RWB], k=rwb)
    if len(right_wing_back) > 0:
        team.append(right_wing_back[0])
    midfielders = []
    for i in range(mfs):
        while len(midfielders) != mfs:
            midfielder = random.choices(MF, weights=[float(x['pontuacao']) for x in MF])
            if not midfielder[0] in midfielders:
                midfielders.append(midfielder[0])
    for i in midfielders:
        team.append(i)
    left_wing_back = random.choices(LWB, weights=[float(x['pontuacao']) for x in LWB], k=lwb)
    if len(left_wing_back) > 0:
        team.append(left_wing_back[0])
    strikers = []
    for i in range(striker):
        while len(strikers) != striker:
            st = random.choices(ST, weights=[float(x['pontuacao']) for x in ST])
            if not st[0] in strikers:
                strikers.append(st[0])
    for i in strikers:
        team.append(i)
    starting_eleven = []
    for i in team:
        if not i['posicao'] in starting_eleven:
            starting_eleven.append(i['posicao'])
        starting_eleven.append(i['jogador'])
    for i in starting_eleven:
        print(i)
