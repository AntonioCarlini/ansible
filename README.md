
This repository holds a number of ansible scripts that I've found useful for configuring various systems.


### Preparation

The scrips assume that there is a specific user (`ansibleadmin`) available on the host that is to be managed and that the local user running the script can log in over SSH as that user without entering a password. The `prepare-ansible-target` script is used to create this environment on the host to be managed. When this script is used, you have to specify an account with sudo capability on the managed host. To run  this script against a host with IP address **HOST-IP** that has a sudo-capable account **USER**, do this:

'ansible-playbook prepare-ansible-target -i **HOST-IP**, -u **USER** --ask-pass --ask-become-pass`

Note that the **HOST-IP** *must* be followed by a comma.


### Available Roles and Playbooks

This table lists the available roles and the platforms on which they have been tested.


|                                                              |                |          |       | Linux Mint | Linux Mint | Ubuntu | Ubuntu | Ubuntu | Debian | Debian | CentOS | CentOS |
|--------------------------------------------------------------|----------------|----------|-------|------------|------------|--------|--------|--------|--------|--------|--------|--------|
| Name                                                         | Role/ Playbook | Molecule | Tests |    20.1    |    19.1    | 20.04  | 18.04  | 16.04  |   10   |    9   |    8   |    7   |
|--------------------------------------------------------------|----------------|----------|-------|------------|------------|--------|--------|--------|--------|--------|--------|--------|
| [anki](roles/anki/README.md)                                 |      Role      |     Y    |   Y   |      Y     |      Y     |    Y   |    Y   |    Y   |    Y   |    Y   |    Y   |    Y   |
| [collaboration_tools](roles/collaboration_tools/README.md)   |      Role      |     Y    |   Y   |      Y     |      Y     |    Y   |    Y   |    N   |    Y   |    Y   |    N   |    N   |
| [developer_tools](roles/developer_tools/README.md)           |      Role      |     Y    |       |      Y     |      Y     |    Y   |    Y   |    Y   |    Y   |    Y   |    Y   |    Y   |
| [document-tools](roles/document-tools/README.md)             |                |          |       |            |            |        |        |        |        |        |        |        |
| [home_common](roles/home_common?README.md)                   |      Role      |     Y    |       |      Y     |      Y     |    Y   |    Y   |    Y   |    Y   |    Y   |    Y   |    Y   |
| [home-station](roles/home-station/REDAME.md)                 |                |          |       |            |            |        |        |        |        |        |        |        |
| [imagemagick-fixup](roles/imagemagick-fixup/README.md)       |      Role      |     Y    |   Y   |      Y     |      Y     |    Y   |    Y   |    Y   |    Y   |    Y   |    Y   |    Y   |
| [image_manipulation](roles/image_manipulation/README.md)     |      Role      |     Y    |       |      Y     |      Y     |    Y   |    Y   |    Y   |    Y   |    Y   |    N   |    N   |
| [japanese](roles/japanese/README.md)                         |      Role      |     Y    |       |      Y     |      Y     |    Y   |    Y   |    Y   |    Y   |    Y   |    N   |    N   |
| [mediawiki](roles/mediawiki/README.md)                       |                |          |       |            |            |        |        |        |        |        |        |        |
| [mysql](roles/mysql/README.md)                               |                |          |       |            |            |        |        |        |        |        |        |        |
| [nix](roles/nix/README.md)                                   |      Role      |     Y    |       |      Y     |      Y     |    Y   |    Y   |    Y   |    Y   |    Y   |    Y   |    Y   |
| [ntp_client](roles/ntp_client/README.md)                     |      Role      |     Y    |       |      N     |      N     |    Y   |    Y   |    Y   |    Y   |    Y   |    N   |    N   |
| [php](roles/php/README.md)                                   |      Role      |     Y    |       |      Y     |      Y     |    Y   |    Y   |    Y   |    Y   |    Y   |    Y   |    Y   |
| [prepare-ansible-target](prepare-ansible-target.README.md)   |    Playbook    |          |       |            |            |        |        |        |        |        |        |        |
| [rust](roles/rust/README.md)                                 |      Role      |     Y    |       |      Y     |      Y     |    Y   |    Y   |    Y   |    Y   |    Y   |    Y   |    Y   |
| [utilities](roles/utilities/README.md)                       |      Role      |     Y    |       |      Y     |      Y     |    Y   |    Y   |    Y   |    N   |    N   |    N   |    N   |
| [vagrant](roles/vagrant/README.md)                           |      Role      |     Y    |       |      Y     |      Y     |    Y   |    Y   |    Y   |    Y   |    Y   |    Y   |    Y   |
| [virtualbox](roles/virtualbox/README.md)                     |                |          |       |            |            |        |        |        |        |        |        |        |
| [visual_studio_code](roles/visual_studio_code/README.md)     |      Role      |     Y    |       |      Y     |      Y     |    Y   |    Y   |    Y   |    Y   |    Y   |    Y   |    Y   |
| [vmware-host](roles/vmware-host/README.md)                   |                |          |       |            |            |        |        |        |        |        |        |        |
| [vmware-player](roles/vmware-player/README.md)               |                |          |       |            |            |        |        |        |        |        |        |        |
| [vpn-station](roles/vpn-station/README.md)                   |                |          |       |            |            |        |        |        |        |        |        |        |
| [webserver](roles/webserver/README.md)                       |      Role      |     Y    |       |      Y     |      Y     |    Y   |    Y   |    Y   |    Y   |    Y   |    Y   |    Y   |
| [work-station](roles/work-station/README.md)                 |                |          |       |            |            |        |        |        |        |        |        |        |