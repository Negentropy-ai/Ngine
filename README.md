# ngine

<div align="center">

**Environment-Agnostic Embodied AI Infrastructure**

[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![CUDA](https://img.shields.io/badge/CUDA-12.x-green.svg)](https://developer.nvidia.com/cuda-toolkit)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0)

</div>

---

## Overview

**ngine** is an open-source framework for building, training, and evaluating embodied AI agents across diverse simulation environments. It provides a unified interface for working with different simulators, robot embodiments, and task domains.

### Key Features

- **Environment Agnostic** - Works with multiple simulation backends (Isaac Lab, ManiSkill, PyBullet)
- **Plugin Architecture** - Extensible design for adding new domains, robots, and simulators
- **Multi-Robot Support** - Unitree G1/H1, ARX arms, Agilex Piper, Fourier GR1, LeRobot compatible
- **Unified MDP Interface** - Consistent observation, action, and reward specifications
- **VR Teleoperation** - Built-in OpenXR support for data collection
- **Flexible Asset Loading** - Pluggable loaders for local, cloud, or custom backends
- **Distributed Training** - Scalable infrastructure for parallel environment execution

## Quick Start

### Prerequisites

- **OS**: Linux (Ubuntu 22.04+ recommended)
- **Python**: 3.10+
- **CUDA**: 12.x
- **Hardware**: NVIDIA RTX GPU
- **Isaac Sim**: 4.5+ (for Isaac Lab backend)

### Installation

```bash
# Clone repository
git clone https://github.com/your-org/ngine.git
cd ngine

# Create environment
conda create -n ngine python=3.10
conda activate ngine

# Install package
pip install -e .

# Optional dependencies
pip install -e ".[cloud]"    # Cloud asset loading
pip install -e ".[lerobot]"  # LeRobot integration
```

## Usage

### Teleoperation

```bash
# Using shell script
./teleop.sh

# Or directly with config
python ngine/scripts/teleop/teleop_main.py \
    --task_config g1-controller
```

### Training

```bash
./train.sh
```

### Evaluation

```bash
./eval.sh
```

## Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `NGINE_DATA_PATH` | Asset data directory | `./data` |
| `NGINE_LOG_DIR` | Log output directory | `./logs` |
| `NGINE_ASSET_BACKEND` | Asset loader backend (`local`, `cloud`) | `local` |

### YAML Configuration

```yaml
# configs/experiment.yml
scene:
  type: robocasa_kitchen
  layout: 1

robot:
  type: g1_dualarm

task:
  type: pick_and_place
  objects:
    - type: bowl
      placement: counter

simulation:
  num_envs: 4
  device: cuda:0
```

## Project Structure

```
ngine/
├── ngine/
│   ├── assets/              # Asset management system
│   │   ├── loaders/         # Pluggable asset loaders
│   │   └── registry.py      # Central asset registry
│   ├── benchmarks/          # Task definitions (LIBERO, Robocasa)
│   ├── engine/              # Core framework
│   │   ├── cfg/             # Configuration system
│   │   ├── devices/         # Input devices (VR, keyboard)
│   │   ├── embodiments/     # Robot definitions
│   │   ├── mdp/             # MDP components
│   │   ├── models/          # Asset and scene models
│   │   ├── orchestrate/     # Environment orchestration
│   │   ├── scenes/          # Scene definitions
│   │   └── tasks/           # Task base classes
│   ├── rl/                  # RL training configs
│   ├── scripts/             # CLI tools
│   └── utils/               # Helper utilities
└── configs/                 # Configuration files
```

## Supported Components

### Simulators
- Isaac Lab (GPU-accelerated)
- ManiSkill (planned)
- PyBullet (planned)

### Robots
| Type | Models |
|------|--------|
| Humanoid | Unitree G1, H1, Fourier GR1 |
| Mobile | Unitree Go2 |
| Arms | ARX X5/X7, Agilex Piper |
| Hands | LeRobot compatible |

### Task Domains
- Kitchen manipulation (Robocasa, LIBERO)
- Object manipulation
- Custom domains via plugin system

## Development

```bash
# Run tests
pytest tests/ -v

# Format code
black ngine/
isort ngine/

# Type checking
mypy ngine/
```

## License

Apache License 2.0 - see [LICENSE](LICENSE) for details.

## Contributing

Contributions welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Citation

```bibtex
@software{ngine2025,
  title = {ngine: Environment-Agnostic Embodied AI Infrastructure},
  year = {2025},
  url = {https://github.com/your-org/ngine}
}
```

## Acknowledgments

Built upon: [Isaac Lab](https://isaac-sim.github.io/IsaacLab/), [Robocasa](https://robocasa.ai/), [LIBERO](https://libero-project.github.io/)
