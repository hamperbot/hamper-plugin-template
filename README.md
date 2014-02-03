Hamper Plugin Template
======================

Base template for a simple external Hamper plugin, based on Cookiecutter.

0. Install [Cookiecutter][1].
1. Use Cookiecutter to make a base project:

   ```shell
   $ cd ~/src
   $ cookiecutter https://github.com/mythmon/hamper-plugin-template.git
   ```

   This will ask for information it will use to fill in the template, such as
   the plugin's name, and your name (for the project metadata).

2. Change into the directory that Cookiecutter made, and start hacking. You
   probably want to start by editing (and possible renaming) `mycommand.py` in
   the package directory.

[1]: http://cookiecutter.readthedocs.org/en/latest/installation.html
