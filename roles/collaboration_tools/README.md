Role Name
=========

Installs those tools most often required for collaboration with other developers.

The tools are:
* Skype
* Slack
* Zoom

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
