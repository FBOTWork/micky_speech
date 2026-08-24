<div align="center">

<img width="3876" height="719" alt="Image" src="https://github.com/user-attachments/assets/8ef46d3d-962e-44e7-bfff-f2757c90dfcf" />

</div>

## Overview
This is a group of ROS2 packages responsible for speak and listen features of [FBOT@Work](https://fbotwork.vercel.app/) industrial robot (MICKY) in RoboCup@Work league.

---

## Architecture

The system consists of two main packages:

```
micky_speech/
├── 📁 micky_speech/        # Core speech algorithms
│   └── 📁 STT/             # Speech recognition with NVIDIA Riva
```

---

## Pre Requisites

- ROS2 Humble
- Python 3.10+
- Ubuntu 22.04
- ROS dependencies are listed in `package.xml`.

## Installation

### 1. Clone Repository
```bash
cd ~/work_ws/src
git clone https://github.com/FBOTWork/micky_speech.git
```

### 2. Install Dependencies
```bash
cd ~/work_ws
sudo rosdep init  # Skip if already initialized
rosdep update
rosdep install --from-paths src --ignore-src -r -y
```

### 3. Build Package
```bash
cd ~/work_ws
colcon build --packages-select micky_vision
source install/setup.bash
```
