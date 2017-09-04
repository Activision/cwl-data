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

from helper import load_csv, save_csv, sort_n_rank

def aggregate_players(rows):
    """Compute aggregate stats for each player for the tournament."""
    # stats to sum
    stats = {'kills', 'deaths', 'duration (s)'}

    # compute base stats (aggregated)
    players = {}
    for row in rows:
        p = row['player']
        if p not in players:
            players[p] = {'player': p, 'team': row['team'], 'n': 0, **{k:0 for k in stats}}
        players[p]['n'] += 1
        for k in stats:
            players[p][k] += int(row[k]) if row[k].isdigit() else float(row[k])

    # compute derived stats
    for p in players.values():
        p['k/d'] = '{:.2f}'.format(p['kills'] / p['deaths'])
        p['+/-'] = '{}{}'.format('+' if p['kills'] > p['deaths'] else '', p['kills'] - p['deaths'])
        p['k per 10min'] = '{:.1f}'.format(600 * p['kills'] / p['duration (s)'])

    return sorted(players.values(), key=lambda x: (x['team'].lower(), x['player'].lower()))


def aggregate_teams(players):
    """Compute aggregate stats for each team for the tournament."""
    # stats to sum
    stats = {'kills', 'deaths'}

    # don't sum these stats
    dont_sum = {'n', 'duration (s)'}

    # compute base stats (aggregated)
    teams = {}
    for p in players:
        t = p['team']
        if t not in teams:
            teams[t] = {'team': t, **{k:0 for k in stats}, **{k:p[k] for k in dont_sum}}
        for k in stats:
            teams[t][k] += p[k]

    # compute derived stats
    for t in teams.values():
        t['k/d'] = '{:.2f}'.format(t['kills'] / t['deaths'])
        t['+/-'] = '{}{}'.format('+' if t['kills'] > t['deaths'] else '', t['kills'] - t['deaths'])
        t['k per 10min'] = '{:.1f}'.format(600 * t['kills'] / t['duration (s)'])

    return sorted(teams.values(), key=lambda x: x['team'].lower())


if __name__ == '__main__':
    print('Compute Aggregates')

    rows = load_csv('../data/data-2017-08-13-champs.csv')
    players = aggregate_players(rows)
    teams = aggregate_teams(players)
    print('  loaded {} rows, {:.0f} games, {} players, {} teams'.format(len(rows), len(rows)/8, len(players), len(teams)))

    print('\nTop 5 Players by K/D:')
    for p in sort_n_rank(players, 'k/d')[:5]:
        print(p['rank'], p['player'], p['team'], p['k/d'])

    print('\nTop 5 Teams by K/D:')
    for t in sort_n_rank(teams, 'k/d')[:5]:
        print(t['rank'], t['team'], t['k/d'])

    print ('\nsaving champs-players.csv')
    save_csv('champs-players.csv', players, ['player','team','n','duration (s)','kills','deaths','+/-','k/d','k per 10min'])

    print ('saving champs-teams.csv')
    save_csv('champs-teams.csv', teams, ['team','n','duration (s)','kills','deaths','+/-','k/d','k per 10min'])
