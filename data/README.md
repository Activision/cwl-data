# CWL Champs 2017

The 2017 Call of Duty World League Championships were played in Orlando, FL from Aug 9 - Aug 13.

## Definitions

Some definitions:

 * Basic Stats - simple gameplay counting stats (starting at 0 and going up), such as `kills`, `deaths`, `hill time`, `bomb defuses`, `firstbloods`, ...
 * Derived Stats - stats computed from other basic stats, such as `k/d` (`kills` divided by `deaths`), `k per 10min` (`kills` divided by `duration` per 10 minutes), `firstblood %` (`firstbloods` divided by `snd rounds`), ...
 * Aggregate Stats - basic stats summed over a certain period of time (series, tournament, season) then normalized per game to allow player vs player comparisons, such as `season k/d`, `kills per game`, `plants per round`, `points per game`, ...
 * Advanced Stats (aka sabermetrics) - complex derived stats that *best* describe player performance and/or enable *better* player vs player comparisons, such as `QBR` from american football, `WAR` and `OPS+` from baseball, `PER` in basketball, ...

For Call of Duty, every class of stats is under active investigation.

## The Stats

 * `match id` - unique game id
 * `series id` - unique series id
 * `end time` - game end time in UTC
 * `duration (s)` - game duration in seconds (includes breaks between rounds, halftimes, ...)
 * `mode` - the game mode (`Hardpoint`, `Search & Destroy`, ...)
 * `map` - the map
 * `team` - the team
 * `player` - the player
 * `win?` - `W` if the player won the game, otherwise `L`
 * `kills` - kills *(for the player)*
 * `deaths` - deaths
 * `+/-` - plus-minus (derived, `kills` minus `deaths`)
 * `k/d` - kill-death ratio (derived, `kills` divided by `deaths`)
 * `kills per 10min` - kills per 10 minutes (derived)
 * `deaths per 10min` - deaths per 10 minutes (derived)
 * `assists` - assists
 * `headshots` - kills via headshot
 * `suicides` - kills from the environment (aka falling off the map)
 * `team kills` - killing
 * `hits` - hits from a gun
 * `shots` - shots fired from a gun
 * `accuracy (%)` - hits per shot as a percentage (dervied)
 * `avg kill dist (m)` - average kill distance
 * `fave weapon` - most used primary gun per loadout
 * `fave rig` - most used rig per loadout
 * `fave payload` - most used rig payload per loadout
 * `fave trait` - most used rig trait per loadout
 * `fave scorestreaks` - top 3 scorestreaks used per loadout
 * `hill time (s)` - HP hill time in seconds
 * `hill captures` - HP hill captures
 * `hill defends` - HP hill defends
 * `snd firstbloods` - SND first kill of the round
 * `bomb pickups` - SND bomb pickups
 * `bomb plants` - SND bomb plants
 * `bomb defuses` - SND bomb defuses
 * `bomb sneak defuses` - SND bomb sneak defuses (defuse completed while opponents still alive)
 * `uplink dunks` - UPL dunks
 * `uplink throws` - UPL throws
 * `uplink points` - UPL points (derived, `dunks` times 2 plus `throws`)
 * `2-piece` - 2 kills by the player within 5 seconds without dying
 * `3-piece` - 3 kills by the player within 10 seconds without dying
 * `4-piece` - 4 kills by the player within 15 seconds without dying
 * `multikills` - total multikills (derived, sum of `2-piece` plus `3-piece` plus `4-piece`)
 * `4-streak` - 4 kills without dying (no time restriction)
 * `5-streak` - 5 kills without dying
 * `6-streak` - 6 kills without dying
 * `7-streak` - 7 kills without dying
 * `8+-streak` - 8 or more kills without dying
 * `4+-streak` - 4 or more kills without dying
 * `scorestreaks earned` - number of scorestreaks earned
 * `scorestreaks used` - number of scorestreaks used
 * `payloads earned` - number of payload abilities earned
 * `payloads used` - number of payload abilities used


## Missing Data

297 of 298 games have complete data, but a hardware failure during a game between Envyus and Ghost Gaming (Winner's Quarterfinals - Map 2 - Search & Destory on Retaliation) resulted in partial data loss.  The failure occured with Envyus leading 4-0, resulting in data from the first 4 rounds to be lost.  Video replay allowed for manual recovery of all basic stats (`kills`, `deaths`, `firstblood`, `defuses`, ...), but some more complex stats were unrecoverable.
