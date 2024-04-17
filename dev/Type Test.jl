include("../../cadCAD.jl/src/spaces.jl")
include("../examples/StarterRepo/src/TypeMappings/types.jl")
using .Spaces: generate_space_type


x::DummyType2 = 100
y::DummyType1 = "100"
z::DummyCompoundType = DummyCompoundType(y, x)

generate_space_type((a=DummyType1,b=DummyType2), "Test")
Test = Spaces.Test("A",100)
print(Test)