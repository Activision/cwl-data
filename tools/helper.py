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

import csv

def load_csv(filename):
    """Helper to load the tournament data from csv."""
    rows = []
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows


def save_csv(filename, rows, header):
    """Helper to write data as csv."""
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, header, restval='?', extrasaction='ignore', quoting=csv.QUOTE_ALL)
        writer.writeheader()
        writer.writerows(rows)


def sort_n_rank(rows, stat, highest_is_first=True):
    """Helper to sort and rank the rows for the given stat."""
    # sort rows
    rows = sorted(rows, key=lambda x: (float(x.get(stat)), float(x.get('k/d')), x.get('player'), x.get('team')), reverse=highest_is_first)

    # add rank to each row
    val, rank = 0, 0
    for i, row in enumerate(rows):
         if i == 0 or val != row[stat]:
             row['rank'] = rank = i+1
             val = row[stat]
         else:
             row['rank'] = rank
    return rows


def find_modes_n_maps(rows):
    """Helper to find all the modes and maps played in the tournament."""
    modes_n_maps = {}
    for row in rows:
        if row['mode'] not in modes_n_maps:
            modes_n_maps[row['mode']] = []
        if row['map'] not in modes_n_maps[row['mode']]:
            modes_n_maps[row['mode']].append(row['map'])
    return modes_n_maps
