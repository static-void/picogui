INCLUDES = -I$(top_builddir)/include -I$(top_srcdir)/include

noinst_LTLIBRARIES = libwidget.la

libwidget_la_SOURCES = \
    widget.c \
    widget_table.c

if WIDGET_BACKGROUND
libwidget_la_SOURCES += background.c
endif
if WIDGET_BOX
libwidget_la_SOURCES += box.c 
endif
if WIDGET_BUTTON
libwidget_la_SOURCES += button.c 
endif
if WIDGET_CHECKBOX
libwidget_la_SOURCES += checkbox.c 
endif
if WIDGET_FLATBUTTON
libwidget_la_SOURCES += flatbutton.c 
endif
if WIDGET_LABEL
libwidget_la_SOURCES += label.c 
endif
if WIDGET_LISTITEM
libwidget_la_SOURCES += listitem.c
endif
if WIDGET_MENUITEM
libwidget_la_SOURCES += menuitem.c
endif
if WIDGET_RADIOBUTTON
libwidget_la_SOURCES += radiobutton.c 
endif
if WIDGET_SUBMENUITEM
libwidget_la_SOURCES += submenuitem.c 
endif
if WIDGET_CANVAS
libwidget_la_SOURCES += canvas.c
endif
if WIDGET_DIALOGBOX
libwidget_la_SOURCES += dialogbox.c
endif
if WIDGET_MESSAGEDIALOG
libwidget_la_SOURCES += messagedialog.c
endif
if WIDGET_INDICATOR
libwidget_la_SOURCES += indicator.c
endif
if WIDGET_MANAGEDWINDOW
libwidget_la_SOURCES += managedwindow.c
endif
if WIDGET_PANELBAR
libwidget_la_SOURCES += panelbar.c
endif
if WIDGET_PANEL
libwidget_la_SOURCES += panel.c
endif
if WIDGET_POPUP
libwidget_la_SOURCES += popup.c
endif
if WIDGET_SCROLL
libwidget_la_SOURCES += scroll.c
endif
if WIDGET_SCROLLBOX
libwidget_la_SOURCES += scrollbox.c
endif
if WIDGET_SIMPLEMENU
libwidget_la_SOURCES += simplemenu.c
endif
if WIDGET_TABPAGE
libwidget_la_SOURCES += tabpage.c 
endif
if WIDGET_TERMINAL
libwidget_la_SOURCES += terminal_frontend.c \
			terminal_vt102.c \
			terminal_textgrid.c
endif
if WIDGET_TEXTBOX
libwidget_la_SOURCES += textbox_frontend.c \
			textbox_document.c \
			textbox_paragraph.c \
			pgstr_textbuffers.c
endif
if WIDGET_FIELD
libwidget_la_SOURCES += field.c
endif
if WIDGET_TEXTEDIT
libwidget_la_SOURCES += textedit_frontend.c \
			textedit_llist.c \
			textedit_logical.c
endif
if WIDGET_TOOLBAR
libwidget_la_SOURCES += toolbar.c
endif


EXTRA_libwidget_la_SOURCES = \
    terminal_frontend.c \
    terminal_textgrid.c \
    terminal_vt102.c \
    canvas.c \
    textbox_frontend.c \
    textbox_document.c \
    textbox_paragraph.c \
    pgstr_textbuffers.c \
    field.c \
    panel.c \
    textedit_frontend.c \
    textedit_logical.c \
    textedit_llist.c \
    managedwindow.c \
    submenuitem.c \
    indicator.c \
    label.c \
    toolbar.c \
    scroll.c \
    button.c \
    popup.c \
    box.c \
    background.c \
    menuitem.c \
    checkbox.c \
    flatbutton.c \
    listitem.c \
    radiobutton.c \
    panelbar.c \
    simplemenu.c \
    dialogbox.c \
    messagedialog.c \
    scrollbox.c \
    tabpage.c

libwidget_la_LIBADD       = $(WIDGET:%.c=%.lo)
libwidget_la_DEPENDENCIES = $(WIDGET:%.c=%.lo)
