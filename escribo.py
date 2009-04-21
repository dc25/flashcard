#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2007 by Akkana Peck.
# This program is free software -- please share it under the terms
# of the GNU Public License.

import pygtk
pygtk.require('2.0')
import gtk, gobject

class EscriboButtons:
    # Our callback.
    # The data passed to this method is printed to stdout
    def callback(self, widget, data=None):
        self.primary.set_text(data)
        self.clipboard.set_text(data)

    # This callback quits the program
    def delete_event(self, widget, event, data=None):
        gtk.main_quit()
        return False

    def AddButton(self, str, vbox) :
        button = gtk.Button(str)
        button.connect("clicked", self.callback, str)
        vbox.pack_start(button, True, True, 2)
        button.show()

    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)

        self.window.set_title("Toggle Button")

        # Set a handler for delete_event
        self.window.connect("delete_event", self.delete_event)

        # Sets the border width around the buttons
        self.window.set_border_width(10)

        # Create a vertical box
        vbox = gtk.VBox(True, 2)
        self.window.add(vbox)

        # Add the buttons: add any additional characters you need here.
        self.AddButton("á", vbox)
        self.AddButton("é", vbox)
        self.AddButton("í", vbox)
        self.AddButton("ó", vbox)
        self.AddButton("ñ", vbox)
        self.AddButton("ú", vbox)
        self.AddButton("Á", vbox)
        self.AddButton("É", vbox)
        self.AddButton("Í", vbox)
        self.AddButton("Ó", vbox)
        self.AddButton("Ú", vbox)
        self.AddButton("Ñ", vbox)
        self.AddButton("¿", vbox)
        self.AddButton("¡", vbox)

        # End with a "Quit" button, which will exit:
        button = gtk.Button("Quit")
        button.connect("clicked", lambda wid: gtk.main_quit())
        vbox.pack_start(button, True, True, 2)
        button.show()

        vbox.show()
        self.window.show()

        # Now initialize the tricky undocumented clipboard stuff:
        self.primary = gtk.clipboard_get(gtk.gdk.SELECTION_PRIMARY)
        self.clipboard = gtk.clipboard_get(gtk.gdk.SELECTION_CLIPBOARD)

def main():
    gtk.main()
    return 0       

if __name__ == "__main__":
    EscriboButtons()
    main()
