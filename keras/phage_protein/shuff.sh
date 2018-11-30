#!/bin/bash


gunzip -c pi_dipep.gz | shuf > pi_dipep_shuf
head -n 24000 pi_dipep_shuf > pi_dipep_head
head -n 10 pi_dipep_shuf > pi_dipep_mini_head
tail -n 1675 pi_dipep_shuf > pi_dipep_tail

gunzip -c tripep_data.gz | shuf > tripep_shuf
head -n 24000 tripep_shuf > tripep_head
tail -n 1675 tripep_shuf > tripep_tail


