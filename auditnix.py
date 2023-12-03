import subprocess
import os
import sys
sys.path.append('./audits/')
#modules
import userAudit
import fileAudit
import processAudit
import logAudit
import networkAudit
import updatesAudit
import kernelAudit
import policyAudit
import malwareAudit
import activityAudit
import passwordAudit
import systemAudit




def run_all_audits():
    userAudit.audit()
    fileAudit.audit()
    processAudit.audit()
    logAudit.audit()
    networkAudit.audit()
    updatesAudit.audit()
    kernelAudit.audit()
    policyAudit.audit()
    malwareAudit.audit()
    activityAudit.audit()
    passwordAudit.audit('root')
    systemAudit.audit()

def run_specific_audit(audit_name, *args):
    if audit_name == 'user':
        userAudit.audit()
    elif audit_name == 'file':
        fileAudit.audit()
    elif audit_name == 'pass':
        username = input("Enter username: ")
        passwordAudit.audit(username)
    elif audit_name == 'process':
        processAudit.audit()
    elif audit_name == 'log':
        logAudit.audit()
    elif audit_name == 'network':
        networkAudit.audit()
    elif audit_name == 'updates':
        updatesAudit.audit()
    elif audit_name == 'kernel':
        kernelAudit.audit()
    elif audit_name == 'policy':
        policyAudit.audit()
    elif audit_name == 'malware':
        malwareAudit.audit()
    elif audit_name == 'activity':
        activityAudit.audit()
    elif audit_name == 'system':
        systemAudit.audit()
    else:
        print("Invalid audit name or missing arguments")


def display_help():
    print("Usage:")
    print("python auditnix.py [audit_name1 audit_name2 ...]")
    print("Available audits: user, file, pass, process, log, network, updates, kernel, policy, malware, activity, system")
    print("Usage 'python auditnix.py -h' for help.")
    print("all: Run all available audits")
    print("user: User Account Auditing")
    print("file: File and Directory Auditing")
    print("process: Process Auditing")
    print("log: Log and Event Auditing")
    print("network: Network Auditing")
    print("updates: Security Updates")
    print("kernel: Kernel and Module Auditing")
    print("policy: Security Policy Auditing")
    print("malware: Malware and Intrusion Detection")
    print("activity: User Activity Auditing")
    print("pass: Password Policy Auditing")
    print("system: System Resource Auditing")

if __name__ == "__main__":
    args = sys.argv[1:]
    if not args or '-h' in args:
        display_help()
    else:
        for arg in args:
            if arg == 'all':
                run_all_audits()
            else:
                run_specific_audit(arg, *args[1:])
