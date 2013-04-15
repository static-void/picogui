INCLUDES = -I$(top_builddir)/include -I$(top_srcdir)/include

noinst_LTLIBRARIES = libvidbase.la

libvidbase_la_SOURCES = \
	dvbl_bitmap.c   \
	dvbl_color.c	\
	dvbl_effects.c	\
	dvbl_init.c	\
	dvbl_lgop.c	\
	dvbl_sprite.c	\
	dvbl_font.c	\
	font_base.c
##	$(VIDBASE)

if VBL_LINEAR1
libvidbase_la_SOURCES += linear1.c
endif
if VBL_LINEAR2
libvidbase_la_SOURCES += linear2.c
endif
if VBL_LINEAR4
libvidbase_la_SOURCES += linear4.c
endif
if VBL_LINEAR8
libvidbase_la_SOURCES += linear8.c
endif
if VBL_LINEAR16
libvidbase_la_SOURCES += linear16.c
endif
if VBL_LINEAR24
libvidbase_la_SOURCES += linear24.c
endif
if VBL_LINEAR32
libvidbase_la_SOURCES += linear32.c
endif
if FB_YUV16_422_PLANAR
libvidbase_la_SOURCES += yuv16_422_planar.c
endif
if VBL_VGAPLAN4
libvidbase_la_SOURCES += vgaplan4.c
endif
if VBL_SLOWVBL
libvidbase_la_SOURCES += slowvbl.c
endif
if DITHER
libvidbase_la_SOURCES += dvbl_dither.c
endif
if PAL8_VISIBONE2
libvidbase_la_SOURCES += visibone2.c
endif
if ANTIALIAS
libvidbase_la_SOURCES += dvbl_primitives_aa.c
else
libvidbase_la_SOURCES += dvbl_primitives.c
endif
if FONTENGINE_BDF
libvidbase_la_SOURCES += font_bdf.c
endif
if FONTENGINE_FREETYPE
libvidbase_la_SOURCES += font_freetype.c
endif
if FONTENGINE_TEXTMODE
libvidbase_la_SOURCES += font_textmode.c
endif
if FONTENGINE_XFT
libvidbase_la_SOURCES += font_xft.c
endif
if FONTENGINE_FTGL
libvidbase_la_SOURCES += font_ftgl.c
endif
if VBL_GL
libvidbase_la_SOURCES += gl_bitmap.c \
			 gl_camera.c \
			 gl_init.c \
			 gl_primitives.c \
			 gl_util.c \
			 gl_grop.c
endif

EXTRA_libvidbase_la_SOURCES = \
	linear1.c	\
	linear2.c	\
	linear4.c	\
	linear8.c	\
	linear16.c      \
	linear24.c      \
	linear32.c      \
	yuv16_422_planar.c \
	slowvbl.c       \
	dvbl_dither.c   \
	visibone2.c     \
	dvbl_primitives.c \
	dvbl_primitives_aa.c \
	font_bdf.c	\
	font_freetype.c	\
	font_textmode.c	\
	font_xft.c	\
	font_ftgl.c	\
	gl_bitmap.c	\
	gl_camera.c	\
	gl_init.c	\
	gl_primitives.c	\
	gl_util.c	\
	gl_grop.c

noinst_HEADERS = \
	yuv.h

libvidbase_la_LIBADD       = $(VIDBASE:%.c=%.lo)
libvidbase_la_DEPENDENCIES = $(VIDBASE:%.c=%.lo)
