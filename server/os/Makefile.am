INCLUDES = -I$(top_builddir)/include -I$(top_srcdir)/include

noinst_LTLIBRARIES = libos.la

if OS_POSIX
libos_la_SOURCES = posix.c \
		    posix_signals.c \
		    posix_commandline.c
##libos_la_LIBADD = posix.lo \
##		  posix_signals.lo \
##		  posix_commandline.lo
##libos_la_DEPENDENCIES = posix.lo \
##			posix_signals.lo \
##			posix_commandline.lo
endif

if OS_WIN32
libos_la_SOURCES = mingw.c \
		    mingw_commandline.c
##libos_la_LIBADD = mingw.lo \
##		    mingw_commandline.lo
##libos_la_DEPENDENCIES = mingw.lo \
##			 mingw_commandline.lo
endif

if OS_UCLINUX
libos_la_SOURCES = uclinux.c
##libos_la_LIBADD = uclinux.lo
##libos_la_DEPENDENCIES = uclinux.lo
endif

##libos_la_SOURCES = \
##	$(OS)

EXTRA_libos_la_SOURCES = \
	posix.c			\
	uclinux.c		\
	posix_signals.c		\
	posix_commandline.c


libos_la_LIBADD       = $(OS:%.c=%.lo)
libos_la_DEPENDENCIES = $(OS:%.c=%.lo)
