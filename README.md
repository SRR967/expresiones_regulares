# expresiones_regulares

Este proyecto fue realizado para la materia de Teoria de Lenguajes Formales.

Realizado por Jhoan Esteban Soler Giraldo, Johana Paola Palacio Osorio, Santiago Ramón Ramos


## Caracteristicas del proyecto
1. Validar expresiones regulares ingresadas por el usuario.
2. Analizar y tokenizar las expresiones regulares.
3. Generar autómatas finitos no deterministas (AFND) basados en las
expresiones regulares.
4. Visualizar los autómatas generados utilizando una interfaz gráfica.

## Estructura del proyecto

El proyecto está organizado en varias clases con responsabilidades específicas:

1. AnalizadorLexico
Descripción:

Descompone una expresión regular en tokens y valida su estructura.
Funciones principales:

tokenizar: Convierte la expresión regular en tokens (literales, operadores, paréntesis).
validar_estructura: Valida errores de sintaxis como paréntesis desbalanceados o operadores consecutivos.
analizar: Ejecuta el proceso completo de tokenización y validación.
obtener_tokens: Devuelve los tokens generados.
obtener_errores: Retorna los errores encontrados.

2. Grafo y Nodo
Descripción:

Representa el autómata generado con nodos y transiciones.
Funciones principales:

agregar_nodo: Crea un nodo en el grafo.
conectar: Conecta dos nodos con un símbolo de transición.
set_estado_inicial: Establece el nodo inicial del grafo.
agregar_estado_final: Marca un nodo como estado final.
visualizar: Genera una representación visual del grafo usando Graphviz.

3. ManejadorDeErrores
Descripción:

Gestiona errores encontrados durante el análisis y validación de expresiones regulares.
Funciones principales:

agregar_error: Registra un error en la lista de errores.
obtener_errores: Devuelve todos los errores almacenados.
limpiar_errores: Limpia la lista de errores.

4. GeneradorDeAutomatas
Descripción:

Construye un grafo dirigido que representa un AFND basado en tokens.
Funciones principales:

construir_grafo_desde_tokens: Procesa una lista de tokens y genera un AFND utilizando operadores como *, + y |.

5. MotorDeValidacion
Descripción:

Valida cadenas de entrada contra una expresión regular utilizando Python Regex.
Funciones principales:

compilar_expresion: Compila la expresión regular para validaciones.
validar_cadena: Comprueba si una cadena cumple con la expresión regular.
validar_multiples_cadenas: Valida múltiples cadenas y devuelve un diccionario con los resultados.
obtener_errores: Retorna errores detectados en la compilación de la expresión.

6. InterfazUsuario
Descripción:

GUI construida con Tkinter que permite al usuario interactuar con el proyecto.
Funciones principales:

validar_expresion: Valida la expresión regular ingresada y las cadenas proporcionadas.
mostrar_automata: Genera y visualiza el autómata basado en la expresión regular.

## Guia de Usuario

Requisitos
Python 3.x
Paquetes requeridos: graphviz, tkinter (incluido por defecto en Python).

### Instalacion
1. Instalar dependencias
    pip install graphviz

2. 

## Uso de la aplicacion

1. Ingresa una expresión regular válida en el campo correspondiente.
2. Ingresa una o varias cadenas separadas por comas para validar.
3. Presiona:
    "Validar" para verificar las cadenas contra la expresión regular.
    "Generar Autómata" para visualizar el autómata generado.

### ✅ Expresiones regulares permitidas
Estas son las expresiones regulares válidas que puedes ingresar en el sistema:

#### Letras y números:

Puedes usar cualquier letra (a-z, A-Z) o dígito (0-9) como símbolos.
Ejemplo: a, b123, x5.
#### Operadores básicos:

Concatenación (implícita): Se entiende que los símbolos consecutivos están concatenados.
Ejemplo: ab genera un autómata donde primero va a seguido de b.
Unión (|): Se utiliza para representar alternativas entre símbolos o grupos.
Ejemplo: a|b genera un autómata que acepta a o b.
Cerradura de Kleene (*): Representa cero o más repeticiones de un símbolo o grupo.
Ejemplo: a* genera un autómata que acepta cadenas como ε, a, aa, aaa, etc.
Cerradura positiva (+): Representa una o más repeticiones de un símbolo o grupo.
Ejemplo: a+ genera un autómata que acepta a, aa, aaa, etc., pero no ε.

#### Agrupación con paréntesis (()):

Puedes usar paréntesis para agrupar partes de una expresión.
Ejemplo: (a|b)c genera un autómata que acepta ac o bc.
Combinaciones de los anteriores:

Ejemplo: (a|b)*c+ genera un autómata que acepta cadenas como c, ccc, ac, bc, aacc, etc.
❌ Expresiones regulares no permitidas
Estas son las expresiones que el sistema no puede manejar actualmente:

#### Operadores avanzados no soportados:

Rangos ([a-z]): No puedes usar rangos de caracteres.
❌ Ejemplo: [a-z] o [0-9].
Negaciones (^): No puedes especificar exclusiones.
❌ Ejemplo: [^a] o [^0-9].
Grupos opcionales (?): No se admite el uso de ? para hacer un símbolo opcional.
❌ Ejemplo: a? (no soportado).
Expresiones con llaves {}:

No puedes definir un número específico de repeticiones.
❌ Ejemplo: a{2,3} o b{4}.
Expresiones inválidas:

Paréntesis desbalanceados:
❌ Ejemplo: (a|b.
Operadores consecutivos:
❌ Ejemplo: a++b o a|*b.
Cadenas vacías:
❌ Ejemplo: Ingresar una cadena sin contenido.
Caracteres especiales no soportados:

El sistema no reconoce caracteres especiales como \d, \w, . o \s.
❌ Ejemplo: a\d, b\w.

