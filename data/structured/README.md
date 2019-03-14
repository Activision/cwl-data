# The Structured Data

Structured data is provided as nested json per game.  Most importantly, the data contains individual intra-game events such as spawns and deaths.


## Samples

Here are a few sample structured data files:

 * 2017 - CWL Champs 2017, Optic Gaming vs Team Envyus, Grand Finals:
    * `hp` - [structured-1502655504-A23F8504-146F-11D3-6C6E-0CFE454272F2.json](https://github.com/Activision/cwl-data/blob/master/data/structured/samples/structured-1502655504-A23F8504-146F-11D3-6C6E-0CFE454272F2.json)
    * `snd` - [structured-1502656269-A850EC88-1471-11D3-6C6E-0CFE454272F2.json](https://github.com/Activision/cwl-data/blob/master/data/structured/samples/structured-1502656269-A850EC88-1471-11D3-6C6E-0CFE454272F2.json)
    * `upl` - [structured-1502657302-F28A9CF2-1473-11D3-6C6E-0CFE454272F2.json](https://github.com/Activision/cwl-data/blob/master/data/structured/samples/structured-1502657302-F28A9CF2-1473-11D3-6C6E-0CFE454272F2.json)
 * 2018 - CWL Dallas 2018, Optic Gaming vs Team Kaliber, Finals:
    * `hp` - [structured-1512958291-be650c82-3e4c-5013-a325-b872e52d6347.json](https://github.com/Activision/cwl-data/blob/master/data/structured/samples/structured-1512958291-be650c82-3e4c-5013-a325-b872e52d6347.json)
    * `snd` - [structured-1512959445-5dbb69ba-3fa7-5bce-8266-8cbf46f1dabd.json](https://github.com/Activision/cwl-data/blob/master/data/structured/samples/structured-1512959445-5dbb69ba-3fa7-5bce-8266-8cbf46f1dabd.json)
    * `ctf` - [structured-1512960410-f77faded-71d4-5b9a-ab0d-1ea3ea546ee2.json](https://github.com/Activision/cwl-data/blob/master/data/structured/samples/structured-1512960410-f77faded-71d4-5b9a-ab0d-1ea3ea546ee2.json)


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
    * `score` - the team score
    * `is_victor` - is this team the winner? (`true` if they won, otherwise `false`)
    * `round_scores` - the list of team score in each round (or hill rotation if `hp`)
    * `side` - the side (`home` or `away`)
 * `players` - the list of players
    * see [The Stats](https://github.com/Activision/cwl-data/tree/master/data#the-stats)...player stats are identical to the tabular stats, _mostly_
 * `events` - the list of intra-game events
    * `type` - the type of event (`roundstart`, `roundend`, `spawn`, `death`)
    * `time_ms` - the relative time from match start of this event (somewhat confusingly games don't always _begin_ exactly at match start)
    * `round` - the round of this event,
    * `round_time_ms` - the relative time from round start of this event
    * `data` - nested metadata for this event, depends on event `type`
       * `score1` - (only for `roundend`) the score at the end of the round for team 1
       * `score2` - (only for `roundend`) the score at the end of the round for team 2
       * `id` - (for `spawn` and `death`) the player
       * `life` - (for `spawn` and `death`) the unique spawn index
       * `pos` - (for `spawn` and `death`) the player's location in x,y (in pixels)
       * `attacker` - (only for `death`)
          * `id` - the attacker
          * `life` - the attacker's unique spawn index
          * `pos` - the attacker's location in x,y (in pixels)
          * `weapon` - the attacker's primary weapon
          * `kill_distance` - the distance of the kill (in pixels)
          * `means_of_death` - the kind of kill


## Missing Data

See [Missing Data](https://github.com/Activision/cwl-data/tree/master/data#missing-data)...in _most_ cases, basic stats are manually recovered using video replay, but *all* intra-game events are lost.
