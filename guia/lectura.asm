; Para ensamblar y enlazar:
; nasm -f win32 input.asm -o input.obj
; gcc input.obj -o input.exe

global _main
extern _GetStdHandle@4
extern _WriteConsoleA@20
extern _ReadConsoleA@20
extern _ExitProcess@4

section .data
    prompt db 'Ingrese texto: ', 0
    len_prompt equ $ - prompt
    
section .bss
    input resb 100       ; Buffer para el input
    chars_read resd 1     ; Número de caracteres leídos

section .text
_main:
    ; Obtener handle de stdout
    push -11             ; STD_OUTPUT_HANDLE = -11
    call _GetStdHandle@4
    mov ebx, eax         ; Guardar handle de salida
    
    ; Mostrar prompt
    push 0               ; lpReserved
    push 0               ; lpNumberOfCharsWritten
    push len_prompt      ; nNumberOfCharsToWrite
    push prompt          ; lpBuffer
    push ebx             ; hConsoleOutput
    call _WriteConsoleA@20
    
    ; Obtener handle de stdin
    push -10             ; STD_INPUT_HANDLE = -10
    call _GetStdHandle@4
    mov esi, eax         ; Guardar handle de entrada
    
    ; Leer input
    push 0               ; lpReserved
    push chars_read      ; lpNumberOfCharsRead
    push 100             ; nNumberOfCharsToRead
    push input           ; lpBuffer
    push esi             ; hConsoleInput
    call _ReadConsoleA@20
    
    ; Salir
    push 0
    call _ExitProcess@4