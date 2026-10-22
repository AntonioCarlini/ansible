Role Name
=========

home_common

Installs those items that are common to all my home systems.

Also performs the following:
* Sets the timezone
* Blocks root login via SSH
* Configures `sudo` for the specified account
* Fixes the locale


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

- `dnf-plugins-core` (only on CentOS)
- `epel-release` (only on CentOS)
- `locales` (only for debian-based OSes)
- `munin-node`
- `nano`
- `perl`
- `openssh-server`
- `tzdata` (only for debian-based OSes)

Example Playbook
----------------

    - hosts: all
      roles:
         - role: home_common

License
-------

Apache License v2.0

Author Information
------------------

antonio@acarlini.com
