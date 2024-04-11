include("../../cadCAD.jl/src/spaces.jl")
include("../examples/StarterRepo/src/TypeMappings/types.jl")



x::DummyType2 = 100
y::DummyType1 = "100"
z::DummyCompoundType = DummyCompoundType(y, x)

Spaces.generate_space_type((a=DummyType1,b=DummyType2), "Test")
print(Spaces.Test("A",100))