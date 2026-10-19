from setuptools import find_packages, setup

package_name = 'micky_speech'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='gabriela',
    maintainer_email='garcia.hoppe.gabriela@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'riva_stt = micky_speech.STT.riva_stt:main',
            'riva_tts = micky_speech.TTS.riva_tts:main', 
        ],
    },
