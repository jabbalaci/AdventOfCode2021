#!/usr/bin/env julia

using FromFile

@from "Helper.jl" import Helper

function main()
    # fname = "example.txt"
    fname = "input.txt"

    numbers = Helper.read_lines_as_ints(fname)
    cnt = 0
    for i in 2:length(numbers)
        prev = numbers[i-1]
        curr = numbers[i]
        if curr > prev
            cnt += 1
        end
    end
    println(cnt)
end

if abspath(PROGRAM_FILE) == @__FILE__
    main()
end
