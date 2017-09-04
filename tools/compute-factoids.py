import string
import csv


def load_csv(filename):
    """Load the tournament data from csv."""
    rows = []
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows


def find_modes_n_maps(rows):
    """Find all the modes and maps played in the tournament."""
    modes_n_maps = {}
    for row in rows:
        if row['mode'] not in modes_n_maps:
            modes_n_maps[row['mode']] = []
        if row['map'] not in modes_n_maps[row['mode']]:
            modes_n_maps[row['mode']].append(row['map'])
    return modes_n_maps


def find_totals(rows):
    """Compute various stat totals."""
    totals = {
        'kills': 0, 'deaths': 0, 'assists': 0,
        'hits': 0, 'shots': 0,
        'hill time (s)': 0,
        'bomb plants': 0, 'bomb defuses': 0,
        'uplink dunks': 0, 'uplink throws': 0, 'uplink points': 0
    }
    for row in rows:
        for k in totals:
            totals[k] += int(row[k])

    return totals


def find_records_per_mode_n_map(rows, modes_n_maps):
    stats = ['player', 'team', 'series id', 'kills', 'deaths', 'k/d', 'hill time (s)', 'snd firstbloods', 'uplink points']
    records = {}
    for row in rows:
        for stat in [
            {'stat': 'kills'},
            {'stat': 'k/d'},
            {'stat': 'hill time (s)', 'mode': 'Hardpoint'},
            {'stat': 'snd firstbloods', 'mode': 'Search & Destroy'},
            {'stat': 'uplink points', 'mode': 'Uplink'}
        ]:
            k = (stat['stat'], row['mode'], row['map'])
            if 'mode' not in stat or stat['mode'] == row['mode']:
                if k not in records:
                    records[k] = []
                records[k].append({x:y for x,y in row.items() if x in stats})

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


def sort_n_rank(rows, stat, highest_is_first=True):
    """Helper to sort and rank the rows for the given stat."""
    # sort rows
    rows = sorted(rows, key=lambda x: (float(x[stat]), float(x['k/d']), x['player']), reverse=highest_is_first)

    # add rank
    val, rank = 0, 0
    for i, row in enumerate(rows):
         if i == 0 or val != row[stat]:
             row['rank'] = rank = i+1
             val = row[stat]
         else:
             row['rank'] = rank
    return rows


if __name__ == '__main__':
    print('Compute Factoids')

    rows = load_csv('../data/data-2017-08-13-champs.csv')
    modes_n_maps = find_modes_n_maps(rows)
    totals = find_totals(rows)
    records = find_records_per_mode_n_map(rows, modes_n_maps)
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
