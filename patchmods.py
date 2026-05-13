import os
import sys

try:
    from PIL import Image
except ImportError:
    print("Error: Pillow is not installed.")
    print("Please install it by running: pip install Pillow")
    sys.exit(1)

def convert_dds_to_png_and_flip(target_dirs):
    count = 0
    for d in target_dirs:
        print(f"Scanning directory: {os.path.abspath(d)}")
        for root, _, files in os.walk(d):
            for f in files:
                if f.lower().endswith('.dds'):
                    dds_path = os.path.join(root, f)
                    # path ti PNG
                    png_path = dds_path[:-4] + '.png'
                    try:
                        # flip
                        with Image.open(dds_path) as img:
                            flipped_img = img.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
                            flipped_img.save(png_path)
                        
                        # 删除旧的 DDS 文件
                        os.remove(dds_path)
                        count += 1
                        print(f"[OK] Converted & Flipped: {f}")
                    except Exception as e:
                        print(f"[ERROR] Failed to convert {f}: {e}")
    return count

if __name__ == "__main__":
    dirs_to_process = sys.argv[1:] if len(sys.argv) > 1 else ["."]
    
    print("Starting DDS to PNG conversion (with vertical coordinate fix)...")
    converted_count = convert_dds_to_png_and_flip(dirs_to_process)
    print(f"\nDone! Successfully converted and flipped {converted_count} files.")