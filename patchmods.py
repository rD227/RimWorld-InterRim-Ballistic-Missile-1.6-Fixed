import os
import sys

try:
    from PIL import Image
except ImportError:
    print("Error: Pillow is not installed.")
    print("Please install it by running: pip install Pillow")
    sys.exit(1)

def convert_dds_to_png(target_dirs):
    count = 0
    for d in target_dirs:
        print(f"Scanning directory: {os.path.abspath(d)}")
        for root, _, files in os.walk(d):
            for f in files:
                if f.lower().endswith('.dds'):
                    dds_path = os.path.join(root, f)
                    # Create corresponding PNG path
                    png_path = dds_path[:-4] + '.png'
                    try:
                        # Open DDS and save as PNG
                        with Image.open(dds_path) as img:
                            img.save(png_path)
                        
                        # Remove the original DDS file after successful conversion
                        os.remove(dds_path)
                        count += 1
                        print(f"[OK] Converted: {f}")
                    except Exception as e:
                        print(f"[ERROR] Failed to convert {f}: {e}")
    return count

if __name__ == "__main__":
    # Use arguments as directories, or default to the current working directory
    dirs_to_process = sys.argv[1:] if len(sys.argv) > 1 else ["."]
    
    print("Starting DDS to PNG conversion...")
    converted_count = convert_dds_to_png(dirs_to_process)
    print(f"\nDone! Successfully converted {converted_count} files.")
