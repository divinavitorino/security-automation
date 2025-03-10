# Preparation Guide

Automation for Windows environments can be tricky. 
Due to its particularities and Operating System architecture, setting up this environment may require additional time. 
However, the good news is: this is a preparation that is done only once. Then, just develop the playbooks according to your needs and you’re done. 
I will leave the ones I developed for my project to serve you as a guide.


# Infrastructure Requirements

- Suggested configuration: 
    - 4 vCPU
    - 16 GB of RAM 
    - 512 GB of storage
- Suggested distributions: 
    - Ubuntu (16.04 and later), 
    - Debian (version 9 (Stretch) and later), 
    - Red Hat Enterprise Linux - RHEL (version 7 and later), 
    - SUSE Linux Enterprise Server - SLES (version 12 and later). 

> [!NOTE]
> This scenario can suit a small to medium-sized company.
> But it is important to evaluate the processing and memory load to ensure that there are no bottlenecks in the execution of processes.

- Firewall rules (allow): 
    - Ansible: 
        - 22 (SSH), 
        - 5985 (WinRM - HTTP), 
        - 5986-(WinRM - HTTPS) 
    - Jenkins: 
        - 8080 (Web interface), 
        - 50000 (Agent-server communication).
- Active Directory credential: read and write permissions for user's organizational units (OU)
- Enable winrm Service on Active Directory
- Configure TrustedHosts file to permit only the connection from Ansible and Jenkins Server

[Powershell Command]

    Set-Item WSMan:localhost\client\trustedhosts -value Servername -Force


> [!NOTE]
> In this scenario, I deployed Ansible and Jenkins on the same server (that uses Ubuntu 22.04), using the Azure cloud. However, from this point on, the chosen architecture (on-premises or cloud) will make little difference.

# Ansible and Jenkins installation

Before starting, update the system packages:

    sudo apt update
    sudo apt upgrade -y

Ansible needs Python. Install this package first:

    sudo apt install -y python3 python3-pip

## Ansible Installation

Run the command

    python3 -m pip install --user ansible

Check the version to make sure the installation runned successfully

    ansible --version

## Jenkins Installation

For Jenkins installation, it is necessary to add the key and repository according to operational system. Please, before proceed, check the procedure on https://www.jenkins.io/doc/book/installing/linux/

To install Jenkins:

    sudo apt install -y jenkins

Enable Jenkins Service:

    sudo systemctl start jenkins
    sudo systemctl enable jenkins

Check service status

    sudo systemctl status jenkins

Access the web interface of Jenkins - http://<serveripaddress>:8080

It is necessary the initial password for the first access. It is stored on a file. Recover it unsing the command

    sudo cat /var/lib/jenkins/secrets/initialAdminPassword

# Additional packages(Linux)

To connect Ansible and Jenkins with Active Directory, you need the following additional packages:

Kerberos library for Python

    apt-get -y install python-dev libkrb5-dev krb5-user

Kerberos Client

    pip install krb5

Remote access using WINRM

    pip install pywinrm

Ansible collection for Microsoft AD management

    ansible-galaxy collection install microsoft.ad

# Configuring Ansible Vault

Ansible Vault allows you to encrypt sensitive data such as passwords or keys.

## Encrypting a Password

To encrypt a password, use the following command:

    ansible-vault encrypt_string 'your_password' --name 'vault_password'

This will output the encrypted string, which you can add to your playbook or variable file.

vault_password: !vault |
          $ANSIBLE_VAULT;1.1;AES256
          3132333435363738393031323334353637383930313233343536373839303132

When running the playbook, provide the vault password using the --ask-vault-pass option:

    ansible-playbook playbook.yml --ask-vault-pass

# Additional packages (Jenkins)


To connect Jenkins with Active Directory, you need the following additional packages. First, open Jenkins in your web browser: `http://<serveripaddress>:8080`


- Active Directory Plugin

1. Go to `Manage Jenkins` > `Manage Plugins`
2. In the `Available` tab, search for `Active Directory Plugin`
3. Select the plugin and click `Install without restart`

- Ansible Plugin

1. Go to `Manage Jenkins` > `Manage Plugins`
2. In the `Available` tab, search for `Ansible Plugin`
3. Select the plugin and click `Install without restart`

- Ansible Vault Plugin

1. Go to `Manage Jenkins` > `Manage Plugins`
2. In the `Available` tab, search for `Ansible Plugin`
3. Select the plugin and click `Install without restart`

- Pipeline Plugin

1. Go to `Manage Jenkins` > `Manage Plugins`
2. In the `Available` tab, search for `Pipeline`
3. Select the plugin and click `Install without restart`

## Configure Ansible Vault Password in Jenkins

1. Open Jenkins in your web browser: `http://<serveripaddress>:8080`
2. Go to `Manage Jenkins` > `Manage Credentials`
3. Click on `(global)` to add a new credential
4. Click `Add Credentials`
5. Select `Secret text` as the kind
6. Enter your Ansible Vault password in the `Secret` field
7. Provide an ID for the credential, e.g., `ansible-vault-password`
8. Click `OK`

Now you are ready to go and use the available playbooks or develop new ones according to your needs! :)

# Maintenance Tips
- It's important to keep the environment up to date, not only Jenkins and Ansible but also the plugins used. 
- Take a snapshot of the machine before upgrading, this will ensure less downtime in the event of a rollback.
- Have a maintenance window in your routine where all jobs are paused for updating. This will ensure that the vulnerabilities and bugs found have been fixed.
