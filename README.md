# Automation

Automations can help optimize large-scale tasks that are done manually, allowing people to focus on more intellectual tasks, such as planning, project development and process improvements.

The Automation of Identity Management Routines project was developed as part of my Master's Final Work (TFM) and aims to propose the creation of an automated structure to perform these tasks.
Using a structure that relies on Ansible and Jenkins, the idea is to create an environment focused on integration with Active Directory and deliver some playbooks that automate the most common tasks for these teams.

# Documentation

The purpose of this documentation is to support the preparation of the environment. As it is an integration with a Windows environment, some additional customizations are necessary.


# Platforms:
![Ansible](https://img.shields.io/badge/ansible-%231A1918.svg?style=for-the-badge&logo=ansible&logoColor=white)
![Jenkins](https://img.shields.io/badge/jenkins-%232C5263.svg?style=for-the-badge&logo=jenkins&logoColor=white)
![YAML](https://img.shields.io/badge/yaml-%23ffffff.svg?style=for-the-badge&logo=yaml&logoColor=151515)
![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![Debian](https://img.shields.io/badge/Debian-D70A53?style=for-the-badge&logo=debian&logoColor=white)

# Preparation Guide

Automation for Windows environments can be tricky. 
Due to its particularities and Operating System architecture, setting up this environment may require additional time. 
However, the good news is: this is a preparation that is done only once. Then, just develop the playbooks according to your needs and you’re done. I will leave the ones I developed for my project to serve you as a guide.

# Infrastructure Requirements

Putting together the information from the providers, a server with the configuration below can be a good starting point:
- 8GB RAM,
- 100GB disk
- 2 processing cores

Other important infrastructure requirements:
- DNS entry, to allow access by name
- Configuring Firewall Rules to allow connection between the Ansible server and Active Directory
- Enable the WinRM service on Active Directory servers to allow remote access (using connection via HTTPS)

# Preparing the Server

In this scenario, I deployed Ansible and Jenkins on the same server (that uses Ubuntu 22.04), using the Azure cloud. However, from this point on, the chosen architecture (on-premises or cloud) will make little difference.
You can check the compatible OS versions [here][https://docs.ansible.com/ansible/latest/installation_guide/installation_distros.html].
Starting from the scratch, you can prepare the server by installing the necessary packages for the environment you want to build.

## Package installation

- python ->
- openjdk ->
- ansible -> python3 -m pip install --user ansible
- Ansible collection for Microsoft AD management -> ansible-galaxy collection install microsoft.ad
- Kerberos library for Python ->  apt-get -y install python-dev libkrb5-dev krb5-user
- Kerberos Client ->pip install krb5
- Remote access using WINRM -> pip install pywinrm

## Configuration files

- /etc/hosts -> include the IP address and name of the Active Directory Servers
- /etc/krb5.conf -> configure the Active Directory Servers on the sessions:

[realms]
    MY.DOMAIN.COM = {
        kdc = domain-controller1.my.domain.com
        kdc = domain-controller2.my.domain.com
    }

[domain_realm]
    .my.domain.com = MY.DOMAIN.COM
