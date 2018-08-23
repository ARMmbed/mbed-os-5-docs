## Unit testing

Use the `mbed unittest` command to build and run unit tests, or to generate files for new unit tests.

Build and run unit tests with `mbed unittest`. The arguments are:

* `--compile` to only compile unit tests.
* `--run` to only run unit tests.
* `-c` or `--clean` to clean build directory.
* `-d` or `--debug` to prepare debug build.
* `--coverage <TYPE>` to generate code coverage report where TYPE can be "html", "xml" or "both".
* `-m <NAME>` or `--make-program <NAME>` to select which make build tool to use where NAME can be "make", "gmake", "mingw32-make" or "ninja".
* `-g <NAME>` or `--generator <NAME>` to select which CMake generator to use where NAME can be "Unix Makefiles", "MinGW Makefiles" or "Ninja".
* `-r <EXPRESSION>` or `--regex <EXPRESSION>` to run tests matching the regular expression.
* `--build <PATH>` to specify build directory.
* `-v` or `--verbose` for verbose diagnostic output.

Generate files for a new unit test with `mbed unittest --new <FILE>`.

### Building and running unit tests

You can specify to only **build** the unit tests by using the `--compile option:

```
$ mbed unittest --compile
```

You can specify to only **run** the unit tests by using the `--run` option:

```
$ mbed unittest --run
```

If you do not specify any of these, `mbed unittest` will build all available unit tests and run them.

### Running a subset of tests

You can run a **limited set** of unit tests by using the `-r` or `--regex` option. This takes a regular expression, which it compares against the test names. For example to run all cellular unit tests you can specify:

```
$ mbed unittest -r cellular
```

### Getting code coverage

You can generate a code coverage report by using the `--coverage` option. For example to create an html report you can specify:

```
$ mbed unittest --coverage html
```

### Creating new unit tests

All unit tests are under `mbed-os/UNITTESTS` directory. You can **generate** the necessary files for a unit test by using the `--new` option. For example to create the files for `rtos/Semaphore.cpp` you can specify:

```
$ mbed unittest --new rtos/Semaphore.cpp
```
