#!/usr/bin/env julia

using FromFile

@from "Helper.jl" import Helper

const OXYGEN = 1
const CO2 = 2

function get_column(i::Int, lines::Vector{String})::Vector{Char}
    return [line[i] for line in lines]
end

function get_value(data::Vector{String}; which=OXYGEN)::Int
    lines = copy(data)

    col_idx = 1
    while length(lines) != 1
        column::Vector{Char} = get_column(col_idx, lines)
        zeros = count(c -> c == '0', column)
        ones = length(column) - zeros
        to_keep::Char = begin
            if which == OXYGEN
                result = '1'    # if ones >= zeros
                if zeros > ones
                    result = '0'
                end
            else    # CO2
                result = '0'    # if zeros <= ones
                if ones < zeros
                    result = '1'
                end
            end
            result
        end
        lines = [line for line in lines if line[col_idx] == to_keep]
        col_idx += 1
    end
    return parse(Int, lines[1], base=2)
end

function main()
    # fname = "example.txt"
    fname = "input.txt"

    data = Helper.read_lines(fname)

    oxygen = get_value(data, which=OXYGEN)
    println(oxygen)
    co2 = get_value(data, which=CO2)
    println(co2)
    println("---")
    println(oxygen * co2)
end

if abspath(PROGRAM_FILE) == @__FILE__
    main()
end
