Role Name
=========

ploticus

Installs ploticus using the package manager. If that fails, it builds ploticus from source

Requirements
------------

None.

Role Variables
--------------

None.

Dependencies
------------

None.

Installed Packages
------------------

- `ploticusx`
- `build-essential` (if need to build from source on a debian-based OS)
- `gcc` (if need to build from source)
- `gd-devel` (if need to build from source on a RedHat-based OS)
- `libgd-dev` (if need to build from source on a debian-based OS)
- `libx11-dev` (if need to build from source)
- `make` (if need to build from source on a RedHat-based OS)
- `zlib-devel` (if need to build from source on a RedHat-based OS)
- `zlib1g-dev` (if need to build from source on a debian-based OS)

Example Playbook
----------------

    - hosts: all
      roles:
         - role: ploticus

License
-------

Apache License v2.0

Author Information
------------------

antonio@acarlini.com
