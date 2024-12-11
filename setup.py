from setuptools import setup, find_packages

base_requirements = [
    'pillow',
    'imageio',
    'imageio-ffmpeg',
    'tqdm',
    'easydict',
    'opencv-python-headless',
    'scipy',
    'ninja',
    'rembg',
    'onnxruntime',
    'trimesh',
    'xatlas',
    'pyvista',
    'pymeshfix',
    'igraph',
    'transformers',
    'torch>=2.0.1',
    'torchvision>=0.19.0',
]

setup(
    name="trellis",
    version="0.1.0",
    packages=find_packages(),
    install_requires=base_requirements,
    extras_require={
        'full': [
            'xformers',
            'flash-attn',
            'kaolin',
            'spconv-cu118;platform_system=="Linux"',
            'gradio==4.44.1',
            'gradio_litmodel3d==0.0.1',
        ]
    },
    python_requires='>=3.10',
    include_package_data=True,
    dependency_links=[
        'https://github.com/EasternJournalist/utils3d.git@9a4eb15e4021b67b12c460c7057d642626897ec8#egg=utils3d',
        'https://github.com/MaxtirError/FlexiCubes.git#egg=flexicubes'
    ]
)
