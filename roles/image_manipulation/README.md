Role Name
=========

image_manipulation

Installs those tools required for PDF/image manipulation.

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

      - gcc
      - imagemagick
      - mupdf-tools
      - pdfshuffler
      - php
      - php-common
      - php-imagick
      - rawtherapee


Example Playbook
----------------

    - hosts: all
      roles:
         - role: image_manipulation

Test Matrix
-----------

Tested against:

- Ubuntu 16.04

License
-------

Apache License v2.0

Author Information
------------------

antonio@acarlini.com
