## Ignoring files from mbed build

An `.mbedignore` file tells the `mbed compile` and `mbed export` commands which files and directories to ignore (not process).

### Usage
You can place an `.mbedignore` file in any directory searched by `mbed compile` or `mbed export`.

Avoid defining rules that would cross the library boundaries; these can lead to side effects or build problems that are hard to find.

### Syntax

Each line in the `.mbedignore` file is a file pattern used for matching files. `mbed compile` and `mbed export` ignore every file that matches any pattern found in any `.mbedignore` file.

The following wildcards are accepted:

|Pattern | Meaning|
|--------|--------|
| `*` | Matches everything. |
| `?` | Matches any single character. |
| `[seq]` | Matches any character in seq. |
| `[!seq]` | Matches any character not in seq. |

The file is parsed with Python's [fnmatch](https://docs.python.org/2/library/fnmatch.html). The syntax follows basic shell patterns with the following exceptions:

1. Each line is treated as though it were prefixed with the path of the `.mbedignore` file.
2. A line cannot start with `.` or `/` (because of rule 1).

The globbing functionality is not used, so you cannot recursively match a specific file pattern. Instead, you need to define a rule per directory.

You can use relative paths, so you can match files deeper in the build tree. However, avoid crossing library boundaries.

### Example

A file located in `source/obsolete/.mbedignore` with the following content:

```
*.c
*.h
second_level/*.c
```

After applying rule 1, the actual patterns used internally for matching the source files are:

```
source/obsolete/*.c
source/obsolete/*.h
source/obsolete/second_level/*.c
```
