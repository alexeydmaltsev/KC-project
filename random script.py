if __name__ == "__main__":
    print("boat, mountain, path, tree, cathedral")
    with open("random.txt", mode="r") as file:
        for _ in range(5):
            for i in range(5):
                nums = [0,0,0]
                for j in range(3):
                    nums[j] = file.readline()[:-1]
                if i != 2:
                    print("    ", end = "")
                print(f"&{20 * (i + 1)}&", end = " ")
                print(f"{nums[0]} &", end = " ")
                print(f"{nums[1]} & {nums[2]} \\\\")
                _ = file.readline()


            print(file.readline())


