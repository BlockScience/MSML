include("../../cadCAD.jl/src/spaces.jl")
include("../examples/StarterRepo/src/TypeMappings/types.jl")
using .Spaces: generate_space_type


x::DummyType2 = 100
y::DummyType1 = "100"
z::DummyCompoundType = DummyCompoundType(y, x)

generate_space_type((a=DummyType1,b=DummyType2), "Test")
# Test = Spaces.Test("A",100)

function atest()::NamedTuple{(:e, :f), Tuple{Spaces.Test, Spaces.Test}}
    return (e = Spaces.Test(a="A", b=100), f = Spaces.Test(a="A", b=100))
end





println(Base.return_types(atest))

# Get the methods of the function
#m = methods(atest)

# Print the signatures of the methods
#for method in m
#    println(method.sig)
#end

