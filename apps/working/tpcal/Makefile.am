bin_PROGRAMS = tpcal
tpcal_SOURCES = tpcal.c transform.c
pkgdata_DATA = calth.th

SUFFIXES = .th .ths .thp

%.ths: %.thp
	$(CPP) -x c -P -C -nostdinc -DTHEMESOURCE \
	    -include $(srcdir)/calth.h -o $@ $<

%.th: %.ths
	themec $<

AM_LDFLAGS = @PICOGUI_LDFLAGS@
LDADD = @PICOGUI_LIBS@

AM_CFLAGS = @CFLAGS@ @PICOGUI_CFLAGS@
