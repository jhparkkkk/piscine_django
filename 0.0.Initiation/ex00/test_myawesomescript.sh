#!/bin/sh

test_case() {
    expected=$1
    input=$2

    output=$(./myawesomescript.sh $input)

    output=$(./myawesomescript.sh $input | tr -d '\r' | tr -d '\n')
    expected=$(echo $expected | tr -d '\r' | tr -d '\n')

    RED='\033[0;31m'
    GREEN='\033[0;32m'
    NO_COLOR='\033[0m'
    
    if [ "$output" = "$expected" ]; then
        echo "${GREEN}PASS:${NO_COLOR} $input -> $expected"
    else
        echo "${RED}FAIL:${NO_COLOR} $input -> Expected: $expected, but got: $output"
    fi
}

test_case "http://42.fr/" "bit.ly/1O72s3U"
test_case "https://try.codecademy.com/for-beginners?utm_source=twitter&utm_medium=organic-social&utm_campaign=camp~curriculum_2023_new_years~prod~All~geo~All~aud~General~funn_Awareness~msg~Learn_More~cont~social~sited~Hub_Page~time~2022Q4~&utm_content=tw_curriculum_2023_new_years_link_in_bio" "bit.ly/3Z19kqd"
test_case "http://www.apple.com/" "bit.ly/xxxxx"
test_case "Error: only one argument required" "" 
test_case "" "bit.ly/1O72s3" 


