#!/bin/bash

## Set paths for different modules, let payloads away cause there is only 1 module
exploits_path="../modules/exploits/"
posts_path="../modules/post/"
encoders_path="../modules/encoders/"

# Arg1: path, Arg2: type
gather_data() {
    mkdir -p data/$2
    grep -R "Rank =" $1 \
        | awk {'print $4'} \
        | sort -n \
        | uniq -c \
        | awk '{printf "%-18s,%s\n", $2, $1}' > data/$2/overall_rankings
    sed -i '1 i\Rank, count' data/$2/overall_rankings

    ## Get overall platform exploits
    grep -R "Rank =" $1 \
        | awk {'print $1'} \
        | grep -o -P "(?<=$1).*?(?=/)" \
        | sort -n \
        | uniq -c \
        | awk '{printf "%-12s,%s\n", $2, $1}' > data/$2/overall_platforms
    sed -i '1 i\Platform, count' data/$2/overall_platforms

    # Now filter all platforms
    sed 1d data/$2/overall_platforms | while read line ; do
        sub_path=$(echo $line | awk {'print $1'})
        mkdir -p data/$2/$sub_path
        search_path="$1$sub_path"

        grep -R "Rank =" $search_path \
            | awk '{print $4'} \
            | sort -nr \
            | uniq -c \
            | awk '{printf "%-18s,%s\n", $2, $1}' > data/$2/$sub_path/platform_result
    done
}

# Arg1: platform
gather_detailed_exploit_data() {
    mkdir -p data/exploit_detailed/$1
    grep -R "Rank =" $exploits_path$1 \
        | awk {'print $4'} \
        | sort -n \
        | uniq -c \
        | awk '{printf "%-18s,%s\n", $2, $1}' > data/exploit_detailed/$1/overall_rankings
    sed -i '1 i\Rank, count' data/exploit_detailed/$1/overall_rankings

    ## Get overall platform exploits
    grep -R "Rank =" $exploits_path$1 \
        | awk {'print $1'} \
        | grep -o -P "(?<=$exploits_path$1/).*?(?=/)" \
        | sort -n \
        | uniq -c \
        | awk '{printf "%-18s,%s\n", $2, $1}' > data/exploit_detailed/$1/overall_platforms
    sed -i '1 i\Platform, count' data/exploit_detailed/$1/overall_platforms

    # Now filter all platforms
    sed 1d data/exploit_detailed/$1/overall_platforms | while read line ; do
        sub_path=$(echo $line | awk {'print $1'})
        mkdir -p data/exploit_detailed/$1/$sub_path
        search_path="$exploits_path$1/$sub_path"

        grep -R "Rank =" $search_path \
            | awk '{print $4'} \
            | sort -nr \
            | uniq -c \
            | awk '{printf "%-18s,%s\n", $2, $1}' > data/exploit_detailed/$1/$sub_path/platform_result
    done
}

gather_data $exploits_path exploit
gather_data $posts_path post
gather_data $encoders_path encoder

gather_detailed_exploit_data linux
gather_detailed_exploit_data multi
gather_detailed_exploit_data unix
gather_detailed_exploit_data windows