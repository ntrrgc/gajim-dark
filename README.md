#Gajim dark theme

This is a dark theme for the Jabber client [Gajim](http://gajim.org/).

It contains a config patch for Gajim, the [elementary Dark](http://satya164.deviantart.com/art/elementary-Dark-GTK3-Theme-244257862) GTK theme and shell scripts to enable it just for Gajim.

#Installation

Run the `./install.py` to patch your Gajim configuration.

    git clone 
    cd gajim-dark
    ./install.py

Just in case anything goes wrong, you have a backup of your config file at '~/.config/gajim/config.bak'.

You should be able to run your newly themed gajim using the provided shell script:

    ./gajim

Finally, symlink it somewhere in your `$PATH` to be able to run it writing only gajim. E.g:

    ln -s "$PWD/gajim" ~/bin/

#Caveats

* The `pop-gtk-theme` script undoes GTK environment variables in order not to make child process (e.g. your browser after you click an HTTP link in a conversation) inherit them. 

  The `install.py` script will add this for you to your config, but it will break if you move this directory.

* The provided `./gajim` script runs `/usr/bin/gajim`. You will need to modify it if you have Gajim installed elsewhere.

* GTK3 gajim is not supported for now.

* MS Windows is not supported for now.
