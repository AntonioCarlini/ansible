Role Name
=========

webserver

Installs a webserver (currently Apache)

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

- `apache2` (on Debian-based OSes)
- `libapache2-mod-php` (on Debian-based OSes)
- `httpd` (on Redhat-based OSes)
- `mod_php` (on Redhat-based OSes)

Example Playbook
----------------

    - hosts: all
      roles:
         - role: apache

License
-------

Apache License v2.0

Author Information
------------------

antonio@acarlini.com
