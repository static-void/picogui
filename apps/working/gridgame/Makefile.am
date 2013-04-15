bin_PROGRAMS = gridgame
gridgame_SOURCES = gridgame.c ataxx.c overflow.c
pkgdata_DATA = checkers.th overflow.th

SUFFIXES = .th .ths .thp

%.ths: %.thp
	$(CPP) -x c -P -C -nostdinc -DTHEMESOURCE \
	    -include $(srcdir)/gridth.h -o $@ $<

%.th: %.ths
	themec $<

AM_LDFLAGS = @PICOGUI_LDFLAGS@
LDADD = @PICOGUI_LIBS@

AM_CFLAGS = @CFLAGS@ @PICOGUI_CFLAGS@
