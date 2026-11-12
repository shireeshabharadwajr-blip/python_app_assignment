import numpy as np

def insert_sensor_reading():
    arr = np.array([10, 20, 30, 40, 50])
    print("Original array:", arr)
    try:
        pos = int(input("Enter insertion position: "))
        if not (0 <= pos <= len(arr)):
            raise IndexError("Invalid insertion position!")
            
        val_str = input("Enter new integer sensor reading: ")
        if not val_str.isdigit():
            raise ValueError("Only integer numerical values are allowed!")
            
        val = int(val_str)
        arr = np.insert(arr, pos, val)
        print("Updated array:", arr)
    except (ValueError, IndexError) as e:
        print("Exception caught:", e)
    finally:
        print("Sensor insertion operation completed.")

if __name__ == "__main__":
    insert_sensor_reading()
