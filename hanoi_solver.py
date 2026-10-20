def hanoi_solver(n):
    rod1 = list(range(n, 0, -1))
    rod2 = []
    rod3 = []

    result = []

    def record_state():
        result.append(f"{rod1} {rod2} {rod3}")

    def move_disks(n, source, target, auxiliary):
        if n == 0:
            return

        move_disks(n - 1, source, auxiliary, target)

        disk = source.pop()
        target.append(disk)
        record_state()

        move_disks(n - 1, auxiliary, target, source)

    record_state()
    move_disks(n, rod1, rod3, rod2)

    return "\n".join(result)

print(hanoi_solver(3))
