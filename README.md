# Auditnix - Linux System Auditing Tool

## Overview
Auditnix is a robust command-line Linux auditing tool designed to enhance system security, integrity, and compliance. This tool provides comprehensive auditing functionalities across various system components, ensuring a meticulous review of user accounts, files, processes, logs, networks, kernel integrity, security policies, malware detection, user activities, password policies, and system resources.

## Usage
To run Auditnix, execute the script auditnix.py with the specified audit names as arguments.

```
python auditnix.py [audit_name1 audit_name2 ...]
```

Available audits:

**user**: User Account Auditing <br>
**file**: File and Directory Auditing <br>
**process**: Process Auditing <br>
**log**: Log and Event Auditing <br>
**network**: Network Auditing <br>
**updates**: Security Updates <br>
**kernel**: Kernel and Module Auditing <br>
**policy**: Security Policy Auditing <br>
**malware**: Malware and Intrusion Detection <br>
**activity**: User Activity Auditing <br>
**pass**: Password Policy Auditing <br>
**system**: System Resource Auditing <br>


For help, use:

```
python3 auditnix.py -h
```

## Installation

Clone the repository:
```
git clone https://github.com/zubairahm3d/auditnix.git
```

Navigate to the Auditnix directory:
```
cd auditnix
```

Run the tool by following the usage guidelines mentioned above.

## Requirements
Auditnix requires Python to run and is compatible with Python 3.x.

## Contact
For any inquiries or issues, please contact [zubi0258@gmail.com].

Feel free to use, modify, and contribute to Auditnix! We appreciate your interest and support in improving system security for Linux environments.
