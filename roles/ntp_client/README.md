Role Name
=========

ntp_client

Installs an NTP client and some related tools

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

- `ntp`
- `ntpstat`

Example Playbook
----------------

    - hosts: all
      roles:
         - role: ntp_client

License
-------

Apache License v2.0

Author Information
------------------

antonio@acarlini.com
