import csv


def load_csv(filename):
    """Load the tournament data from csv."""
    rows = []
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows


def save_csv(filename, rows, header):
    """Write data as csv."""
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, header, restval='?', extrasaction='ignore', quoting=csv.QUOTE_ALL)
        writer.writeheader()
        writer.writerows(rows)


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


def sort_n_rank(rows, stat, highest_is_first=True):
    """Helper to sort and rank the rows for the given stat."""
    # sort rows
    rows = sorted(rows, key=lambda x: float(x[stat]), reverse=highest_is_first)

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
    print('Compute Aggregates')

    rows = load_csv('../data/data-2017-08-13-champs.csv')
    players = aggregate_players(rows)
    teams = aggregate_teams(players)
    print('  loaded {} rows, {} players, {} teams'.format(len(rows), len(players), len(teams)))

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
