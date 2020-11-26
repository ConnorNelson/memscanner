import sys
from collections import defaultdict


class Map:
    def __init__(self, mapping_str, pid):
        self.pid = pid

        segments = mapping_str.split()
        if len(segments) == 6:
            address, perms, offset, dev, inode, pathname = segments
        elif len(segments) == 5:
            address, perms, offset, dev, inode = segments
            pathname = None

        address_start, address_end = address.split("-")
        self.address_start = int(address_start, 16)
        self.address_end = int(address_end, 16)

        self.read = "r" in perms
        self.write = "w" in perms
        self.execute = "x" in perms
        self.shared = "s" in perms
        self.private = "p" in perms
        self.perms = perms

        self.offset = int(offset, 16)

        self.inode = inode

        self.pathname = pathname

    def __len__(self):
        return self.address_end - self.address_start

    def __contains__(self, item):
        if not isinstance(item, int):
            return False
        return self.address_start < item < self.address_end

    def __bytes__(self):
        with open(f"/proc/{self.pid}/mem", "rb") as f:
            try:
                f.seek(self.address_start)
                return f.read(len(self))
            except:
                return b""

    def __iter__(self):
        data = bytes(self)
        for offset in range(0, len(self), 8):
            yield data[offset : offset + 8]

    def __repr__(self):
        address = f"{hex(self.address_start)}-{hex(self.address_end)}"
        perms = self.perms
        pathname = self.pathname

        return f"<Map {address} {perms} {pathname}>"


def main():
    pid = int(sys.argv[1])

    with open(f"/proc/{pid}/maps") as f:
        maps = f.read()

    mappings = [Map(line, pid) for line in maps.strip().split("\n")]
    has_pointer = defaultdict(list)

    max_len = max(len(repr(mapping)) for mapping in mappings)

    for from_mapping in mappings:
        for offset, qword in enumerate(from_mapping):
            qword = int.from_bytes(qword, "little")
            for to_mapping in mappings:
                if to_mapping == from_mapping:
                    continue
                if to_mapping in has_pointer[from_mapping]:
                    continue
                if to_mapping.pathname == from_mapping.pathname:
                    continue
                if not to_mapping.pathname or not from_mapping.pathname:
                    continue
                if qword in to_mapping:
                    from_addr = f"0x{from_mapping.address_start + offset:016x}"
                    to_addr = f"0x{qword:016x}"
                    from_offset = f"0x{offset:08x}"
                    to_offset = f"0x{(qword - to_mapping.address_start):08x}"
                    from_str = f"{from_mapping.pathname} ({from_mapping.perms})"
                    to_str = f"{to_mapping.pathname} ({to_mapping.perms})"
                    print(
                        f"[{from_addr} -> {to_addr}]  (+{from_offset} -> +{to_offset})  {from_str} -> {to_str}"
                    )
                    has_pointer[from_mapping].append(to_mapping)


if __name__ == "__main__":
    main()
