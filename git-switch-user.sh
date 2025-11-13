#!/bin/bash
============================================
Git Switch User Script para Linux / macOS
Cambia rápidamente entre diferentes perfiles de Git.
============================================
Definición de perfiles
declare -A PROFILES_NAME
declare -A PROFILES_EMAIL

PROFILES_NAME[1]="General"
PROFILES_EMAIL[1]="tucorreo@example.com"

PROFILES_NAME[2]="Santiago Chavarro"
PROFILES_EMAIL[2]="santiagoachm@gmail.com"

PROFILES_NAME[3]=""
PROFILES_EMAIL[3]=""

echo "========== Cambiar perfil de Git =========="
echo
echo "1) General"
echo "2) Personal"
echo "3) Trabajo"
echo
read -p "Selecciona el número del perfil: " choice

case $choice in
  1)
    git config --global user.name "TuNombre"
    git config --global user.email "${PROFILES_EMAIL[1]}"
    echo "✅ Perfil cambiado a GENERAL"
    ;;
  2)
    git config --global user.name "${PROFILES_NAME[2]}"
    git config --global user.email "${PROFILES_EMAIL[2]}"
    echo "✅ Perfil cambiado a PERSONAL"
    ;;
  3)
    git config --global user.name "${PROFILES_NAME[3]}"
    git config --global user.email "${PROFILES_EMAIL[3]}"
    echo "✅ Perfil cambiado a TRABAJO"
    ;;
  *)
    echo "❌ Opción no válida."
    exit 1
    ;;
esac

echo
echo "Configuración actual de Git:"
git config --global user.name
git config --global user.email

echo "--------------------------------------------"
