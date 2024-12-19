def generate_mdl_script(num_textures, time_interval):
    mdl_script = f"""Version {{
    FormatVersion 800,
}}
Model "MainMenuGIF" {{
    NumGeosets 1,
    NumBones 1,
    NumAttachments 1,
    BlendTime 150,
    MaximumExtent {{ 0.8, 0.59999, 0 }},
    BoundsRadius 0.499997,
}}
Sequences 1 {{
    Anim "Stand" {{
        Interval {{ 1000, {1000 + num_textures * time_interval} }},
    }}
}}
Textures {num_textures} {{
"""

    for i in range(1, num_textures + 1):
        mdl_script += f'    Bitmap {{\n        Image "ui\\Glues\\MainMenu\\MainMenu3d_exp\\MainMenu_{i:03d}.blp",\n    }}\n'

    mdl_script += f"""}}
Materials 1 {{
    Material {{
        Layer {{
            FilterMode None,
            Unshaded,
            TextureID {num_textures + 2} {{
                DontInterp,
                0: 0,
"""

    for i in range(num_textures + 1):
        time = 1000 + i * time_interval
        mdl_script += f"                {time}: {i},\n"

    mdl_script += f"""            }}
        }}
    }}
}}
Geoset {{
    Vertices 4 {{
        {{ 0.8, 0, 0 }},
        {{ 0.8, 0.59999, 0 }},
        {{ 0, 0, 0 }},
        {{ 0, 0.59999, 0 }},
    }}
    Normals 4 {{
        {{ 0, 0, 1 }},
        {{ 0, 0, 1 }},
        {{ 0, 0, 1 }},
        {{ 0, 0, 1 }},
    }}
    TVertices 4 {{
        {{ 1, 1 }},
        {{ 1, 0 }},
        {{ 0, 1 }},
        {{ 0, 0 }},
    }}
    VertexGroup {{
        0,
        0,
        0,
        0,
    }}
    Faces 1 6 {{
        Triangles {{
            {{ 3, 2, 1, 0, 1, 2 }},
        }}
    }}
    Groups 1 1 {{
        Matrices {{ 0 }},
    }}
    MinimumExtent {{ 0, 0, 0 }},
    MaximumExtent {{ 0.8000000119, 0.59999, 0 }},
    BoundsRadius 0.99999,
    MaterialID 0,
    SelectionGroup 0,
}}
Bone "Plane01" {{
    ObjectId 0,
    GeosetId Multiple,
    GeosetAnimId None,
}}
Attachment "UNNAMED" {{
    ObjectId 1,
    AttachmentID 0,
}}
PivotPoints 2 {{
    {{ 0, 0, 0 }},
    {{ 0, 0, 0 }},
}}
"""
    return mdl_script


num_textures = int(input("Number of images : "))
time_interval = int(input("Frame Interval(ms) : "))

mdl_script = generate_mdl_script(num_textures, time_interval)

with open("MainMenu3D_exp.mdl", "w") as file:
    file.write(mdl_script)
    
print("Complete")