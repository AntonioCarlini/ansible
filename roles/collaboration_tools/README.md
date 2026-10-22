Role Name
=========

Installs those tools most often required for collaboration with other developers.

Currently only debain-based systems are supported (so not CentOS 7 or CentOS 8).
Ubuntu 16.04 seems to have problems with Zoom so that is not currently supported either.

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

- `slack`
- `skype`
- `teams`
- `zoom`

Example Playbook
----------------

    - hosts: all
      roles:
         - role: collaboration_tools

License
-------

Apache v2.0

Author Information
------------------

antonio@acarlini.com
