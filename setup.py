import os
import glob

from setuptools import find_packages, setup

package_name = 'micky_speech'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'nodes'), glob.glob('nodes/*.py')),
        (os.path.join('share', package_name , 'launch'), glob.glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'nodes', 'config'), glob.glob('nodes/config/*.yaml')),
        (os.path.join('share', package_name, 'nodes', 'config', 'rviz'), glob.glob('nodes/config/rviz/*.rviz')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Gabriela',
    maintainer_email='garcia.hoppe.gabriela@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'reference_node = nodes.reference_node:main',
            'stt_node = micky_speech.STT.riva_talker:main'
        ],
    },
)