## Plan: Backend FastAPI Tests

Vamos a agregar tests backend con pytest en una carpeta tests separada, con cobertura intermedia y estructura AAA en cada prueba. La idea es cubrir el comportamiento actual de la API sin refactorizar el backend, aislando el estado en memoria para que los tests no se contaminen entre sí.

**Steps**
1. Agregar pytest a requirements.txt para que la suite pueda instalarse y ejecutarse localmente.
2. Crear la carpeta tests con esta base:
   - tests/conftest.py
   - tests/test_activities_list.py
   - tests/test_signup.py
   - tests/test_unregister.py
3. En tests/conftest.py, definir:
   - una fixture de TestClient para la app FastAPI
   - una fixture que haga backup y restore del diccionario global activities con deepcopy
4. Implementar tests para GET /activities en tests/test_activities_list.py.
   - Caso 200
   - Validación básica de estructura del payload
5. Implementar tests para POST /activities/{activity_name}/signup en tests/test_signup.py.
   - Registro exitoso
   - Registro duplicado con 400
   - Actividad inexistente con 404
6. Implementar tests para DELETE /activities/{activity_name}/participants en tests/test_unregister.py.
   - Eliminación exitosa
   - Actividad inexistente con 404
   - Participante no registrado con 404
7. Estructurar cada test con AAA explícito:
   - Arrange: preparar client, actividad/email y estado inicial
   - Act: ejecutar la request HTTP
   - Assert: validar status, respuesta JSON y mutación del estado si aplica
8. Ejecutar pytest desde la raíz y ajustar cualquier detalle menor de imports o aislamiento.

**Relevant files**
- requirements.txt — agregar pytest
- pytest.ini — reutilizar configuración existente
- src/app.py — usar la app y el estado actual como sistema bajo prueba
- tests/conftest.py — fixtures compartidas
- tests/test_activities_list.py — pruebas de listado
- tests/test_signup.py — pruebas de registro
- tests/test_unregister.py — pruebas de desregistro

**Verification**
1. Instalar dependencias y correr pytest -v desde la raíz.
2. Ejecutar la suite completa y luego archivos individuales para confirmar aislamiento.
3. Revisar que cada test tenga bloques AAA visibles y consistentes.

**Decisions**
- Incluido: pytest, carpeta tests separada, cobertura intermedia, patrón AAA.
- Excluido por ahora: frontend tests, edge cases extensivos y cambios de arquitectura.
- Se tomará como contrato actual el comportamiento ya implementado en src/app.py.

Si te parece bien este plan, ya queda listo para que el siguiente agente lo implemente.
