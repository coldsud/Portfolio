#!/bin/bash
#
transport=('car' 'train' 'bike' 'bus')

echo "${transport[@]}"

echo "${transport[1]}"

unset transport[1]

echo "${transport[@]}"

transport[1]='trainride'

echo "${transport[@]}"

cars=('honda' 'audi' 'bmw' 'tesla')

echo "${cars[@]}"

echo "${cars[2]}"

