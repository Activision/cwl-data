# The Evented Data

Evented data is provided as nested json.  Most importantly, evented data contains unique intra-game data, such as individual kills events.

## Evented Data

* [evented-2017-08-13-champs.tgz](evented-2017-08-13-champs.tgz) - evented 2017 CWL Championships data

## Examples

Here are a few example evented data files (CWL Champs 2017 Grand Finals, Optic Gaming vs Team Envyus):

 * `hp` - [evented-1502655504-A23F8504-146F-11D3-6C6E-0CFE454272F2.json](evented-1502655504-A23F8504-146F-11D3-6C6E-0CFE454272F2.json)
 * `snd` - [evented-1502656269-A850EC88-1471-11D3-6C6E-0CFE454272F2.json](evented-1502656269-A850EC88-1471-11D3-6C6E-0CFE454272F2.json)
 * `upl` - [evented-1502657302-F28A9CF2-1473-11D3-6C6E-0CFE454272F2.json](evented-1502657302-F28A9CF2-1473-11D3-6C6E-0CFE454272F2.json)

## The Stats

 * `title` - the Call of Duty title
 * `platform` - the console
 * `id` - unique game id
 * `series_id` - unique series id
 * `start_time_s` - the game start time as UTC timestamp
 * `end_time_s` - the game end time as UTC timestamp
 * `duration_ms` - the game duration in milliseconds
 * `mode` - the game mode
 * `map` - the map
 * `rounds` - the number of rounds (`hp` is 1, `upl` is 2 or 4 for overtime, ...)
 * `hp_hill_names` - (only for `hp`) the name of the hills
 * `hp_hill_rotations` - (only for `hp`) the number of hill rotations
 * `teams` - the list of teams
    * `name` - the team name
    * `score` - the score
    * `is_victor` - is this team the winner? (`true` if they won, otherwise `false`)
    * `round_scores` - the list of team score in each round (or hill rotation if `hp`)
 * `players` - the list of players
    * see [Data](data#the-stats)...player stats are identical to the tabular stats, _mostly_
 * `events` - the list of events
    * `type` - the type of event (`roundstart`, `roundend`, `spawn`, `death`)
    * `time` - the relative time from match start of this event (somewhat confusingly games don't always _begin_ exactly at match start)
    * `round` - the round of this event1,
    * `round_time` - the relative time from round start of this event
    * `data` - nested metadata for this event, depends on event `type`
       * `score1` - (only for `roundend`) the score at the end of the round for team 1
       * `score2` - (only for `roundend`) the score at the end of the round for team 2
       * `id` - (for `spawn` and `death`) the player
       * `team` - (for `spawn` and `death`) the player's team index
       * `life` - (for `spawn` and `death`) the unique spawn index
       * `pos` - (for `spawn` and `death`) the player's location in x,y,z (in game units)
       * `attacker_id` - (only for `death`) the attacker
       * `attacker_team` - (only for `death`) the attacker's team index
       * `attacker_life` - (only for `death`) the attacker's unique spawn index
       * `attacker_weapon` - (only for `death`) the attacker's weapon
       * `attacker_weapon_class` - (only for `death`) the attacker's weapon class (`ar`, `smg`, ...)
       * `attacker_pos` - (only for `death`) the attacker's location in x,y,z (in game units)
       * `kill_distance` - (only for `death`) the distance of the kill (in game units)
       * `means_of_death` - (only for `death`) the kind of kill


## Missing Data

 * `evented-1502548557-A10D2B1C-1377-11D3-2AD6-0CFE454272F2.json` - hardware failure during CWL Champs 2017 resulted in partial data loss for this game.  The failure occured with Envyus leading 4-0, resulting in all events from the first 4 rounds to be lost.  Basic stats (`kills`, `deaths`, `firstblood`, `defuses`, ...) were recovered manually via video replay.
