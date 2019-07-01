# OpenArena Gamepack

## Overview
This repo hosts the GPLv2 gamepack for OpenArena. The intention is to create a fully-GPLv2'd gamepack for any Radiant distributions. Expect files to be changed and deleted as the gamepack is being maintained, as this gamepack is not only a fetch repo but also a maintenance one, trying to fix shader errors in the editor, add missing key shaders (for example, the Alpha shaders for terrains) and missing key images (0% Alpha... 100% Alpha).

## Content
This gamepack contains definition files for OA 0.8.8 as well as the newer entities used in the future OA3.

The gamepacks contain, in addition to the required stuff:
* OA 0.8.8 shaders, some of them modified.
* Custom textures made for the editor.
* Full common.shader support, complete with the missing shaders, which now enables OA mappers to do terrains. Yay!
* Fully generated entities.ent and entities.def for both XML and regular versions of the NetRadiant editors.

A separate repository located [here](https://github.com/neonknightoa/oagamepack-assets) includes the following for OA 0.8.8 mapping:
* OA 0.8.8 mapmodels
* OA 0.8.8 map sources
* OA 0.8.8 world sounds
* OA Community Mappack Volume 1 mapmodels
* OA Community Mappack Volume 1 map sources
* OA Community Mappack Volume 1 world sounds

## Sources
The sources for these packs can be found in the following locations:

* http://openarena.ws/svn (Shaders and most textures except.)
* https://github.com/NeonKnightOA/oaassets/sources
* https://github.com/NeonKnightOA/oashaders/sources
