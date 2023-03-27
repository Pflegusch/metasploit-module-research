#!/bin/bash

modules=("auxiliary" "encoder" "evasion" "exploit" "nop" "payload" "post")

# Hardcode modules it here because otherwise msfconsole 
# will need to start up each time which needs time
generate_csv_files() {
    ../metasploit-framework/msfconsole -q -x "\
    search type:auxiliary -s type -o csv/auxiliary.csv; \
    search type:encoder -s type -o csv/encoder.csv; \
    search type:evasion -s type -o csv/evasion.csv; \
    search type:exploit -s type -o csv/exploit.csv; \
    search type:nop -s type -o csv/nop.csv; \
    search type:payload -s type -o csv/payload.csv; \
    search type:post -s type -o csv/post.csv; \
    exit"
}

generate_platforms() {
    for module in ${modules[@]}; do
        cat csv/$module.csv \
            | grep -o -P "(?<=$module/).*?(?=/)" \
            | sort -n \
            | uniq -c > platforms/$module
        echo "Wrote platform results to platforms/$module"
    done
}

generate_csv_files
generate_platforms