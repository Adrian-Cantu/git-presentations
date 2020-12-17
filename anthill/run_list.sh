#!/usr.bin/bash

sleep 40
run=$(cat list_of_commands.txt | head -n $SGE_TASK_ID | tail -n 1)
$run > $SGE_TASK_ID\_command.txt
