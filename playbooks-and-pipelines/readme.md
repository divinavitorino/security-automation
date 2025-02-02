# Playbooks

To use the playbook in Ansible, you need two files:
1. Inventory file: In this file, the information and connection methods with the hosts that will be managed are defined.
2. .yml or .yaml file: File that performs administration tasks on servers

Each file can have one or more tasks, depending on the need. It is important to think about tasks in blocks and gradually increase the degree of complexity

To avoid messing up with your playbooks, it is important to divide them in folders, according to the solutions you are creating.

Also, the names should be easy and simple to identificate them. 

# Pipelines

To use pipelines, you will need to configure a new pipeline on Jenkins.

> [!IMPORTANT]
> Test playbooks in controlled environments before putting them into production

> [!IMPORTANT]
> Use Ansible Vault to store your credentials