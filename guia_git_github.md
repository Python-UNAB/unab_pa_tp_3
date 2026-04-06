# Guía rápida: Subir un proyecto a GitHub desde cero usando Git

## 1. Inicializar el repositorio local

```bash
git init
```

## 2. Configurar tu usuario (solo la primera vez)

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"
```

## 3. Agregar los archivos al área de staging

```bash
git add .
```

## 4. Hacer el primer commit

```bash
git commit -m "Primer commit"
```

## 5. Crear el repositorio en GitHub

- Ve a https://github.com y crea un nuevo repositorio (sin README ni archivos extra).
- Copia la URL del repositorio (por ejemplo: https://github.com/usuario/repositorio.git)

## 6. Agregar el remoto origin

```bash
git remote add origin https://github.com/usuario/repositorio.git
```

## 7. Renombrar la rama principal a main (opcional, pero recomendado)

```bash
git branch -M main
```

## 8. Subir el proyecto a GitHub

```bash
git push -u origin main
```

## 9. Trabajar con ramas (Branches)

- **Crear una nueva rama y moverse a ella**:

  ```bash
  git checkout -b nombre-de-la-rama
  # o la sintaxis más moderna:
  git switch -c nombre-de-la-rama
  ```

- **Cambiar de rama**:

  ```bash
  git checkout nombre-de-la-rama
  # o:
  git switch nombre-de-la-rama
  ```

- **Listar las ramas locales**:

  ```bash
  git branch
  ```

- **Listar todas las ramas (incluyendo remotas)**:

  ```bash
  git branch -a
  ```

- **Fusionar una rama a la actual** (asegúrate de estar en la rama que recibirá los cambios, ej. `main`):

  ```bash
  git merge nombre-de-la-rama
  ```

- **Eliminar una rama local**:
  ```bash
  git branch -d nombre-de-la-rama
  ```

## 10. Consultar estado, historial y repositorios

- **Ver el estado de los archivos** (qué está modificado, qué está en staging, etc.):

  ```bash
  git status
  ```

- **Ver el historial de commits**:

  ```bash
  git log
  # Historial compacto y gráfico:
  git log --oneline --graph --all
  ```

- **Ver qué cambió en los archivos** que aún no has agregado (staged):

  ```bash
  git diff
  ```

- **Clonar un repositorio remoto** en tu computadora local:

  ```bash
  git clone https://github.com/usuario/repositorio.git
  ```

- **Descargar información del remoto** (sin fusionar nada):
  ```bash
  git fetch
  ```

## 11. Deshacer cambios temporales (Stash y Restore)

- **Descartar cambios** en un archivo que NO tiene commit:

  ```bash
  git restore archivo.ext
  ```

- **Sacar un archivo del área de staging** (deshacer el `git add` pero conservar los cambios):

  ```bash
  git restore --staged archivo.ext
  ```

- **Guardar los cambios a medias** temporalmente en un "baúl" (útil si necesitas cambiar de rama urgentemente sin hacer commit):
  ```bash
  git stash
  ```
- **Recuperar esos cambios guardados** (del stash):
  ```bash
  git stash pop
  ```

---

## Crear un repositorio en GitHub desde la terminal (requiere GitHub CLI)

Si tienes instalada la GitHub CLI (`gh`):

```bash
gh repo create usuario/repositorio --public --source=. --remote=origin --push
```

- Puedes elegir `--public` o `--private`.
- Sigue las instrucciones interactivas.

---

## ¿Cómo funciona Git?

- **git init**: Inicializa un repositorio local.
- **git add**: Prepara archivos para el commit.
- **git commit**: Guarda los cambios localmente.
- **git remote add origin**: Vincula tu repo local con uno remoto (GitHub).
- **git push**: Sube los commits al repositorio remoto.
- **git pull**: Descarga cambios del remoto.

> ¡Listo! Así puedes versionar y subir tus proyectos a GitHub desde cero.
