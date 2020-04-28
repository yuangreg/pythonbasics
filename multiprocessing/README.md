# Multiprocessing

#### Q: Multi-threading not working on python?
###### A: 

> If you are using the "standard" python implementation (aka cpython) you should be aware of the Global Interpreter Lock. 

>In CPython, the global interpreter lock, or GIL, is a mutex that prevents multiple native threads from executing Python bytecodes at once. This lock is necessary mainly because CPython's memory management is not thread-safe. (However, since the GIL exists, other features have grown to depend on the guarantees that it enforces.)

##### A possible alternative to **multithreading** is to use the **multiprocessing** module.