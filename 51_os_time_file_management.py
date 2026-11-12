import os
import time

def file_management_demo():
    dir_path = "My_Project/assignments/task1"
    os.makedirs(dir_path, exist_ok=True)
    print("Current Working Directory:", os.getcwd())
    print("Byte String Format:", os.getcwdb())
    
    file_path = os.path.join(dir_path, "sample.py")
    with open(file_path, "w") as f:
        f.write("print('Python Assignment')")
        
    print("Directory Exists:", os.path.isdir(dir_path))
    
    total_size = sum(
        os.path.getsize(os.path.join(root, file))
        for root, dirs, files in os.walk("My_Project")
        for file in files
    )
    print(f"total_size: {total_size} bytes")
    print("access time:", time.ctime(os.path.getatime(file_path)))
    print("Last modified time:", time.ctime(os.path.getmtime(file_path)))
    print("list of files in the directory:", os.listdir(dir_path))

if __name__ == "__main__":
    file_management_demo()
