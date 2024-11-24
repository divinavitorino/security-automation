# Preparation Guide

Automation for Windows environments can be tricky. 
Due to its particularities and Operating System architecture, setting up this environment may require additional time. 
However, the good news is: this is a preparation that is done only once. Then, just develop the playbooks according to your needs and you’re done. I will leave the ones I developed for my project to serve you as a guide.
The Security Automation for SMBs project relies on open source tools to create an implementation framework for routine identity management tasks.


# Infrastructure Requirements

- Suggested configuration: 4 vCPU, 16 GB of RAM, 512 GB of storage
- Suggested distributions: Ubuntu (16.04 and later), Debian (version 9 (Stretch) and later), Red Hat Enterprise Linux - RHEL (version 7 and later), SUSE Linux Enterprise Server - SLES (version 12 and later). 
- Firewall rules: Ansible: 22 (SSH), 5985 (WinRM - HTTP), 5986-(WinRM - HTTPS) and Jenkins: 8080 (Web interface), 50000 (Agent-server communication).
- Active Directory credential: read and write permissions for user's organizational units (OU)

> [!NOTE]
> This scenario can suit a small to medium-sized company.
> But it is important to evaluate the processing and memory load to ensure that there are no bottlenecks in the execution of processes.

> [!NOTE]
> In this scenario, I deployed Ansible and Jenkins on the same server (that uses Ubuntu 22.04), using the Azure cloud. However, from this point on, the chosen architecture (on-premises or cloud) will make little difference.

## Package installation

- python 
- openjdk 
- ansible

python3 -m pip install --user ansible

- Ansible collection for Microsoft AD management

ansible-galaxy collection install microsoft.ad

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


