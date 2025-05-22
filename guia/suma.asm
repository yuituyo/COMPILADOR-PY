global _main
extern _ExitProcess@4

section .data
    num1 dd 15      ; Primer número
    num2 dd 27      ; Segundo número

section .text
_main:
    mov eax, [num1] ; Cargar primer número en EAX
    add eax, [num2] ; Sumar segundo número (EAX = EAX + num2)
    
    ; El resultado queda en EAX (15 + 27 = 42)
    
    ; Salir con código de retorno = resultado (solo byte bajo)
    push eax
    call _ExitProcess@4