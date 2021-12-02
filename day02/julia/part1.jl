#!/usr/bin/env julia

using FromFile

@from "Helper.jl" import Helper

function main()
    # fname = "example.txt"
    fname = "input.txt"
    lines = Helper.read_lines(fname)

    horizontal = 0
    depth = 0

    for line in lines
        parts = split(line)
        instruction = parts[1]
        value = parse(Int, parts[2])
        if instruction == "forward"
            horizontal += value
        elseif instruction == "down"
            depth += value
        elseif instruction == "up"
            depth -= value
        else
            @assert false
        end
    end
    println(horizontal * depth)
end

if abspath(PROGRAM_FILE) == @__FILE__
    main()
end
