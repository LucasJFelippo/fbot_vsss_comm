# Fbot Vsss Comm

This is a public package created by the FBot team of the Federal University of Rio Grande (FURG), for the LARC competition. This is a open source package, feel free to use as you wish.

### How to use

You just need to clone this repository to a folder on your project, and import `Communication` from `comm.py`

#### Exemple
```py
from path.to.package import Communication()

# Make an instance of Communication class
comm = Communication()

print(comm.robot(2, True))
```

### Setting file
`setting.json` are the setting file, there you can configure the ports of the robots and main cpu
