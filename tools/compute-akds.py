# Copyright (c) 2017, Activision Publishing, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its contributors
# may be used to endorse or promote products derived from this software without
# specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""Compute player and team adjusted KDs."""

from helper import load_csv, save_csv, sort_n_rank
from operator import itemgetter

# calculate how many hardpoint, snd, and 3rd game mode kills occurred during the tournament.
# then calculate snd multiplier and 3rd game mode multipliers so that kills in these two game modes
# are weighted equal to kills in hardpoint
def calculate_kill_multipliers(rows):
    kills_hp = 0
    kills_snd = 0
    kills_3rd = 0

    # sum number of kills in each game mode
    for row in rows:
        if row['mode'] == "Hardpoint":
            kills_hp += int(row['kills'])
        elif row['mode'] == "Search & Destroy":
            kills_snd += int(row['kills'])
        else:
            kills_3rd += int(row['kills'])

    # return multipliers used to adjust kills so they are equal to hardpoint's kills
    return (float(kills_hp)/float(kills_snd), float(kills_hp)/float(kills_3rd))

# find all the kills and deaths for each player, making sure to scale them according to 
# game mode multipliers
def compute_player_adjusted_kills_deaths(rows, mult_snd, mult_3rd):
    players = {}

    for row in rows:
        mode = row['mode']
        player = row['player']
        team = row['team']
        kills = row['kills']
        deaths = row['deaths']

        if player not in players:
            if mode == "Hardpoint":
                players[player] = [team, int(kills), int(deaths)]
            elif mode == "Search & Destroy":
                players[player] = [team, mult_snd * int(kills), mult_snd * int(deaths)]
            else:
                players[player] = [team, mult_3rd * int(kills), mult_3rd * int(deaths)]
        else:
            if mode == "Hardpoint":
                players[player][1] += int(kills)
                players[player][2] += int(deaths)
            elif mode == "Search & Destroy":
                players[player][1] += mult_snd * int(kills)
                players[player][2] += mult_snd * int(deaths)
            else:
                players[player][1] += mult_3rd * int(kills)
                players[player][2] += mult_3rd * int(deaths)

    return players

# aggregate scaled kills and deaths by team
def aggregate_teams_adjusted_kills_deaths(players):
    teams = {}
    for stats in players.values():
        if stats[0] not in teams:
            teams[stats[0]] = [stats[1], stats[2]]
        else:
            teams[stats[0]][0] += stats[1]
            teams[stats[0]][1] += stats[2]
    
    return teams

# calculate adjusted KDs for players
def calculate_player_akds(players):
    player_akds = {}

    for player, stats in players.items():
        player_akds[player] = stats[1]/stats[2]

    return player_akds

# calculate adjusted KDs for teams
def calculate_team_akds(teams):
    team_akds = {}

    for team, stats in teams.items():
        team_akds[team] = stats[0]/stats[1]

    return team_akds


if __name__ == '__main__':
    rows = load_csv('../data/data-2017-08-13-champs.csv')

    print('Summing kills...')
    (mult_snd, mult_3rd) = calculate_kill_multipliers(rows)

    print('Adjusting player stats...')
    players = compute_player_adjusted_kills_deaths(rows, mult_snd, mult_3rd)

    print('Aggregating adjusted team stats..')
    teams = aggregate_teams_adjusted_kills_deaths(players)

    print('Calculating player adjusted K/Ds...')
    player_akds = calculate_player_akds(players)
    player_akds = sorted(player_akds.items(), key=itemgetter(1), reverse=True)

    print('Calculating team adjusted K/Ds...')
    team_akds = calculate_team_akds(teams)
    team_akds = sorted(team_akds.items(), key=itemgetter(1), reverse=True)

    print()
    print("Top Five Player aKDs:")
    for player in player_akds[:5]:
        print(player[0] + ":", player[1])

    print()
    print("Top Five Team aKDs:")
    for team in team_akds[:5]:
        print(team[0] + ":", team[1])
    # print()
    # print(player_akds)
    # print(team_akds)