#!/bin/bash

generate_csv_files() {
    ../../metasploit-framework/msfconsole -q -x "\
    search type:auxiliary -s type -o csv/auxiliary.csv; \
    search type:encoder -s type -o csv/encoder.csv; \
    search type:evasion -s type -o csv/evasion.csv; \
    search type:exploit -s type -o csv/exploit.csv; \
    search type:nop -s type -o csv/nop.csv; \
    search type:payload -s type -o csv/payload.csv; \
    search type:post -s type -o csv/post.csv; \
    exit"
}

generate_csv_files
