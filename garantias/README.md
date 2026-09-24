# Garantías y Mantenimiento — Leaseir

Panel en https://alejandroleaseir97.github.io/leaseir-portal/garantias/ (tarjeta en el cuadro de mando).

- `index.html` — el panel. Pide la contraseña del cuadro de mando y descifra los datos en el navegador.
- `data.enc.json` — los datos **cifrados** (AES-256-GCM, clave PBKDF2-SHA256, igual que /conciliacion).
  El JSON en claro no se sube nunca al repo.

## Qué cruza
- Ventas: *Historical Sales - Valores V3.xlsx*, pestaña **Data (Valores)**. De cada nº de serie manda la línea de fecha más reciente.
- Holded (Leaseir Technologies): facturas de las cuentas **Mantenimiento Nacional / Internacional**; las series se leen de las líneas de cada PDF.

## Plazos de garantía
Botón **Reglas de garantía**: plazo por defecto (12 meses), reglas por nombre (Sin Vello 12, Elha 24, Epil Point 36)
y plazo manual cliente a cliente. En esta versión de GitHub se guardan en el navegador de quien los cambia.

## Refrescar datos
Regenerar el JSON y cifrarlo con `python ../conciliacion/cifrar.py data.json data.enc.json CONTRASEÑA`.
