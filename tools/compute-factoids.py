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

"""Compute total stats and various single-game high score records."""

from helper import load_csv, sort_n_rank


def find_totals(rows):
    """Compute stat totals by summing over the entire tournament."""
    # stats to sum
    totals = {
        'kills': 0, 'deaths': 0, 'assists': 0,
        'hits': 0, 'shots': 0,
        'hill time (s)': 0,
        'bomb plants': 0, 'bomb defuses': 0,
        'uplink dunks': 0, 'uplink throws': 0, 'uplink points': 0
    }
    # sum for all games in the tournament
    for row in rows:
        for k in totals:
            totals[k] += int(row[k])

    return totals


def find_records_per_mode_n_map(rows):
    """Search the entire tournament for single-game high scores across various stats."""
    # the stats for each result (must be superset of stats below)
    stats = ['player', 'team', 'series id', 'kills', 'deaths', 'k/d', 'hill time (s)', 'snd firstbloods', 'uplink points']

    # for each stat, find all results in the tournament
    records = {}
    for stat in [
        {'stat': 'kills'},
        {'stat': 'k/d'},
        {'stat': 'hill time (s)', 'mode': 'Hardpoint'},
        {'stat': 'snd firstbloods', 'mode': 'Search & Destroy'},
        {'stat': 'uplink points', 'mode': 'Uplink'}
    ]:
        for row in rows:
            k = (stat['stat'], row['mode'], row['map'])
            if 'mode' not in stat or stat['mode'] == row['mode']:
                if k not in records:
                    records[k] = []
                records[k].append({x:y for x,y in row.items() if x in stats})

    # for each stat, sort the results
    out = []
    for k in records:
        stat, mode, map_ = k
        out.append({
            'title': '{} {} - {} on {}'.format('Best' if stat == 'k/d' else 'Most', stat.capitalize(), mode, map_),
            'stat': stat,
            'mode': mode,
            'map': map_,
            'players': sort_n_rank(records[k], stat)
        })

    return sorted(out, key=lambda x: x['title'])


if __name__ == '__main__':
    print('Compute Factoids')

    rows = load_csv('../data/data-2017-08-13-champs.csv')
    totals = find_totals(rows)
    records = find_records_per_mode_n_map(rows)
    print('  loaded {} rows, {:.0f} games'.format(len(rows), len(rows)/8))

    print('\nTotals:')
    for stat, total in totals.items():
        print('{} = {}'.format(stat, total))

    print('\nRecords:')
    for record in records:
        print('  {} : {}'.format(
            record['title'],
            ', '.join(['{}. {} {}'.format(p['rank'], p['player'], p[record['stat']]) for p in record['players'][:3]])
        ))
