with open("input.txt", "r") as f:
    file = f.read().strip().splitlines()

seeds = [int(i) for i in file[0].replace("seeds: ", "").split(" ")]

new_nums = [0] * len(seeds)
for line in file[2:]:
    if line:
        if line[0].isnumeric():
            values = [int(j) for j in line.split()]
            for i, seed in enumerate(seeds):
                if seed in range(values[1], values[1] + values[2]):
                    # print(values[0] - values[1], seed)
                
                    new_nums[i] = seed + (values[0] - values[1])
                else:
                    if not new_nums[i]:
                        new_nums[i] = seed
                # print(seeds, new_nums, seed)
    else:
        seeds = new_nums.copy()


print(min(new_nums))
