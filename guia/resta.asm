
global _main
extern _ExitProcess@4

section .data
    num1 dd 30      
    num2 dd 12      

section .text
_main:
    mov eax, [num1] ; Cargar numero en EAX
    sub eax, [num2] ; Restar  (EAX = EAX - num2)
    
    ; El resultado queda en EAX (30 - 12 = 18)
    
    ; Salir con código de retorno = resultado 
    push eax
    call _ExitProcess@4