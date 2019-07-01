// 12-12-06 removed redundant nodrop
// 12-23-06 fixed the b0rked invisible shader
// 01-25-07 removed redundant clip + added nodrawnonsolid, clusterportal
// 01-27-07 moved portal from clown.shader to here
// 01-31-07 added mirror shader doesnt work, gave other shaders transparency in map editor.-kit89 
// 02-14-07 added timportal + mirror1, mirror 2, terrain, terrain 2, metalclip 
// 02-27-07 added botclip, missleclip, remapped certain mirrors to point to invisible.tga
// 22/11/18 added remaining shaders.

textures/common/areaportal
{
	qer_trans 0.50
	qer_nocarve
	surfaceparm nodraw
	surfaceparm nolightmap
	surfaceparm nonsolid
	surfaceparm structural
	surfaceparm trans
	surfaceparm nomarks
	surfaceparm areaportal
}
textures/common/caulk
{
	surfaceparm nodraw
	surfaceparm nomarks
        surfaceparm nolightmap
}


textures/common/clip
{
	qer_trans 0.50
	qer_nocarve
	surfaceparm nolightmap
	surfaceparm nomarks
	surfaceparm nodraw
	surfaceparm nonsolid
	surfaceparm playerclip
	surfaceparm noimpact
	surfaceparm trans
}

//separates areas into smaller ones for botplay
textures/common/clusterportal
{
	qer_trans 0.50
	qer_nocarve
	surfaceparm nodraw
	surfaceparm nolightmap
	surfaceparm nonsolid
	surfaceparm trans
	surfaceparm nomarks
	surfaceparm clusterportal
}

textures/common/cushion
{
	qer_nocarve
	qer_trans 0.50
	surfaceparm nodraw
	surfaceparm nolightmap
	surfaceparm nomarks
	surfaceparm nodamage
	surfaceparm trans
}

//need this or maps FTBFS
//for the idiot bots out there use instead of botclip!!!!
textures/common/donotenter
{
	qer_trans 0.50
	qer_nocarve
	surfaceparm nodraw
	surfaceparm nonsolid
	surfaceparm trans
	surfaceparm nomarks
	surfaceparm donotenter
}

// Someday someone will find a use for this.
textures/common/energypad
{
	surfaceparm nolightmap
	cull twosided
	// add a shader stage here.
}
textures/common/full_clip
{
	qer_trans 0.50
	qer_nocarve
	surfaceparm nodraw
	surfaceparm playerclip
}
//aids in VIS compiles
textures/common/hint
{
	surfaceparm hint
	surfaceparm nodraw
	surfaceparm nonsolid
	surfaceparm structural
	surfaceparm trans
	surfaceparm noimpact
}

// Aids in VIS compiles, according to someone acts like a hint but doesn't create portals
// beyond local structures.
textures/common/hintlocal
{
	surfaceparm nodraw
	surfaceparm nonsolid
	surfaceparm structural
	surfaceparm trans
	surfaceparm noimpact
}

textures/common/invisible
{
	surfaceparm nolightmap			
        {
		map textures/common/invisible.tga
		alphaFunc GE128
		depthWrite
		rgbGen vertex
	}
        
}

//nicked from nexuiz for backwards compat 
textures/common/mirror1
{
	surfaceparm nolightmap
	portal
  	{
		map textures/common/invisible.tga
		blendfunc GL_ONE GL_ONE_MINUS_SRC_ALPHA
		depthWrite
	}
}

//nicked from nexuiz w/added turb. for backwards compat 
textures/common/mirror2
{
	surfaceparm nolightmap
	portal
	{
		map textures/common/invisible.tga
		blendfunc GL_ONE GL_ONE_MINUS_SRC_ALPHA
		depthWrite
	}
        {
               map textures/sfx/mirror.tga
	       tcMod turb 0 0.25 0 0.05
	       blendFunc GL_ZERO GL_ONE_MINUS_SRC_COLOR
        }

}

textures/common/missileclip
{
	qer_trans 0.50
	qer_nocarve
	surfaceparm nodamage
	surfaceparm nomarks
	surfaceparm nodraw
	surfaceparm playerclip
	surfaceparm trans
}

textures/common/nodraw
{
	qer_trans 0.50
	qer_nocarve
	surfaceparm nodraw
	surfaceparm nolightmap
	surfaceparm nonsolid
	surfaceparm nomarks
	surfaceparm trans
}
//for every stupid q3dm17 remake
textures/common/nodrawnonsolid
{
	qer_trans 0.50
	qer_nocarve
	surfaceparm nonsolid
	surfaceparm nolightmap
	surfaceparm nodraw
}

//use this near the trigger hurts, lava, death fogs, etc.
// to keep weapons and powerups from piling up and bots from suiciding...
textures/common/nodrop
{
	qer_trans 0.50
	qer_nocarve
	surfaceparm 	trans
	surfaceparm	nonsolid
	surfaceparm	nomarks
	surfaceparm     nodrop
	surfaceparm 	nolightmap
	surfaceparm 	nodraw
}
textures/common/noimpact
{
	qer_trans 0.50
	qer_nocarve
	surfaceparm noimpact
}
textures/common/nolightmap
{
	qer_trans 0.50
	qer_nocarve
	surfaceparm nolightmap
}
//for func_ entities
textures/common/origin
{
	qer_nocarve
	surfaceparm nodraw
	surfaceparm nolightmap
	surfaceparm nonsolid
	surfaceparm trans
	surfaceparm origin
}
//can also be used as a mirror
textures/common/portal
{
	surfaceparm nolightmap
	portal
	{
		map textures/common/invisible.tga
		blendfunc GL_ONE GL_ONE_MINUS_SRC_ALPHA
		depthWrite
	}
}

//for an icy effect
textures/common/slick
{
	qer_trans 0.50
	qer_nocarve
	surfaceparm nodraw
	surfaceparm nolightmap
	surfaceparm nomarks
	surfaceparm trans
	surfaceparm slick
}

//nicked from nexuiz
textures/common/terrain
{
	q3map_terrain
	surfaceparm nodraw
        surfaceparm nolightmap
	surfaceparm nomarks
}

//nicked from nexuiz
textures/common/terrain2
{
	q3map_terrain
	surfaceparm dust
	surfaceparm nodraw
	surfaceparm nomarks
	surfaceparm nolightmap
}

textures/common/timportal
{
	surfaceparm nolightmap
	portal
	{
		map textures/common/invisible.tga
		blendfunc GL_ONE GL_ONE_MINUS_SRC_ALPHA
		depthWrite

	}
	{
		map textures/oa_fogs/kc_fogcloud3.jpg
		blendfunc gl_src_alpha gl_one_minus_src_alpha
		alphagen portal 512
		rgbGen identity	
		tcmod rotate .1 
		tcmod scroll .04 .01
	}
}

//general trigger brush for multiple uses.
textures/common/trigger
{
	qer_trans 0.50
	qer_nocarve
	surfaceparm nodraw
}
//to keep certain textures from being shot up
textures/common/weapclip
{
	qer_trans 0.50
	qer_nocarve
	surfaceparm nodraw
	surfaceparm nolightmap
	surfaceparm trans
	surfaceparm nomarks
}

//nicked from nexuiz
textures/common/metalclip
{
	qer_trans 0.50
	qer_nocarve
	surfaceparm nodraw
	surfaceparm nolightmap
	surfaceparm nonsolid
	surfaceparm trans
	surfaceparm nomarks
	surfaceparm noimpact
	surfaceparm playerclip
	surfaceparm metalsteps
}

// simplifies world geometry for bots
// use for smoothing highly detailed walls, floors and ceilings.
textures/common/botclip
{
	qer_trans 0.50
	qer_nocarve
	surfaceparm nodraw
	surfaceparm nolightmap
	surfaceparm nonsolid
	surfaceparm trans
	surfaceparm nomarks
	surfaceparm noimpact
	surfaceparm botclip
}
// How does this work: 
textures/common/lightgrid
{
	qer_trans 0.50
	qer_nocarve
	surfaceparm nodraw
	surfaceparm nolightmap
	surfaceparm nonsolid
	surfaceparm detail
	surfaceparm nomarks
	surfaceparm trans
	surfaceparm lightgrid
}
// Hint-like shader that suppresses portals.
textures/common/antiportal
{
	qer_trans 0.50
	qer_nocarve
	surfaceparm nodraw
	surfaceparm nonsolid
	surfaceparm structural
	surfaceparm trans
	surfaceparm antiportal
}

//Added for Mirrors
textures/common/mirror
{
	portal
	q3map_nolightmap
    {
        map textures/common/invisible.tga
        blendFunc GL_ONE GL_ONE_MINUS_SRC_ALPHA
        depthWrite
    }
}

// Q2-like hint: doesn't split the BSP, so should be used in hint brushes
// in the faces that shouldn't cut the BSP tree.
textures/common/skip
{
	qer_trans 0.50
	qer_nocarve
	surfaceparm nodraw
	surfaceparm noimpact
	surfaceparm nonsolid
	surfaceparm skip
	surfaceparm structural
	surfaceparm trans
}
// Same as skip, allows Radiant to filter both hint and skip.
textures/common/hintskip
{
	qer_trans 0.50
	qer_nocarve
	qer_editorImage textures/common/skip.tga
	surfaceparm nodraw
	surfaceparm noimpact
	surfaceparm nonsolid
	surfaceparm skip
	surfaceparm structural
	surfaceparm trans
}
// Caulk for water: allows water shaders to be used where the water area extends
// Think am_mckinleyish pool entrances.
textures/common/watercaulk
{
	qer_trans 0.50
	qer_nocarve
	surfaceparm nodraw
	surfaceparm nonsolid
	surfaceparm trans
	surfaceparm water
}
// Caulk for lava: same as watercaulk, but for lava pits.
textures/common/lavacaulk
{
	qer_trans 0.50
	qer_nocarve
	surfaceparm nodraw
	surfaceparm nonsolid
	surfaceparm trans
	surfaceparm lava
}
// Caulk for slime: same as watercaulk and lavacaulk, but for slime pits.
textures/common/slimecaulk
{
	qer_trans 0.50
	qer_nocarve
	surfaceparm nodraw
	surfaceparm nonsolid
	surfaceparm trans
	surfaceparm slime
}
// Terrain-specific shaders. With these, we complete the pack.
// Go to simonoc's page for terrain tutorials.
textures/common/alpha_0
{
	qer_trans 0.50
	qer_nocarve
	q3map_alphaMod volume
	q3map_alphaMod scale 0.0
	surfaceparm nodraw
	surfaceparm nonsolid
	surfaceparm trans
}
textures/common/alpha_25
{
	qer_trans 0.50
	qer_nocarve
	q3map_alphaMod volume
	q3map_alphaMod scale 0.25
	surfaceparm nodraw
	surfaceparm nonsolid
	surfaceparm trans
}
textures/common/alpha_50
{
	qer_trans 0.50
	qer_nocarve
	q3map_alphaMod volume
	q3map_alphaMod scale 0.50
	surfaceparm nodraw
	surfaceparm nonsolid
	surfaceparm trans
}
textures/common/alpha_75
{
	qer_trans 0.50
	qer_nocarve
	q3map_alphaMod volume
	q3map_alphaMod scale 0.75
	surfaceparm nodraw
	surfaceparm nonsolid
	surfaceparm trans
}
textures/common/alpha_100
{
	qer_trans 0.50
	qer_nocarve
	q3map_alphaMod volume
	q3map_alphaMod scale 1.0
	surfaceparm nodraw
	surfaceparm nonsolid
	surfaceparm trans
}