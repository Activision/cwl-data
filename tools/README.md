# CWL Data Tools

Tools and code for processing the data.

## Compute Factoids

Compute total stats and various single-game high score records.

### Usage

Run it (requires Python >= 3.5):

```
> cd tools
> python compute-factoids.py
```

Output:

```
Factoids:
  loaded 2384 rows, 298 games

Totals:
  kills = 40798
  deaths = 40886

Records:
  Most Kills - Hardpoint on Throwback
    1. Scump 45, 2. Formal 44, 3. Slasher 42
  Most Uplink points - Uplink on Frost
    1. Zero 11, 2. Fastballa 8, 2. Proto 8
```

## Compute Aggregates

Compute player and team aggregate stats for a tournament.  Outputs aggregates as csv files.

### Usage

Run it (requires Python >= 3.5):

```
> cd tools
> python compute-aggregates.py
```

Output:

```
Aggregates:
  loaded 2384 rows, 298 games, 128 players, 32 teams

Top 3 Players by K/D:
1 Formal OpTic Gaming 1.44
2 Royalty Enigma6 1.35
3 Slasher Team EnVyUs 1.27

Top 3 Teams by K/D:
1 OpTic Gaming 1.16
2 Team EnVyUs 1.10
2 FaZe Clan 1.10
```

## Future?

What other tools should we build?  What stats do you want to see?  Drop us an [Issue](https://github.com/Activision/cwl-data/issues) if you want to share ideas.  Or see [Contributing](CONTRIBUTING.md) on how to share code.
