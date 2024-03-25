abstract type DummyType1 <: AbstractString end
abstract type DummyType2 <: Integer end
struct DummyCompoundType
    A::DummyType1
    B::DummyType2
end