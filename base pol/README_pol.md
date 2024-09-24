![Base](logo.webp)

# Węzeł Base

Base to bezpieczna, niskokosztowa, przyjazna dla deweloperów sieć Ethereum L2, zbudowana, aby wprowadzić kolejny miliard użytkowników do świata blockchain. Została opracowana na bazie otwartoźródłowego [OP Stack](https://stack.optimism.io/) od Optimism.

To repozytorium zawiera odpowiednie kompilacje Docker, które umożliwiają uruchomienie własnego węzła w sieci Base.

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

### Wymagania sprzętowe

Zalecamy następującą konfigurację sprzętową do uruchomienia węzła:

- nowoczesny wielordzeniowy procesor z dobrą wydajnością pojedynczego rdzenia
- co najmniej 16 GB RAM (zalecane 32 GB)
- wysokowydajny dysk SSD (zalecany NVME) z co najmniej 750 GB (pełny węzeł) lub 4,5 TB (węzeł archiwalny) wolnego miejsca

### Rozwiązywanie problemów

Jeśli napotkasz problemy z węzłem, otwórz [problem na GitHubie](https://github.com/base-org/node/issues/new/choose) lub skontaktuj się z nami na [Discord](https://discord.gg/buildonbase):

- Po dołączeniu do serwera, w aplikacji Discord przejdź do `server menu` > `Linked Roles` > `connect GitHub` i połącz swoje konto GitHub, aby uzyskać dostęp do naszych kanałów deweloperskich
- Zgłoś swój problem `#🛟|developer-support` lub `🛠｜node-operators`

### Obsługiwane sieci

| Base Network      | Status |
|-------------------| ------ |
| Testnet (Sepolia) | ✅     |
| Mainnet           | ✅     |

### Użytkowanie

1. Upewnij się, że masz dostęp do pełnego węzła Ethereum L1 RPC (nie Base) i ustaw `OP_NODE_L1_ETH_RPC` (w pliku `.env.*` jeśli używasz docker-compose). eśli uruchamiasz własny węzeł L1, musi być on zsynchronizowany, zanim Base będzie mogło się w pełni zsynchronizować.
2. Odkomentuj linię odpowiadającą Twojej sieci (`.env.sepolia`, lub `.env.mainnet`) w sekcjach `env_file` w pliku `docker-compose.yml`.
3. Uruchom:

```
docker compose up --build
```

4. Powinieneś teraz móc użyć `curl` do zapytania swojego węzła Base:

```
curl -d '{"id":0,"jsonrpc":"2.0","method":"eth_getBlockByNumber","params":["latest",false]}' \
  -H "Content-Type: application/json" http://localhost:8545
```

Uwaga: Niektóre węzły L1 (np. Erigon) nie obsługują pobierania dowodów przechowywania. Można to obejść, dodając `--l1.trustrpc` podczas uruchamiania op-node (dodaj to w `op-node-entrypoint` i odbuduj obraz dockera za pomocą `docker compose build`.) Nie rób tego, chyba że całkowicie ufasz dostawcy węzła L1.

#### Utrzymywanie danych

Domyślnie katalog danych jest przechowywany w `${PROJECT_ROOT}/geth-data`. Możesz to nadpisać, modyfikując wartość zmiennej
`GETH_HOST_DATA_DIR` w pliku [`.env`](./.env).

Aby załadować [snapshot](#snapshots) możesz wyodrębnić snapshot do folderu `$GETH_HOST_DATA_DIR`.

#### Uruchamianie w pojedynczym kontenerze z `supervisord`

Jeśli chcesz uruchomić węzeł w pojedynczym kontenerze zamiast używać `docker-compose`, możesz skorzystać z punktu wejścia `supervisord`.
Jest to przydatne na przykład do uruchamiania węzła w klastrze Kubernetes.

Zauważ, że będziesz musiał nadpisać niektóre ustawienia domyślne, które zakładają środowisko z wieloma kontenerami (`OP_NODE_L2_ENGINE_RPC`) oraz konflikty portów (`OP_NODE_RPC_PORT`).
Przykład:

```
docker run --env-file .env.sepolia -e OP_NODE_L2_ENGINE_RPC=ws://localhost:8551 -e OP_NODE_RPC_PORT=7545 ghcr.io/base-org/node:latest
```

### Snapshoty

Możesz pobrać najnowsze snapshoty za pomocą adresów URL podanych w [dokumentacji Base](https://docs.base.org/guides/run-a-base-node/#snapshots).

### Synchronizacja

Szybkość synchronizacji zależy od Twojego węzła L1, ponieważ większość łańcucha pochodzi z danych przesyłanych do L1. Możesz sprawdzić status synchronizacji, używając RPC `optimism_syncStatus` na kontenerze `op-node`. Przykład:

```
command -v jq  &> /dev/null || { echo "jq is not installed" 1>&2 ; }
echo Latest synced block behind by: \
$((($( date +%s )-\
$( curl -s -d '{"id":0,"jsonrpc":"2.0","method":"optimism_syncStatus"}' -H "Content-Type: application/json" http://localhost:7545 |
   jq -r .result.unsafe_l2.timestamp))/60)) minutes
```

## Zrzeczenie się odpowiedzialności

Cieszymy się, że możesz budować na Base 🔵 — ale chcemy upewnić się, że rozumiesz charakter oprogramowania węzła i inteligentnych kontraktów oferowanych tutaj.

OPROGRAMOWANIE WĘZŁA I INTELIGENTNE KONTRAKTY ZAWARTE W TYM MIEJSCU SĄ DOSTARCZANE W STANIE, W JAKIM SĄ, Z WSZYSTKIMI WADAMI I BEZ GWARANCJI JAKIEGOKOLWIEK RODZAJU, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM BEZ GWARANCJI PRZYDATNOŚCI HANDLOWEJ, NARUSZENIA PRAW LUB PRZYDATNOŚCI DO KONKRETNEGO CELU. W SZCZEGÓLNOŚCI, NIE MA ŻADNEGO OŚWIADCZENIA ANI GWARANCJI, ŻE OPROGRAMOWANIE WĘZŁA I INTELIGENTNE KONTRAKTY OCHRONIĄ TWOJE AKTYWA — LUB AKTYWA UŻYTKOWNIKÓW TWOJEJ APLIKACJI — PRZED KRADZIEŻĄ, HACKOWANIEM, ATAKAMI CYBERNETYCZNYMI LUB INNYMI FORMAMI UTRATY LUB DEWALUACJI.

Rozumiesz również, że korzystanie z oprogramowania węzła i inteligentnych kontraktów podlega obowiązującym przepisom prawa, w tym, bez ograniczeń, wszelkim obowiązującym przepisom o przeciwdziałaniu praniu pieniędzy, przepisom antyterrorystycznym, przepisom o kontroli eksportu, ograniczeniom dla użytkowników końcowych, przepisom o prywatności lub przepisom o sankcjach ekonomicznych.
