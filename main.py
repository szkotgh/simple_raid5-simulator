import random
import base64

disk1 = []
disk2 = []
disk3 = []
data_size = 10
is_data_inited = False

def print_disks():
    print(f"Disk1: {disk1}")
    print(f"Disk2: {disk2}")
    print(f"Disk3: {disk3}")
    
    if is_data_inited:
        data_str = ""
        for i in range(data_size):
            data_str += f"{disk1[i]}{disk2[i]}{disk3[i]}"
        print(f"Data: {data_str}")
        print(f"Hash: {base64.b64encode(str(hash(data_str)).encode()).decode()}")
    else:
        print("Data init required")

def init_disks():
    disk1.clear()
    disk2.clear()
    disk3.clear()
    
    # init disk 1
    for i in range(data_size):
        random_value = random.randint(0, 1)
        disk1.append(random_value)
    
    # init disk 2
    for i in range(data_size):
        disk2.append(disk1[i] ^ 1)
    
    # init disk 3
    for i in range(data_size):
        disk3.append(disk1[i] ^ disk2[i])
    
    global is_data_inited
    is_data_inited = True

def remove_disk_data(disk):
    if not is_data_inited:
        print("Data init required")
        return
    
    for i in range(data_size):
        disk[i] = 0

def repair_disk(disk):
    if not is_data_inited:
        print("Data init required")
        return
    
    for i in range(data_size):
        disk[i] = disk1[i] ^ disk2[i] ^ disk3[i]

def main():
    while True:
        print("======================================")
        print_disks()
        print()
        print("1. Init disks")
        print("2. Remove disk data")
        print("3. Repair disk")
        print("4. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except KeyboardInterrupt:
            break
        except:
            continue
        
        if choice == 1:
            init_disks()
            
        elif choice == 2:
            disk_choice = int(input("Enter disk number: "))
            if disk_choice == 1:
                remove_disk_data(disk1)
            elif disk_choice == 2:
                remove_disk_data(disk2)
            elif disk_choice == 3:
                remove_disk_data(disk3)
            else:
                print("Invalid disk number")
            
        elif choice == 3:
            disk_choice = int(input("Enter disk number: "))
            if disk_choice == 1:
                repair_disk(disk1)
            elif disk_choice == 2:
                repair_disk(disk2)
            elif disk_choice == 3:
                repair_disk(disk3)
            else:
                print("Invalid disk number")
            
        elif choice == 4:
            break

if __name__ == "__main__":
    main()