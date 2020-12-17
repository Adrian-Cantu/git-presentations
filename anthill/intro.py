# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.7.1
#   kernelspec:
#     display_name: Bash
#     language: bash
#     name: bash
# ---

# # anthill 
#
# anthill is cluster that uses the "Sun Grid engine" scheduler.
#
#

# To submit a job to the cluster you need to write a bash script

cat ./sleep_test.sh

# submit using qsub

rm -rf sge sgo
mkdir -p sge
mkdir -p sgo
qsub -cwd -N test -e sge -o sgo -q important ./sleep_test.sh

# you can check the status using qstat

qstat


# If needed, the job can be killed using qdel

#qdel [job-ID]
qdel 6039617

# STDOUT is redirected to sgo and STDERR to sge.

cat sgo/test.o6039618

# ## cwd
# -cwd tells SGE to use the current directory
# ## N
# -N names the job
# ## e
# -e redirects STDERR
# ## o
# -o redirects STDOUT
# ## q
# -q select the queue. there are 3 queues:
#
# # default
# The default queue has 35 nodes, each with 16 processors and 128 GB RAM. Each processor runs an independent job, so you can run 560 jobs simultaneously on these machines. This queue is in eternally friendly mode, and all jobs are run on a first-in first-out basis.
# # important
# The important queue has 4 nodes with 16 processors and 128 GB RAM each. This queue is for single jobs only. Do not run array jobs on this queue or they will be terminated! The queue is for testing and running individual programs.
# # smallmem
# This queue has nine nodes each with 8 processors (72 computes total), Each processor has 14 GB RAM, except node1 that has 24 GB RAM. People often forget about this queue, so sometimes it is worth checking!

qconf -sql

# argument can also be passed in file

cat sleep_test_infile.sh

qsub ./sleep_test_infile.sh

# With an array job, sleep_test_job_array.sh gets passed a special variable called $SGE_TASK_ID that is the number of the job it is running

cat ./sleep_test_job_array.sh

qsub -cwd -N array -e sge -o sgo -t 1:5:1 -q default ./sleep_test_job_array.sh

qstat

ls sgo/array*

cat sgo/array*

# a classic hack is to list all commands to run in a file and have a script read it and run.

cat ./list_of_commands.txt

cat ./run_list.sh

qsub -cwd -N list -e sge -o sgo -t 1:3:1 -q default ./run_list.sh

qstat

ls

grep command *command.txt

# finally, it is wise to use full path when possible. Don't assume the enviroment is the same

cat path.sh

qsub -cwd -N ppath -e sge -o sgo -q default ./path.sh

cat sgo/ppath* sge/ppath*

cat full_path.sh

qsub -cwd -N fpath -e sge -o sgo -q default ./full_path.sh

cat sgo/fpath* sge/fpath*

which -a python

# # extra tips
# use -pe make 16 to take a full node for yourself.
#
