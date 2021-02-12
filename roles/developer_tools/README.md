Role Name
=========

developer_tools

Installs those tools required for development.

Some tools (such as rust and nix) only make sense in a user context, therefore the variable 'user_account' will normally be required.

Requirements
------------

'user_account' must be specified unless 'system_only' is true.

Role Variables
--------------

user_account: the user for which the development tools are being installed.

system_only: if true then no user account is set up and only system-wide tools are installed.

Dependencies
------------

None.

Example Playbook
----------------

    - hosts: all
      roles:
         - role: developer_tools

License
-------

Apache License v2.0

Author Information
------------------

antonio@acarlini.com
