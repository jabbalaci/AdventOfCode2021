#!/usr/bin/env julia

using FromFile

@from "Helper.jl" import Helper

function main()
    fname = "example.txt"
    # fname = "input.txt"

    lines = Helper.read_lines(fname)
    for line in lines
        println(line)
    end
end

if abspath(PROGRAM_FILE) == @__FILE__
    main()
end
