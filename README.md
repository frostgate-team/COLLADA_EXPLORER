# COLLADA_EXPLORER

This is a script for getting textures referenced by .dae files in HPL Engine games. 
Note, that this tool are working in pair with [HPMParser](https://github.com/frostgate-team/HPMParser).
You need to use HPMParser before you start working with COLLADA_EXPLORER because it uses mesh lists generated by HPMParser.

# USAGE OF COLLADA_EXPLORER

- As stated earlier, you need to use [HPMParser](https://github.com/frostgate-team/HPMParser) at first to obtain map mesh lists.
- Open the config.ini file in the COLLADA EXPLORER folder and customize it for your system.
  * "working_path" is the path to game directory. For example: `G:/steam games/SteamApps/common/Amnesia The Dark Descent/`
  * "meshlist_path" is the path to mesh lists generated by HPMParser tool. For example: `G:/repo/HPMParser/out/`

Obtained textures paths will shown in `out/matlist.txt`