# The Data

Call of Duty World League data.

## Tabular Data

Tabular data is simply per-player per-game stats for every game in the tournament (aka 1 row per player-game).

 * 2017
    * CWL Champs - Orlando, FL - Aug 9-13, 2017 - [data-2017-08-13-champs.csv](data-2017-08-13-champs.csv)
 * 2018
    * CWL Dallas - Dallas, TX - Dec 8-10, 2017 - [data-2017-12-10-dallas.csv](data-2017-12-10-dallas.csv)
    * CWL New Orleans - New Orleans, LA - Jan 12-14, 2018 - [data-2018-01-14-neworleans.csv](data-2018-01-14-neworleans.csv)
    * CWL Pro League, Stage 1 - Columbus, OH - Jan 23-Apr 8, 2018 - [data-2018-04-08-proleague1.csv](data-2018-04-08-proleague1.csv)
    * CWL Atlanta - Atlanta, GA - Mar 9-11, 2018 - [data-2018-03-11-atlanta.csv](data-2018-03-11-atlanta.csv)
    * CWL Birmingham - Birmingham, UK - Mar 30-Apr 1, 2018 - [data-2018-04-01-birmingham.csv](data-2018-04-01-birmingham.csv)
    * CWL Pro League, Relegation - Seattle, WA - Apr 19, 2018 - [data-2018-04-19-relegation.csv](data-2018-04-19-relegation.csv)
    * CWL Seattle - Seattle, WA - Apr 20-22, 2018 - [data-2018-04-22-seattle.csv](data-2018-04-22-seattle.csv)
    * CWL Pro League, Stage 2 - Columbus, OH - May 15-July 29, 2018 - [data-2018-07-29-proleague2.csv](data-2018-07-29-proleague2.csv)
    * CWL Anaheim - Anaheim, CA - Jun 15-17, 2018 - [data-2018-06-17-anaheim.csv](data-2018-06-17-anaheim.csv)
    * CWL Champs - Columbus, OH - Aug 15-19, 2018 - [data-2018-08-19-champs.csv](data-2018-08-19-champs.csv)
 * 2019
    * CWL Pro League Qualifer - Columbus, OH - Jan 16-20, 2019 - [data-2019-01-20-proleague-qual.csv](data-2019-01-20-proleague-qual.csv)
    * CWL Pro League - Columbus, OH - Feb 4-Jul 5, 2019 - [data-2019-07-05-proleague.csv](data-2019-07-05-proleague.csv)
    * CWL Fort Worth - Fort Worth, TX - Mar 15-17, 2019 - [data-2019-03-17-fortworth.csv](data-2019-03-17-fortworth.csv)
    * CWL London - London, UK - May 3-5, 2019 - [data-2019-05-05-london.csv](data-2019-05-05-london.csv)
    * CWL Anaheim - Anaheim, CA - Jun 14-16, 2019 - [data-2019-06-16-anaheim.csv](data-2019-06-16-anaheim.csv)
    * CWL Pro League Finals - Miami, FL - Jul 19-21, 2019 - [data-2019-07-21-proleague-finals.csv](data-2019-07-21-proleague-finals.csv)
    * CWL Champs - Los Angeles, CA - Aug 14-18, 2019 - [data-2019-08-18-champs.csv](data-2019-08-18-champs.csv)

## Structured Data

Structured data is provided as nested json per game, where each game includes individual game events such as spawns and deaths.  See [Structured](structured) for details.

## Definitions

Some definitions:

 * __Basic Stats__ - simple gameplay counting stats (starting at 0 and going up), such as `kills`, `deaths`, `hill time`, `bomb defuses`, `firstbloods`, ...
 * __Derived Stats__ - stats computed from other basic stats, such as `k/d` (`kills` divided by `deaths`), `k per 10min` (`kills` divided by `duration` per 10 minutes), `firstblood %` (`firstbloods` divided by `snd rounds`), ...
 * __Aggregate Stats__ - basic stats summed over a certain period of time (series, tournament, season) then normalized per game to allow player vs player comparisons, such as `season k/d`, `kills per game`, `plants per round`, `points per game`, ...
 * __Advanced Stats__ (aka Sabermetrics) - complex derived stats that *best* describe player performance and/or enable *better* player vs player comparisons, such as `QBR` from football (american), `WAR` and `OPS+` from baseball, `PER` in basketball, ...

For Call of Duty, everything from basic stats to advanced stats is under active investigation.  What stats are best when comparing players? When stats are best when comparing teams?  What stats best predict future performance?  What stats can be used to succinctly capture the story of the games, the series, the pool, or the tournament?

## The Stats

The basic and derived stats found in the data (aka the columns in the tabular data files):

 * `match id` - unique game id
 * `series id` - unique series id
 * `end time` - game end time in UTC
 * `duration (s)` - game duration in seconds (includes breaks between rounds, halftimes, ...)
 * `mode` - the game mode (`Hardpoint`, `Search & Destroy`, ...)
 * `map` - the map
 * `team` - the team
 * `player` - the player
 * `win?` - `W` if the player won the game, otherwise `L`
 * `score` - the team's score in the game
 * `kills` - kills *for the player*
 * `deaths` - deaths
 * `+/-` - plus-minus (derived, `kills` minus `deaths`)
 * `k/d` - kill-death ratio (derived, `kills` divided by `deaths`)
 * `kills per 10min` - kills per 10 minutes (derived)
 * `deaths per 10min` - deaths per 10 minutes (derived)
 * `player score` - the player's score in the game (BO4)
 * `player spm` - the player's score per minute (derived) (BO4)
 * `damage dealt` - damage dealt (BO4)
 * `ekia` - ekia *for the player* (BO4)
 * `assists` - assists
 * `headshots` - kills via headshot
 * `suicides` - kills from the environment (aka falling off the map)
 * `team kills` - friendly fire kills (aka killing a player on your own team)
 * `team deaths` - friendly fire deaths (aka getting killed by your own team)
 * `kills (stayed alive)` - kills where the attacker is not subsequently killed within the next 5 seconds
 * `hits` - hits from a gun
 * `shots` - shots fired from a gun
 * `accuracy (%)` - hits per shot as a percentage (dervied)
 * `num lives` - total number of lives (WW2)
 * `time alive (s)` - total time alive (in s) (WW2)
 * `avg time per life (s)` - average time alive per life (WW2, derived, `time alive` divided by `num lives`)
 * `avg kill dist (m)` - average kill distance
 * `fave weapon` - most used primary gun per loadout
 * `fave rig` - most used rig per loadout (IW)
 * `fave payload` - most used rig payload per loadout (IW)
 * `fave trait` - most used rig trait per loadout (IW)
 * `fave division` - most used division per loadout (WW2)
 * `fave training` - most used basic training per loadout (WW2)
 * `fave scorestreaks` - top 3 scorestreaks used per loadout
 * `hill time (s)` - HP hill time in seconds
 * `hill captures` - HP hill captures
 * `hill defends` - HP hill defends
 * `snd rounds` - SND rounds
 * `snd firstbloods` - SND first kill of the round (killing a teammate does *not* count as firstbloods)
 * `snd firstdeaths` - SND first death of the round (WW2, being killed by a teammate *does* count as a firstdeath)
 * `snd survives` - SND alive at end of the round (WW2)
 * `bomb pickups` - SND bomb pickups
 * `bomb plants` - SND bomb plants
 * `bomb defuses` - SND bomb defuses
 * `bomb sneak defuses` - SND bomb sneak defuses (aka ninja defuse, when defuse completed with at least one opponent alive)
 * `snd 1-kill round` - _exactly_ 1 kill in an SND round
 * `snd 2-kill round` - 2 kills in an SND round
 * `snd 3-kill round` - 3 kills in an SND round
 * `snd 4-kill round` - 4 kills in an SND round (aka an Ace)
 * `uplink dunks` - UPL dunks (IW)
 * `uplink throws` - UPL throws (IW)
 * `uplink points` - UPL points (derived, `dunks` times 2 plus `throws`, IW)
 * `ctf captures` - CTF captures (WW2)
 * `ctf returns` - CTF returns (WW2)
 * `ctf pickups` - CTF pickups (anywhere, not just from opponent base, WW2)
 * `ctf defends` - CTF defends (aka killing an oppenent *near* your flag, WW2)
 * `ctf kill carriers` - CTF kill carriers (aka killing an opposing flag carrier, WW2)
 * `ctf flag carry time (s)` - CTF flag carry time (WW2)
 * `2-piece` - 2 kills by the player without dying, separated by <= 5 seconds (aka 2 kills in 5s max)
 * `3-piece` - 3 kills by the player without dying, each kill separated by <= 5 seconds (aka 3 kills in 10s max)
 * `4-piece` - 4 kills by the player without dying, each kill separated by <= 5 seconds (aka 4 kills in 15s max)
 * `multikills` - total multikills (IW, derived, sum of `2-piece` plus `3-piece` plus `4-piece`)
 * `4-streak` - 4 kills without dying (within a single round, otherwise no time restriction)
 * `5-streak` - 5 kills without dying
 * `6-streak` - 6 kills without dying
 * `7-streak` - 7 kills without dying
 * `8+-streak` - 8 or more kills without dying
 * `4+-streak` - 4 or more kills without dying (IW)
 * `scorestreaks earned` - number of scorestreaks earned
 * `scorestreaks used` - number of scorestreaks used
 * `scorestreaks deployed` - number of times a scorestreak is deployed (WW2, for Flamethrower and other multi-use scorestreaks)
 * `scorestreaks kills` - kills with a scorestreak (WW2)
 * `scorestreaks assists` - assists with a scorestreak (WW2)
 * `payloads earned` - number of payload abilities earned (IW)
 * `payloads used` - number of payload abilities used (IW)

Note: not all stats are present in all seasons or tournaments of Call of Duty World League as the rules can and do change.

## Missing Data

 * 2017
    * CWL Champs (Aug 9-13, 2017)
       - 297 of 298 games have complete data
       - hardware failure during a game between Envyus and Ghost Gaming (Winner's Quarterfinals - Map 2 - Search & Destory on Retaliation) resulted in partial data loss.  The failure occured with Envyus leading 4-0, resulting in data from the first 4 rounds to be lost.  Video replay allowed for manual recovery of all basic stats (`kills`, `deaths`, `firstblood`, `defuses`, ...), but some more complex stats were unrecoverable.
 * 2018
    * CWL Dallas (Dec 8-10, 2017)
       - 269 of 269 *elite* games have data (all pool play, plus both champ brackets)
       - use of a prohibited scorestreak resulted in a forfeit by Rise Nation of game 1 against Red Reserve in pool play, but that data **IS** included
    * CWL New Orleans (Jan 12-14, 2018)
       - 280 of 280 *elite* games have data
    * CWL Pro League, Stage 1 (Jan 23-Apr 8, 2018)
       - 503 of 504 games captured, including playoffs
       - week 6 - the only lost game was CTF from Echo Fox vs Red Reserve on Wed, Feb 28
    * CWL Atlanta (Mar 9-11, 2018)
       - day 1 - lost the CTF game from Evil Geniuses vs Vitality on Fri, Mar 9
       - day 2 - lost 5 games due to data server crash
    * CWL Birmingham (Mar 30-Apr 1, 2018)
       - massive data loss (lost ~80 games, only captured 164 games), dataset is *NOT* filled out yet (see [#11](/user/project/issues/11) if you want to help)
    * CWL Pro League, Relegation (Apr 19, 2018)
       - lost CTF game 3 from Epsilon vs Vitality on Thurs, Apr 19
    * CWL Seattle (Apr 20-22, 2018)
       - day 1 - lost HP game 1 from Echo Fox vs Rise Nation
       - day 2 - lost both HP game 4 and SND game 5 from Unilad vs Ghost Gaming
    * CWL Pro League, Stage 2 (May 15-July 29, 2018)
       - week 4 - only first HP game of the week eUnited v Unilad
    * CWL Anaheim (Jun 15-17, 2018)
       - day 1 - quitting while a game was in progress resulted in a forfeit by Complexity in game 3 against Optic in pool play, but that data **IS** included
       - day 3 - lost SND game 5 from Faze vs Mindfreak
       - day 3 - game 4 HP from Rise Nation vs Red Reserve was a *tie*, but that data **IS** included
    * CWL Champs (Aug 15-19, 2018)
       - 295 of 296 games have complete data
       - lost very last pool play game of Day 2, the game 4 HP from Echo Fox vs Team Vitality
 * 2019
    * CWL Pro League Qualifier (Jan 16-20, 2019)
       - 317 of ~400 games captured - LAN data system was in beta and significant data loss occurred
    * CWL Pro League (Feb 5-Jul 5, 2019)
       - 221 of 226 games captured for Week 1 - Week 4
       - 569 games through Week 10
       - 696 games in total (12 weeks)
    * CWL Fort Worth (Mar 15-17, 2019)
       - minimal data loss
    * CWL London (May 3-5, 2019)
       - lost first few series on Friday due to site power issues
    * CWL Anaheim (Jun 14-16, 2019)
       - yeah! zero data loss
    * CWL Pro League Finals (Jul 19-21, 2019)
       - 93 of 93 games. zero data loss.
    * CWL Champs (Aug 14-18, 2019)
       - 296 of 300 games have complete data