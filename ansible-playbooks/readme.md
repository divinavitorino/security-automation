# Playbooks

To use the playbook in Ansible, you need two files:
1. Inventory file: In this file, the information and connection methods with the hosts that will be managed are defined.
2. .yml or .yaml file: File that performs administration tasks on servers

Each file can have one or more tasks, depending on the need. It is important to think about tasks in blocks and gradually increase the degree of complexity

> [!IMPORTANT]
> Test playbooks in controlled environments before putting them into production

> [!IMPORTANT]
> Use Ansible Vault to store your credentials