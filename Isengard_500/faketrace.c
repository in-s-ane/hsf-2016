#include <stdio.h>
/* #define __USE_GNU */
/* #include <dlfcn.h> */

/* typedef ssize_t (*orig_read_t)(int fd, void* buf, size_t count); */
/* orig_read_t orig_read; */

long ptrace(int x, int y, int z)
{
    //printf("%p\n", __builtin_return_address(0));
    return 0;
}

/* ssize_t read(int fd, void* buf, size_t count) */
/* { */
/*     printf("read: %p\n", __builtin_return_address(0)); */
/*     orig_read = (orig_read_t)dlsym(RTLD_NEXT, "read"); */
/*     return orig_read(fd, buf, count); */
/* } */
