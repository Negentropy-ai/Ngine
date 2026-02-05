#!/bin/bash
task_config=lerobot_liftobj_state

python ./ngine/scripts/rl/train.py \
    --task_config="$task_config" \
    --headless \
    # --enable_cameras
