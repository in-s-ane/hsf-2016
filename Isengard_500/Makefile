all:
	gcc -m32 -fPIC -c fake.c -o fake.o -fno-stack-protector
	ld -shared -m elf_i386 -o fake.so fake.o -ldl
