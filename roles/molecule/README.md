Role Name
=========

molecule

Installs molecule (and ansible) in a python venv for the  specified user

Requirements
------------

None.

Role Variables
--------------

user_account - the user for which to install molecule

Dependencies
------------

None.

Installed Packages
------------------

Python packages installed in the virtual environment:

- `molecule`
- `ansible`
- `python3-pip`

Example Playbook
----------------

    - hosts: all
      roles:
         - role: molecule

License
-------

Apache License v2.0

Author Information
------------------

antonio@acarlini.com
