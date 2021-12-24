#!/usr/bin/env julia

using FromFile

@from "Helper.jl" import Helper

function take_apart(right::AbstractString)::Vector{Int}
    result::Vector{Int} = []

    parts = split(right, ",")
    for part in parts
        _, r = split(part, "=")
        a, b = split(r, "..")
        append!(result, parse(Int, a))
        append!(result, parse(Int, b))
    end
    #
    return result
end

function main()
    # fname = "example1.txt"
    # fname = "example2.txt"
    fname = "input.txt"

    bag::Set{Tuple{Int, Int, Int}} = Set()
    lines = Helper.read_lines(fname)
    for line in lines
        left, right = split(line)
        x1, x2, y1, y2, z1, z2 = take_apart(right)
        for x in x1:x2
            if !(-50 <= x <= 50)
                continue
            end
            for y in y1:y2
                if !(-50 <= y <= 50)
                    continue
                end
                for z in z1:z2
                    if !(-50 <= z <= 50)
                        continue
                    end
                    t = (x, y, z)
                    if left == "on"
                        push!(bag, t)
                    else
                        delete!(bag, t)
                    end
                end
            end
        end
    end
    println(length(bag))
end

if abspath(PROGRAM_FILE) == @__FILE__
    main()
end
