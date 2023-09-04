from ..Spaces import dummy_space1, dummy_space2

dummy_transmission_channels = []

dummy_transmission_channels.append({"origin": "Dummy Boundary Action",
                                        "target": "Dummy Policy",
                                        "space": dummy_space1,
                                        "optional": False})

dummy_transmission_channels.append({"origin": "Dummy Policy",
                                        "target": "Dummy Mechanism",
                                        "space": dummy_space2,
                                        "optional": False})


dummy_transmission_channels.append({"origin": "Dummy Control Action",
                                        "target": "Dummy Policy",
                                        "space": dummy_space2,
                                        "optional": False})