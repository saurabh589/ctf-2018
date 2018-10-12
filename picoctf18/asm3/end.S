global _start
	_start:
		push    0xcc85310c
		push    0xda0f9ac5
		push    0xf238999b
		push    0
		push   	ebp
		mov 	ebp,esp
		mov		eax,0xb6
		xor		al,al
		mov		ah,BYTE [ebp+0x8]
		sal		ax,0x10
		sub		al,BYTE [ebp+0xf]
		add		ah,BYTE [ebp+0xd]
		xor		ax,WORD [ebp+0x12]
		mov		esp, ebp
		pop		ebp
		ret
