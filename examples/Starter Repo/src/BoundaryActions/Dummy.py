from ..Spaces import dummy_space1

dummy_boundary_action_v1_option = {
    "name": "V1 Dummy Boundary",
    "description": "Description",
    "logic": "A+B=C",
}

dummy_boundary_action = {
    "name": "Dummy Boundary Action",
    "description": "Dummy",
    "constraints": [],
    "boundary_action_options": [dummy_boundary_action_v1_option],
    "called_by": ["Dummy"],
    "codomain": (dummy_space1,),
    "parameters_used": [],
}
