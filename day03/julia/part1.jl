#!/usr/bin/env julia

using FromFile

@from "Helper.jl" import Helper

function get_column(i::Int, lines::Vector{String})::Vector{Char}
    return [line[i] for line in lines]
end

function main()
    # fname = "example.txt"
    fname = "input.txt"

    lines = Helper.read_lines(fname)
    no_of_columns = length(lines[1])

    result::Vector{Char} = []
    for i in 1:no_of_columns
        column = get_column(i, lines)
        zeros = count(c -> c == '0', column)
        ones = length(column) - zeros
        append!(result, zeros > ones ? '0' : '1')
    end
    gamma_str = join(result)
    epsilon_str = begin
        tmp = replace(gamma_str, '0' => 'x')
        tmp = replace(tmp, '1' => '0')
        replace(tmp, 'x' => '1')
    end
    gamma = parse(Int, gamma_str, base=2)
    epsilon = parse(Int, epsilon_str, base=2)
    println(gamma)
    println(epsilon)
    println("---")
    println(gamma * epsilon)
end

if abspath(PROGRAM_FILE) == @__FILE__
    main()
end
