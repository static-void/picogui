bin_PROGRAMS = picomail

picomail_SOURCES = configfile.c imap.c picomail.c tcpclient.c

EXTRA_DIST = picomail.conf

AM_LDFLAGS = @PICOGUI_LDFLAGS@
LDADD = @PICOGUI_LIBS@

AM_CFLAGS = @CFLAGS@ @PICOGUI_CFLAGS@
