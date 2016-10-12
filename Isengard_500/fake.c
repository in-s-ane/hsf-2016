#include <stdio.h>
#include <stdarg.h>

long ptrace(int x, int y, int z) {
    return 0;
}

ssize_t read(int fd, void *buf, size_t count) {
    puts("In read");
    return 0;
}

int printf(const char *format, ...) {
    puts("In printf");
    va_list arg;
    int done;

    va_start(arg, format);
    done = vfprintf(stdout, format, arg);
    va_end(arg);


    return done;
}
