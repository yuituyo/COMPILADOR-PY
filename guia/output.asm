section .data
    msg db "Hola desde ASM en Windows!", 13, 10   ; Texto + retorno de carro (13) + salto de línea (10)
    msg_len equ $ - msg                           ; Longitud del mensaje

section .text
    global Start
    extern GetStdHandle, WriteConsoleA, ExitProcess   ; Importar funciones de kernel32.dll

Start:
    ; 1. Obtener el "handle" de la consola (stdout)
    mov rcx, -11                 ; STD_OUTPUT_HANDLE = -11 (constante de Windows)
    call GetStdHandle            ; RAX = handle de la consola

    ; 2. Imprimir el mensaje en la consola
    mov rcx, rax                ; Handle de la consola (1er argumento)
    lea rdx, [msg]              ; Dirección del mensaje (2do argumento)
    mov r8, msg_len             ; Longitud del mensaje (3er argumento)
    xor r9, r9                  ; Bytes escritos (NULL, no lo necesitamos)
    push 0                      ; Reservar espacio en la pila (alineación para __fastcall)
    call WriteConsoleA          ; Llama a WriteConsoleA

    ; 3. Salir del programa
    xor rcx, rcx                ; Código de retorno (0 = éxito)
    call ExitProcess            ; Termina el programa