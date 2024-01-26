# Add these to your ~/.zshrc

AOC="/Users/edwin.mui/Downloads/CodingProjects/advent-of-code" # remember to change this to whatever your AOC directory is
AOC_COOKIE="_ga=GA1.2.1476044819.1701804649; session=53616c7465645f5fdae1f70dfab0ade3f25f7a6a5c4f03d2f2e06a08d6c89a613d59b07d28194c047624bdbd2f32c5b811778b1b57d25ed1e3ab91163a09e4ac; _gid=GA1.2.1753189704.1702014864; _gat=1" # get this from the cookies tab in network tools on the AOC website

alias aos="cd $AOC; python3 solution.py < in.txt"
alias aot="cd $AOC; echo -ne '\e[0;34m'; python3 solution.py < test.txt; echo -ne '\e[0m'"
alias aoc="aot; echo; aos"

alias jaos="cd $AOC; bun solution.js in.txt"
alias jaot="cd $AOC; bun solution.js test.txt"
alias jaoc="jaot; echo; jaos"

function aoc-load () {
    if [ "$1" ]
    then
        curl --cookie "session=$AOC_COOKIE" https://adventofcode.com/$1/day/$2/input > in.txt
    else
        curl --cookie "session=$AOC_COOKIE" "$(date +https://adventofcode.com/%Y/day/%d/input | sed 's/\/0/\//g')" > in.txt
    fi
}
