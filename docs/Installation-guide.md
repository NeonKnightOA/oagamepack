# Setting up the editor

In order to create and/or edit maps for OpenArena, you need to download not only **the editor itself**, but also **a fresh copy of the game itself**, and **the gamepack** (which, unless you're reading this online, you already have).

For the purposes of this guide, we're using [this version of NetRadiant](https://github.com/garux/netradiant-custom). Also we're going to call **"game folder"** to the folder where the contents of the OA game are located, **"editor folder"** to the folder where the contents related to the editor are located, and **"gamepack folder"** to the folder where the contents related to the OA gamepack are located.

You have two ways of getting a copy of the editor: by downloading the binaries or compiling the source code.

## Binary download

_**Last updated: Jan 5, 2019.** Links may become obsolete as new versions are released._

Go to [this location](https://github.com/Garux/netradiant-custom/releases) and download the stable version of NetRadiant that fits your OS:

* [Linux (64-bit)](https://github.com/Garux/netradiant-custom/releases/download/20181213/netradiant-custom-ubuntu-18-04-x86_64.7z)
* [Windows (32-bit)](https://goo.gl/UyXRUJ)
* [Windows (64-bit)](https://goo.gl/gBQSGC)

Once the download is finished, search for the folder where the binaries are located, and move **everything** from this position onto a temporary folder.

## Source code

The source code for the stable versions of the editor can be obtained from the [Releases section](https://github.com/Garux/netradiant-custom/releases):

* [.zip](https://github.com/Garux/netradiant-custom/archive/20181213.zip)
* [.tar.gz](https://github.com/Garux/netradiant-custom/archive/20181213.tar.gz)

Alternatively, if you want to obtain the latest update, you can obtain a copy of the latest commit and compile it by yourself. [In this page](https://github.com/garux/netradiant-custom) go to **Clone or Download** and select **Download Zip**.

The _make_ script checks for the existence of the following compilation tools and packages:  _"bash"_ (or another shell), _"coreutils"_, _"sed"_, _"findutils"_, _"diff"_, _"gcc"_, _"g++"_, _"binutils"_, _"pkg-config"_, _"unzip"_, _"git-core"_, _"svn"_, _"wget"_ and _"libc6"_.

The required libraries for the compilation phase are _"libjpeg8-dev"_, _"libglib2.0-dev"_, _"libxml2-dev"_, _"libpng12-dev"_, _"mesa-common-dev"_ (or another OpenGL library), _"libgtk2.0-dev"_, _"libpango1.0-dev"_, _"libgtkglext1-dev"_, _"libc6-dev"_ and _"zlib1g-dev"_.

For the compilation itself you can use an IDE or run the **make** script directly. Regardless of the used method, you should be able to obtain a folder called "Install" after this phase. This folder contains the binaries and folder structure required in order to run the editor.

## The game itself

This step is critical: you don't want to pollute your **gaming** OA folder, and (if you use Linux) you don't want to deal with scattered files. So we're downloading a fresh copy of the game, instead. Head to [the official website's Download section](http://openarena.ws/download.php) and get **the latest full release** (which, as of this writing, is 0.8.8, in this case download **both** the full release and the patch).

## Gamepack

You can download the gamepack for OpenArena from [this location](https://github.com/NeonKnightOA/oagamepack/). Go to **Clone or Download** and select **Download Zip**.

## Installation

First of all, unzip the contents of the full OA 0.8.8 game into a folder, and then unzip the contents of the 0.8.8 patch inside of it. This is the **game folder**, and it should have the following structure (if there are extra files, ignore them):

```
baseoa/*
missionpack/*
OpenArena.app/*
OpenArena 0.8.8 r28.app/*
libogg-0.dll
libvorbis-0.dll
libvorbisfile-3.dll
oa_ded.exe
oa_ded.i386
oa_ded.x86_64
openarena.exe
openarena.i386
openarena.x86_64
openarena_deprecated.exe
SDL.dll
```

Now, **inside the game folder**, create another folder called **"NetRadiant"**, and move the generated contents from either the unzipped folder or the compiled folder here. Finally, **inside of the editor folder**, unzip the folders **games** and **oa.game** from the gamepack ZIP. This will be the **editor folder**, and it should have the following structure:

```
bitmaps/*
docs/*
games/*
gl/*
modules/*
oa.game/*
plugins/*
<several .game directories>/
.gtkrc-2.0.radiant
.gtkrc-2.0.win
global.xlink
q2map.x86_64
q3data.qdt
q3data.x86_64
q3map2.x86_64
qdata3.x86_64
quake3.exclude
radiant.x86_64
RADIANT_MAJOR
RADIANT_MINOR
```

Therefore, the resulting overall structure must look, more or less, like this:

```
baseoa/*
missionpack/*
NetRadiant/
	bitmaps/*
	docs/*
	games/*
	gl/*
	modules/*
	oa.game/*
	plugins/*
	<several .game directories>/
	.gtkrc-2.0.radiant
	.gtkrc-2.0.win
	global.xlink
	q2map.x86_64
	q3data.qdt
	q3data.x86_64
	q3map2.x86_64
	qdata3.x86_64
	quake3.exclude
	radiant.x86_64
	RADIANT_MAJOR
	RADIANT_MINOR
OpenArena.app/*
OpenArena 0.8.8 r28.app/*
libogg-0.dll
libvorbis-0.dll
libvorbisfile-3.dll
oa_ded.exe
oa_ded.i386
oa_ded.x86_64
openarena.exe
openarena.i386
openarena.x86_64
openarena_deprecated.exe
SDL.dll
```

Run the game and the editor for the first time so the proper files can be generated for edition.

If you have problems with seeing certain shaders in the editor, copy the file **game folder/editor folder/oa.game/baseoa/scripts/default_shaderlist.txt** to **game folder/baseoa/scripts/**, overwriting it.