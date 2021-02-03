Role Name
=========

anki

Installs anki

Uses the package manager to install xdg-utils and enough tooling to run make.
The anki tarball is downloaded, expanded and make is used to install it.

Requirements
------------

None.

Role Variables
--------------

anki_version (currently 2.1.20)

Dependencies
------------

None.

Example Playbook
----------------

    - hosts: all
      roles:
         - role: anki

License
-------

Apache License v2.0

Author Information
------------------

antonio@acarlini.com
