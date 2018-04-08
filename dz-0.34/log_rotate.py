#!/bin/env python
import os
import sys
import shutil
import datetime


log_suffix = ".log"
log_time_suffix = (datetime.datetime.now() - datetime.timedelta(minutes=10)).strftime(".%Y-%m-%d_%H")


def print_help_and_exit():
    sys.stderr.write("Usage: \n\tpython %s <path_to_log_dir>\n" % sys.argv[0])
    sys.exit(-1)


def main():
    if len(sys.argv) != 2:
        print_help_and_exit()
    if not os.path.exists(sys.argv[1]):
        sys.stderr.write("Not exists directory: %s\n" % sys.argv[1])
        print_help_and_exit()
    path = sys.argv[1]
    filename_list = [os.path.join(path, filename) for filename in os.listdir(path) if filename.endswith(log_suffix)]

    for filename in filename_list:
        try:
            shutil.copy(filename, filename + log_time_suffix)
            os.popen("true > " + filename)
            sys.stdout.write("[ OK ] %s => %s%s\n" % (filename, filename, log_time_suffix))
        except Exception as e:
            sys.stderr.write("[Fail] %s => %s%s, error: %s\n" % (filename, e.message, filename, log_time_suffix))


if __name__ == '__main__':
    main()
