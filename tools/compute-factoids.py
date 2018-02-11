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

import argparse
import re


TOTALS = {
    'iw': ['kills', 'deaths', 'assists', 'hits', 'shots', 'hill time (s)', 'bomb plants', 'bomb defuses', 'uplink dunks', 'uplink throws', 'uplink points'],
    'ww2': ['kills', 'deaths', 'assists', 'hits', 'shots', 'hill time (s)', 'bomb plants', 'bomb defuses', 'ctf captures', 'ctf returns', 'ctf pickups', 'ctf defends', 'ctf kill carriers', 'ctf flag carry time (s)']
}

STATS = {
    'iw': [
        {'stat': 'kills'},
        {'stat': 'k/d'}, 
        {'stat': 'hill time (s)', 'mode': 'Hardpoint'},
        {'stat': 'snd firstbloods', 'mode': 'Search & Destroy'},
        {'stat': 'uplink points', 'mode': 'Uplink'}
    ],
    'ww2': [
        {'stat': 'kills'},
        {'stat': 'k/d'},
        {'stat': 'hill time (s)', 'mode': 'Hardpoint'},
        {'stat': 'snd firstbloods', 'mode': 'Search & Destroy'},
        {'stat': 'ctf captures', 'mode': 'Capture The Flag'}
    ]
}


def find_totals(rows, title):
    """Compute stat totals by summing over the entire tournament."""
    # stats to sum
    totals = {stat:0 for stat in TOTALS[title]}
    for row in rows:
        for k in totals:
            # check if stat is float or int
            if re.findall("\d+\.\d+", row[k]):
                totals[k] += float(row[k])
            else:
                totals[k] += int(row[k])

    return totals


def find_records_per_mode_n_map(rows, title):
    """Search the entire tournament for single-game high scores across various stats."""
    # the stats for each result (must be superset of stats below)
    stats = ['player', 'team', 'series id', 'kills', 'deaths', 'k/d', 'hill time (s)', 'snd firstbloods']
    if title == 'ww2':
        stats.append('ctf captures')
    else:
        stats.append('uplink points')

    # for each stat, find all results in the tournament
    records = {}
    for stat in STATS[title]:
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


def parse_cmd_args():
    """Parses command line arguments."""
    # create parser
    help_desc = 'Compute total stats and various single-game high score records.'
    parser = argparse.ArgumentParser(description=help_desc)

    # -argument- [optional] by default, script will compute factoids for COD:IW
    parser.add_argument('--title', metavar='TITLE',
                        help='sets COD title to compute factoids for')

    # -argument- [optional]
    parser.add_argument('--path', metavar='PATH',
                        help='imports .csv data from input path')

    # parse command line arguments
    return vars(parser.parse_args())


if __name__ == '__main__':
    args = parse_cmd_args()
    title = 'iw' if not args['title'] else args['title']
    path = '../data/data-2017-08-13-champs.csv' if not args['path'] else args['path']

    print('Factoids:')

    rows = load_csv(path)
    totals = find_totals(rows, title)
    records = find_records_per_mode_n_map(rows, title)
    print('  loaded {} rows, {:.0f} games'.format(len(rows), len(rows)/8))

    print('\nTotals:')
    for stat, total in totals.items():
        print('  {} = {}'.format(stat, total))

    print('\nRecords:')
    for record in records:
        print('  {}\n    {}'.format(
            record['title'],
            ', '.join(['{}. {} {}'.format(p['rank'], p['player'], p[record['stat']]) for p in record['players'][:3]])
        ))
