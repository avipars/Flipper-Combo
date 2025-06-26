import os

def find_non_ir_files(root_path):
    print(f"Scanning for non-.ir files in: {root_path}\n")
    count = 0

    for dirpath, _, filenames in os.walk(root_path):
        for file in filenames:
            if not file.lower().endswith('.ir'):
                full_path = os.path.join(dirpath, file)
                print(f"Found non-.ir file: {full_path}")
                count += 1

    if count == 0:
        print("✅ No non-.ir files found.")
    else:
        print(f"\nTotal non-.ir files found: {count}")

folder = input("Enter the fullpath to your local IRDB folder (unzipped):\n")
find_non_ir_files(folder)