include("../../../../cadCAD.jl/src/spaces.jl")
include("types.jl")
using .Spaces: generate_space_type

generate_space_type((a=DummyType1,), "Dummy Space 1")
generate_space_type((a=DummyType1, b=DummyType1, c=DummyType2,), "Dummy Space 2")
