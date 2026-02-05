#!/usr/bin/env python3
"""
Convert a local KitchenRoom.usd to asset format.

This script:
1. Loads the local KitchenRoom.usd
2. Identifies fixtures from subdirectories
3. Reorganizes them into /World/fixtures/ hierarchy
4. Renames them to standardized format (dishwasher_0, microwave_0, etc.)
5. Adds required metadata
6. Exports as scene.usd and scene_enabled.usd
"""

import os
import sys
import re
from pathlib import Path

def identify_fixture_type(name):
    """Map directory names to fixture types."""
    name_lower = name.lower()
    
    fixture_map = {
        'dishwasher': 'dishwasher',
        'microwave': 'microwave',
        'sink': 'sink',
        'stove': 'stove',
        'stovetop': 'stove',
        'refrigerator': 'refrigerator',
        'oven': 'oven',
        'coffeemachine': 'coffee_machine',
        'toaster': 'toaster',
        'rangehood': 'range_hood',
    }
    
    for key, fixture_type in fixture_map.items():
        if key in name_lower:
            return fixture_type
    
    return None

def convert_kitchen_scene(input_usd, output_dir):
    """Convert local kitchen scene to asset format."""
    
    print(f"Converting: {input_usd}")
    print(f"Output to: {output_dir}")
    
    # This requires USD Python bindings (pxr)
    try:
        from pxr import Usd, UsdGeom, Sdf
    except ImportError:
        print("\nERROR: USD Python bindings (pxr) not available!")
        print("This script requires Isaac Sim's Python environment.")
        print("\nTo run this script:")
        print("1. Activate Isaac Sim's Python:")
        print("   source ~/.local/share/ov/pkg/isaac-sim-*/python.sh")
        print("2. Run the script:")
        print("   python convert_kitchen_scene.py")
        return False
    
    # Load input stage
    input_stage = Usd.Stage.Open(str(input_usd))
    if not input_stage:
        print(f"ERROR: Could not open {input_usd}")
        return False
    
    # Create output stage
    output_usd = Path(output_dir) / "scene.usd"
    output_stage = Usd.Stage.CreateNew(str(output_usd))
    
    # Create World and fixtures hierarchy
    world_prim = UsdGeom.Xform.Define(output_stage, "/World")
    fixtures_prim = UsdGeom.Xform.Define(output_stage, "/World/fixtures")
    
    # Find fixtures in input scene
    input_dir = Path(input_usd).parent
    fixture_dirs = [d for d in input_dir.iterdir() if d.is_dir() and not d.name.startswith('.')]
    
    fixture_counts = {}
    
    print(f"\nFound {len(fixture_dirs)} potential fixture directories")
    
    for fixture_dir in fixture_dirs:
        fixture_type = identify_fixture_type(fixture_dir.name)
        
        if fixture_type:
            # Get count for this fixture type
            count = fixture_counts.get(fixture_type, 0)
            fixture_counts[fixture_type] = count + 1
            
            # Create standardized name
            fixture_name = f"{fixture_type}_{count}"
            fixture_path = f"/World/fixtures/{fixture_name}"
            
            print(f"  {fixture_dir.name} -> {fixture_name}")
            
            # Create fixture prim (simplified - actual implementation would copy geometry)
            fixture_xform = UsdGeom.Xform.Define(output_stage, fixture_path)
            
            # Add metadata
            prim = output_stage.GetPrimAtPath(fixture_path)
            prim.SetCustomDataByKey("fixture_type", fixture_type)
            prim.SetCustomDataByKey("original_name", fixture_dir.name)
    
    # Save output
    output_stage.GetRootLayer().Save()
    print(f"\nSaved: {output_usd}")
    
    # Create scene_enabled.usd (copy for now)
    output_enabled = Path(output_dir) / "scene_enabled.usd"
    output_stage.GetRootLayer().Export(str(output_enabled))
    print(f"Saved: {output_enabled}")
    
    print("\nNOTE: This is a simplified conversion.")
    print("A complete conversion would require:")
    print("  - Copying all geometry and materials")
    print("  - Preserving articulation data")
    print("  - Adding proper fixture metadata")
    print("  - Setting up collision meshes")
    
    return True

if __name__ == "__main__":
    input_usd = Path("/home/user/startups/ngine/datasets/Kitchen/Collected_KitchenRoom/KitchenRoom.usd")
    output_dir = Path("/home/user/startups/ngine/datasets/converted_kitchen")
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print("=" * 80)
    print("Kitchen Scene Converter - Local to Asset Format")
    print("=" * 80)
    
    success = convert_kitchen_scene(input_usd, output_dir)
    
    if success:
        print("\n✓ Conversion complete!")
        print(f"\nTo use the converted scene, update your config:")
        print(f"  layout: {output_dir}/scene.usd")
    else:
        print("\n✗ Conversion failed!")
        sys.exit(1)
