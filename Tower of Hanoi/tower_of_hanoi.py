def hanoi_solve(disks):
    rods = [list(range(disks, 0, -1)), [], []]
    path = f"{rods[0]} {rods[1]} {rods[2]}"

    def move(n, source, transit, target):
        nonlocal path
        if n == 0:
            return
        move(n - 1, source, target, transit)
        target.append(source.pop())
        path += f"\n{rods[0]} {rods[1]} {rods[2]}"
        move(n - 1, transit, source, target)

    move(disks, rods[0], rods[1], rods[2])
    return path
    
    