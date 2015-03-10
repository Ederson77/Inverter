from distutils.core import setup
import py2exe
setup(console=['inverter.py'])

from distutils.core import setup
import py2exe
import os, sys, cairo, pango, pangocairo, atk, gobject, gio

# Find GTK+ installation path
__import__('gtk')
m = sys.modules['gtk']
gtk_base_path = m.__path__[0]

setup(
    name = 'inverter',
    description = '',
    version = '0.1',

    windows = [
                  {
                      'script': 'inverter.py',
                  }
              ],

	options = {
                  'py2exe': {
                      'packages':'encodings',
                      # Optionally omit gio, gtk.keysyms, and/or rsvg if you're not using them
                      'includes': 'cairo, pango, pangocairo, atk, gobject, gio, gtk.keysyms',
                  }
              },

    data_files=[
                   'inverter.glade',
               ]
)