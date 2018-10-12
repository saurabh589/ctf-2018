.intel_syntax noprefix
.bits 32
					//input  asm2(0x4,0x2d)
.global asm2

asm2:
	push   	ebp
	mov    	ebp,esp
	sub    	esp,0x10
	mov    	eax,DWORD PTR [ebp+0xc] // 0x2d
	mov 	DWORD PTR [ebp-0x4],eax
	mov    	eax,DWORD PTR [ebp+0x8] //0x4
	mov	DWORD PTR [ebp-0x8],eax
	jmp    	part_b
part_a:	
	add    	DWORD PTR [ebp-0x4],0x1  // 0x2d+0x1
	add	DWORD PTR [ebp+0x8],0x64   // 0x4 + 0x64
part_b:	
	cmp    	DWORD PTR [ebp+0x8],0x1d89
	jle    	part_a
	mov    	eax,DWORD PTR [ebp-0x4]
	mov	esp,ebp
	pop	ebp
	ret
