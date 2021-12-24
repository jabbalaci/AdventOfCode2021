module Helper

read_content(fname::String)::String = read(fname, String)

read_lines(fname::String)::Vector{String} = readlines(fname)

read_lines_as_ints(fname::String)::Vector{Int} = [parse(Int, line) for line in readlines(fname)]

end # module
