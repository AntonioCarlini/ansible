Role Name
=========

This role installs ImageMagick and adjusts it to allow conversion to PDF to succeed.

The default install of ImageMagick prohibits conversion to PDF as, when used with arbitrary input, this can represent a security risk. This makes the convert command useless for converting other other graphics formats to PDF using the command line interactively. This is still true in mageMagick 6.9.10-23, so this script allows that to be overriden in those cases when the risk is deemed acceptable by the user.

This role is not incorporated into any of the otehr roles that install imagemagick so as not to inadvertently introduce a potential risk without deliberate action.

Requirements
------------

None

Role Variables
--------------

None

Dependencies
------------

None

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - role: imagemagick-fixup

License
-------

Apache License v2.0

Author Information
------------------

antonio@acarlini.com
