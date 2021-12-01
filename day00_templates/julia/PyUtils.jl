module PyUtils

function input(prompt="")
    print(prompt)
    return readline()
end

chr(code::Int) = Char(code)

ord(c::Char) = convert(Int, c)

int(x::Union{Char, String}) = parse(Int, x)

int(x::Float64) = (x < 0 ? -1 : 1) * floor(Int, abs(x))

bin(n) = string(n, base=2)

hex(n) = string(n, base=16)

end # module
