#!/bin/bash

# Display hours
display_hours() {
    TIME=$(date "+%H:%M")
    echo -n "$TIME"
}

# Display date
display_date() {
    DATE=$(date "+%y-%d-%m")
    echo -n "$DATE"
}

while true; do 
    echo "%{c} $(display_date) \
          %{r} $(display_hours)"
    sleep 1
done |

lemonbar \
 -g "x28"\
 -B "#000000"\
 -F "#F1F2F0"\
 -f "Liberation Mono"
 
