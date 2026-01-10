@echo off
echo Running Consolide examples...
echo.

for /d %%d in (examples\*) do (
    echo ==============================
    echo Running %%~nd
    echo ==============================
    python examples\%%~nd\main.py
    echo.
)

echo Done.
