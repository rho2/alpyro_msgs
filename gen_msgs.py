#!/usr/bin/env python3
import base64
import subprocess
from typing import Dict, List, Set, Union
from pathlib import Path

def rosmsg(args: Union[str, List[str]]) -> str:
    if isinstance(args, str):
        args = [args]
    return subprocess.check_output(["/alpyro/rosmsg"] + args).decode("utf-8")

def gen_pkg(pkg: str):
    print(f"- {pkg}")
    msgs = rosmsg(["package", pkg]).splitlines()

    folder = Path("/out", pkg)
    folder.mkdir(exist_ok=True)

    init_file = folder / "__init__.py"
    init_file.touch(exist_ok=True)

    classes: List[str] = []
    for msg in msgs:
        _, _, classname = msg.partition("/")
        print(f"  - {classname}")

        msg_def = rosmsg(["show", msg])
        md5_sum = rosmsg(["md5", msg]).strip()

        msg_def_b64 = base64.b64encode(msg_def.encode("utf-8")).decode("utf-8")

        fields: Dict[str, str] = {}
        simple_types: Set[str] = {"RosMessage"}
        packages: Set[str] = set()

        for line in msg_def.strip().splitlines():
            if line.startswith("  "):
                continue
            typ, name = line.split()
            fields[name] = typ.replace("/", ".").replace("bool", "boolean").replace("char", "uint8").replace('byte', "int8")

        for t in fields.values():
            if "." in t:
                packages.add(t.split("[", 1)[0])
            else:
                simple_types.add(t.split("[", 1)[0])

        defs: Dict[str, str] = {
            "__msg_typ__": f"\"{msg}\"",
            "__msg_def__": f"\"{msg_def_b64}\"",
            "__md5_sum__": f"\"{md5_sum}\"",
        }

        classes.append(classname)

        class_file = (folder / classname.lower()).with_suffix(".py")
        with open(class_file, "w") as out:
            if "[" in msg_def:
                print(f"from typing import List", file=out)
                print(f"from typing_extensions import Annotated", file=out)
            if "=" in msg_def:
                print(f"from typing import Final", file=out)
            print(f"from alpyro_msgs import {', '.join(sorted(simple_types))}", file=out)
            for p in sorted(packages):
                pkg, _, cls = p.partition(".")

                print(f"from alpyro_msgs.{pkg}.{cls.lower()} import {cls}", file=out)

            print("\n", file=out)
            print(f"class {classname}(RosMessage):", file=out)

            for name, value in defs.items():
                print(f"  {name} = {value}", file=out)
            print("", file=out)

            for name, typ in fields.items():
                typ = typ.rsplit(".")[-1]
                if "[" in typ:
                    base, _, size = typ[:-1].partition("[")
                    s = int(size) if size else 0
                    if base == "uint8":
                        typ = f"Annotated[bytes, {s}, 0]"
                    else:
                        typ = f"Annotated[List[{base}], {s}, 0]"
                if "=" in name:
                    name, _, val = name.partition("=")
                    if typ == "string":
                        val = f"\"{val}\""
                    print(f"  {name}: Final[{typ}] = {val}", file=out)
                else:
                    print(f"  {name}: {typ}", file=out)

packages = rosmsg("packages").splitlines()

for p in packages:
    gen_pkg(p)
