# OpenArena Gamepack

## Overview
This repo hosts the GPLv2 gamepack for OpenArena. The intention is to create a fully-GPLv2'd gamepack for any Radiant distributions. Expect files to be changed and deleted as the gamepack is being maintained, as this gamepack is not only a fetch repo but also a maintenance one, trying to fix shader errors in the editor, add missing key shaders (for example, the Alpha shaders for terrains) and missing key images (0% Alpha... 100% Alpha).

## Content
There are two gamepacks: one for OA 0.8.8 and another for the latest SVN revision. In the future, an OA3 pack will also be included.

The gamepacks contain, in addition to the required stuff:
* OA 0.8.8/SVN r951 mapmodels
* OA 0.8.8/SVN r951 world sounds
* OA 0.8.8/SVN r951 shaders, some of them modified.
* Custom textures made for the editor.
* Full common.shader support, complete with the missing shaders, which now enables mappers to do OA terrains. Yay!
* Fully generated entities.ent and entities.def for both XML and regular versions of the NetRadiant editors.

## Sources
The sources for these packs can be found in the following locations:

* http://openarena.ws/svn (Shaders and most textures except.)
* https://github.com/NeonKnightOA/oaassets/sources
* https://github.com/NeonKnightOA/oashaders/sources
