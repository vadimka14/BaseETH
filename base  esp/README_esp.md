![Base](logo.webp)

# Nodo Base

Base es una solución Ethereum L2 segura, económica y amigable para desarrolladores, construida para llevar a la cadena a los próximos mil millones de usuarios. Está construida sobre el [OP Stack](https://stack.optimism.io/)de código abierto de Optimism.

Este repositorio contiene las construcciones de Docker relevantes para ejecutar tu propio nodo en la red Base.

<!-- Badge row 1 - status -->

[![GitHub contributors](https://img.shields.io/github/contributors/base-org/node)](https://github.com/base-org/node/graphs/contributors)
[![GitHub commit activity](https://img.shields.io/github/commit-activity/w/base-org/node)](https://github.com/base-org/node/graphs/contributors)
[![GitHub Stars](https://img.shields.io/github/stars/base-org/node.svg)](https://github.com/base-org/node/stargazers)
![GitHub repo size](https://img.shields.io/github/repo-size/base-org/node)
[![GitHub](https://img.shields.io/github/license/base-org/node?color=blue)](https://github.com/base-org/node/blob/main/LICENSE)

<!-- Badge row 2 - links and profiles -->

[![Website base.org](https://img.shields.io/website-up-down-green-red/https/base.org.svg)](https://base.org)
[![Blog](https://img.shields.io/badge/blog-up-green)](https://base.mirror.xyz/)
[![Docs](https://img.shields.io/badge/docs-up-green)](https://docs.base.org/)
[![Discord](https://img.shields.io/discord/1067165013397213286?label=discord)](https://base.org/discord)
[![Twitter Base](https://img.shields.io/twitter/follow/Base?style=social)](https://twitter.com/Base)

<!-- Badge row 3 - detailed status -->

[![GitHub pull requests by-label](https://img.shields.io/github/issues-pr-raw/base-org/node)](https://github.com/base-org/node/pulls)
[![GitHub Issues](https://img.shields.io/github/issues-raw/base-org/node.svg)](https://github.com/base-org/node/issues)

### Requisitos de Hardware

Recomendamos tener esta configuración de hardware para ejecutar un nodo:

- Un CPU moderno de múltiples núcleos con buen rendimiento de un solo núcleo.
- Al menos 16 GB de RAM (32 GB recomendados).
- Un disco SSD de alto rendimiento (NVME recomendado) con al menos 750 GB (nodo completo) o 4.5 TB (nodo de archivo) libres.

### Solución de Problemas

Si encuentras problemas con tu nodo, por favor abre un [issue en GitHub](https://github.com/base-org/node/issues/new/choose) o contacta en nuestro [Discord](https://discord.gg/buildonbase):

- Una vez que te hayas unido, en la aplicación de Discord ve a `server menu` > `Linked Roles` > `connect GitHub` y conecta tu cuenta de GitHub para obtener acceso a nuestros canales de desarrolladores.
- Reporta tu problema en `#🛟|developer-support` o `🛠｜node-operators`

### Redes Soportadas

| Base Network      | Status |
|-------------------| ------ |
| Testnet (Sepolia) | ✅     |
| Mainnet           | ✅     |

### Uso

1. Asegúrate de tener disponible un RPC completo de Ethereum L1 (no Base) y configura `OP_NODE_L1_ETH_RPC` (en el archivo `.env.*` si estás usando docker-compose). Si estás ejecutando tu propio nodo L1, debe estar sincronizado antes de que Base pueda sincronizarse completamente.
2. Descomenta la línea correspondiente a tu red (`.env.sepolia`, o `.env.mainnet`) bajo las 2 claves `env_file` en `docker-compose.yml`.
3. Ejecuta:

```
docker compose up --build
```

4. Ahora deberías poder `curl` a tu nodo Base:

```
curl -d '{"id":0,"jsonrpc":"2.0","method":"eth_getBlockByNumber","params":["latest",false]}' \
  -H "Content-Type: application/json" http://localhost:8545
```

Nota: Algunos nodos L1 (por ejemplo, Erigon) no admiten la obtención de pruebas de almacenamiento. Puedes sortear esto especificando `--l1.trustrpc` al iniciar op-node (añádelo en `op-node-entrypoint` y reconstruye la imagen de docker con `docker compose build`.) No hagas esto a menos que confíes plenamente en el proveedor del nodo L1.

#### Persistencia de Datos

Por defecto, el directorio de datos se almacena en `${PROJECT_ROOT}/geth-data`. Puedes sobrescribir esto modificando el valor de la variable
`GETH_HOST_DATA_DIR` en el archivo [`.env`](./.env).

Para cargar un [snapshot](#snapshots) puedes extraer el snapshot en la carpeta `$GETH_HOST_DATA_DIR`.

#### Ejecución en un contenedor único con `supervisord`

Si deseas ejecutar el nodo en un solo contenedor en lugar de `docker-compose`, puedes usar el punto de entrada `supervisord`.
Esto es útil para ejecutar el nodo en un clúster de Kubernetes, por ejemplo.

Ten en cuenta que necesitarás sobrescribir parte de la configuración predeterminada que asume un entorno de múltiples contenedores (`OP_NODE_L2_ENGINE_RPC`) y cualquier conflicto de puertos (`OP_NODE_RPC_PORT`).
Ejemplo:

```
docker run --env-file .env.sepolia -e OP_NODE_L2_ENGINE_RPC=ws://localhost:8551 -e OP_NODE_RPC_PORT=7545 ghcr.io/base-org/node:latest
```

### Snapshots

Puedes obtener los últimos snapshots a través de las URL proporcionadas en la [documentación de Base](https://docs.base.org/guides/run-a-base-node/#snapshots).

### Sincronización

La velocidad de sincronización depende de tu nodo L1, ya que la mayor parte de la cadena se deriva de los datos enviados al L1. Puedes verificar el estado de sincronización utilizando el RPC `optimism_syncStatus` en el contenedor `op-node`. Ejemplo:

```
command -v jq  &> /dev/null || { echo "jq is not installed" 1>&2 ; }
echo Latest synced block behind by: \
$((($( date +%s )-\
$( curl -s -d '{"id":0,"jsonrpc":"2.0","method":"optimism_syncStatus"}' -H "Content-Type: application/json" http://localhost:7545 |
   jq -r .result.unsafe_l2.timestamp))/60)) minutes
```

## Descargo de Responsabilidad

Estamos emocionados de que construyas sobre Base 🔵 — pero queremos asegurarnos de que entiendas la naturaleza del software de nodo y los contratos inteligentes ofrecidos aquí.

EL SOFTWARE DE NODO Y LOS CONTRATOS INTELIGENTES CONTENIDOS AQUÍ SE PROPORCIONAN TAL CUAL, DONDE ESTÁN, CON TODOS LOS DEFECTOS Y SIN GARANTÍA DE NINGÚN TIPO, EXPRESA O IMPLÍCITA, INCLUYENDO CUALQUIER GARANTÍA DE COMERCIALIZACIÓN, NO INFRACCIÓN, O APTITUD PARA CUALQUIER PROPÓSITO PARTICULAR. EN PARTICULAR, NO HAY REPRESENTACIÓN O GARANTÍA DE QUE EL SOFTWARE DE NODO Y LOS CONTRATOS INTELIGENTES PROTEGERÁN TUS ACTIVOS — O LOS ACTIVOS DE LOS USUARIOS DE TU APLICACIÓN — DE ROBOS, HACKEOS, ATAQUES CIBERNÉTICOS, O CUALQUIER OTRA FORMA DE PÉRDIDA O DEVALUACIÓN.

También entiendes que el uso del software de nodo y los contratos inteligentes está sujeto a la legislación aplicable, incluyendo sin limitación, cualquier ley aplicable contra el lavado de dinero, leyes contra el terrorismo, leyes de control de exportaciones, restricciones para usuarios finales, leyes de privacidad, o leyes/regulaciones de sanciones económicas.
