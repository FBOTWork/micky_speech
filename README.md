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

## Prerequisites

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
2. Update local branch with `git fetch` then `git pull`
3. Create a feature branch (`git checkout -b feature/feature-name`)
4. Create feature directory in `micky_speech/feature_name/`
5. Implement the feature
6. Update `__init__.py` imports
7. Add launch file in `launch/`
8. Add feature node to `setup.py`
9. Test and verify that the feature is fully functional
10. Commit changes (`git commit -m 'Add feature-name'`)
11. Push the branch (`git push`)
12. Open a Pull Request from `feature/feature-name` to `release` and add a reviewer
13. After review and validation, merge the Pull Request into `release`
14. Once `release` is tested and stable, merge it into `master`

### Fixing a Feature

1. Switch to the `release` branch (`git checkout release`)
2. Update local branch with `git fetch` then `git pull`
3. Create a fix branch (`git checkout -b fix/broken-feature`)
4. Fix a feature
5. Commit changes (`git commit -m 'Fix amazing feature'`)
6. Push to the branch (`git push`)
7. Open a Pull Request from `fix/feature-name` to `release` and add a reviewer
8. After review and validation, merge the Pull Request into `release`
9. Once `release` is tested and stable, merge it into `master`

---
