SUBDIRS = $(VIDSUBDIRS)

INCLUDES = -I$(top_builddir)/include -I$(top_srcdir)/include $(DRIVER_CFLAGS)

noinst_LTLIBRARIES = libvideo.la

libvideo_la_SOURCES = \
	video_drivers.c

if EZ328
libvideo_la_SOURCES += ez328.c
endif
if EZ328VGA
libvideo_la_SOURCES += ez328vga.c
endif
if SDLFB
libvideo_la_SOURCES += sdlfb.c
endif
if SDLGL
libvideo_la_SOURCES += sdlgl.c
endif
if GLCONTEXT
libvideo_la_SOURCES += glcontext.c
endif
if SVGAFB
libvideo_la_SOURCES += svgafb.c
endif
if NCURSES
libvideo_la_SOURCES += ncurses.c
endif
if NULL
libvideo_la_SOURCES += null.c
endif
if NULLFB
libvideo_la_SOURCES += nullfb.c
endif
if FBDEV
libvideo_la_SOURCES += fbdev.c
endif
if SERIAL40X4
libvideo_la_SOURCES += serial40x4.c
endif
if SCRSHOT
libvideo_la_SOURCES += scrshot.c
endif
if S1D13806
libvideo_la_SOURCES += s1d13806.c
endif
if SED133X
libvideo_la_SOURCES += sed133x.c
endif
if X11
libvideo_la_SOURCES += x11_bitmap.c \
		       x11_window.c \
		       x11_init.c \
		       x11_primitives.c
endif
if MGL2FB
libvideo_la_SOURCES += mgl2fb.c
endif
if VNCSERVER
libvideo_la_SOURCES += vncserver.c \
		       libvncserver/libvncserver.la
endif
if DIRECTFB
libvideo_la_SOURCES += directfb.c
endif

EXTRA_libvideo_la_SOURCES = \
	ez328.c    \
	ez328vga.c \
	fbdev.c    \
	ncurses.c  \
	null.c 	   \
	nullfb.c   \
	sdlfb.c    \
	svgafb.c   \
	serial40x4.c \
	scrshot.c  \
	s1d13806.c \
	x11_init.c \
	x11_window.c \
	x11_bitmap.c \
	x11_primitives.c \
	mgl2fb.c \
	sdlgl.c \
	glcontext.c \
	vncserver.c

libvideo_la_LIBADD       = $(DRIVER:%.c=%.lo)
libvideo_la_DEPENDENCIES = $(DRIVER:%.c=%.lo)


