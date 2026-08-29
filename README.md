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

---

## Development

### Creating a New Feature

1. Switch to the `release` branch (`git checkout release`)
2. Create a feature branch (`git checkout -b feature/feature-name`)
3. Create feature directory in `micky_speech/feature_name/`
4. Implement the feature
5. Update `__init__.py` imports
6. Add launch file in `launch/`
7. Add feature node to `setup.py`
8. Test and verify that the feature is fully functional
9. Commit changes (`git commit -m 'Add feature-name'`)
10. Push the branch (`git push`)
11. Open a Pull Request from `feature/feature-name` to `release` and add a reviewer
12. After review and validation, merge the Pull Request into `release`
13. Once `release` is tested and stable, merge it into `master`

### Fixing a Feature

1. Switch to the `release` branch (`git checkout release`)
2. Create a fix branch (`git checkout -b fix/broken-feature`)
3. Fix a feature
4. Commit changes (`git commit -m 'Fix amazing feature'`)
5. Push to the branch (`git push`)
6. Open a Pull Request from `fix/feature-name` to `release` and add a reviewer
7. After review and validation, merge the Pull Request into `release`
8. Once `release` is tested and stable, merge it into `master`

---