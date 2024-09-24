![Base](logo.webp)

# Вузол Base

Base — це безпечний, недорогий та зручний для розробників Ethereum L2, створений для того, щоб залучити наступний мільярд користувачів у блокчейн. Він побудований на основі [OP Stack](https://stack.optimism.io/)з відкритим вихідним кодом від Optimism..

Цей репозиторій містить відповідні збірки Docker для запуску вашого власного вузла в мережі Base.

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

### Вимоги до апаратного забезпечення

Рекомендуємо мати таку конфігурацію обладнання для запуску вузла:

- сучасний багатоядерний процесор з хорошою одноядерною продуктивністю
- щонайменше 16 ГБ оперативної пам’яті (рекомендується 32 ГБ)
- високопродуктивний SSD-диск (рекомендується NVME) з об’ємом не менше 750 ГБ (повний вузол) або 4,5 ТБ (архівний вузол) вільного місця

### Вирішення проблем

Якщо ви зіткнулися з проблемами з вашим вузлом, будь ласка, відкрийте [GitHub issue](https://github.com/base-org/node/issues/new/choose) або зверніться до нас у  [Discord](https://discord.gg/buildonbase):

- Після приєднання у додатку Discord перейдіть до `server menu` > `Linked Roles` > `connect GitHub` і підключіть свій обліковий запис GitHub, щоб отримати доступ до наших каналів для розробників
- Повідомте про вашу проблему в `#🛟|developer-support` або `🛠｜node-operators`

### Підтримувані мережі

| Base Network      | Status |
|-------------------| ------ |
| Testnet (Sepolia) | ✅     |
| Mainnet           | ✅     |

### Використання

1. Переконайтеся, що у вас є RPC-вузол Ethereum L1 (не Base), і встановіть `OP_NODE_L1_ETH_RPC` (у файлі  `.env.*` якщо використовуєте  docker-compose). Якщо ви запускаєте власний L1-вузол, він має бути синхронізований перед тим, як Base зможе повністю синхронізуватися.
2. Розкоментуйте рядок, який відповідає вашій мережі (`.env.sepolia`, або `.env.mainnet`) під 2 ключами `env_file` у `docker-compose.yml`.
3. Запустіть команду:

```
docker compose up --build
```

4. Тепер ви повинні мати можливість виконати запит до свого Base-вузла за допомогою `curl`:

```
curl -d '{"id":0,"jsonrpc":"2.0","method":"eth_getBlockByNumber","params":["latest",false]}' \
  -H "Content-Type: application/json" http://localhost:8545
```

Примітка: Деякі L1-вузли (наприклад, Erigon) не підтримують отримання доказів сховища. Ви можете обійти це, вказавши `--l1.trustrpc` під час запуску op-node (додайте це у `op-node-entrypoint` та перебудуйте образ docker за допомогою `docker compose build`.) Не робіть цього, якщо ви повністю не довіряєте постачальнику вузла L1.

#### Збереження даних

За замовчуванням каталог даних зберігається в `${PROJECT_ROOT}/geth-data`. Ви можете змінити це, модифікувавши значення змінної
`GETH_HOST_DATA_DIR` у файлі [`.env`](./.env).

Щоб завантажити [знімок](#snapshots) ви можете розпакувати знімок у папку `$GETH_HOST_DATA_DIR`.

#### Запуск у єдиному контейнері з `supervisord`

Якщо ви хочете запустити вузол у єдиному контейнері замість `docker-compose`, ви можете використовувати entrypoint `supervisord`.
Це корисно, наприклад, для запуску вузла в Kubernetes-кластері.

Зверніть увагу, що вам потрібно буде перевизначити деякі параметри за замовчуванням, які передбачають середовище з кількома контейнерами (`OP_NODE_L2_ENGINE_RPC`) а також можливі конфлікти портів (`OP_NODE_RPC_PORT`).
Приклад:

```
docker run --env-file .env.sepolia -e OP_NODE_L2_ENGINE_RPC=ws://localhost:8551 -e OP_NODE_RPC_PORT=7545 ghcr.io/base-org/node:latest
```

### Знімки

Ви можете отримати останні знімки за URL-адресами, наданими в [документації Base](https://docs.base.org/guides/run-a-base-node/#snapshots).

### Синхронізація

Швидкість синхронізації залежить від вашого L1-вузла, оскільки більша частина ланцюга базується на даних, надісланих до L1. Ви можете перевірити статус синхронізації, використовуючи RPC `optimism_syncStatus` у контейнері `op-node` container. Наприклад:

```
command -v jq  &> /dev/null || { echo "jq is not installed" 1>&2 ; }
echo Latest synced block behind by: \
$((($( date +%s )-\
$( curl -s -d '{"id":0,"jsonrpc":"2.0","method":"optimism_syncStatus"}' -H "Content-Type: application/json" http://localhost:7545 |
   jq -r .result.unsafe_l2.timestamp))/60)) minutes
```

## Відмова від відповідальності

Ми раді, що ви розробляєте на Base 🔵 — але ми хочемо переконатися, що ви розумієте характер програмного забезпечення вузла та смарт-контрактів, представлених тут.

ПРОГРАМНЕ ЗАБЕЗПЕЧЕННЯ ВУЗЛА ТА СМАРТ-КОНТРАКТИ, ЩО МІСТЯТЬСЯ ТУТ, НАДАЮТЬСЯ "ЯК Є", "ЯК Є", З УСІМА ДЕФЕКТАМИ ТА БЕЗ ЖОДНИХ ГАРАНТІЙ БУДЬ-ЯКОГО ВИДУ, ПРЯМО ВИСЛОВЛЕНИХ АБО НЕВИРАЖЕНИХ, ВКЛЮЧАЮЧИ БУДЬ-ЯКІ ГАРАНТІЇ ТОВАРНОЇ ПРИДАТНОСТІ, НЕПОРУШЕННЯ АБО ПРИДАТНОСТІ ДЛЯ КОНКРЕТНОЇ МЕТИ. ЗОКРЕМА, НЕ НАДАЄТЬСЯ ЖОДНОГО ПРЕДСТАВНИЦТВА ЧИ ГАРАНТІЇ, ЩО ПРОГРАМНЕ ЗАБЕЗПЕЧЕННЯ ВУЗЛА ТА СМАРТ-КОНТРАКТИ ЗАХИСТЯТЬ ВАШІ АКТИВИ — АБО АКТИВИ КОРИСТУВАЧІВ ВАШОГО ЗАСТОСУНКУ — ВІД КРАДІЖКИ, ХАКЕРСЬКИХ АТАК, КІБЕРАТАК АБО ІНШИХ ФОРМ ВТРАТИ АБО ЗНЕЦІНЕННЯ.

Ви також розумієте, що використання програмного забезпечення вузла та смарт-контрактів підпадає під дію чинного законодавства, включаючи, але не обмежуючись, будь-які застосовні закони проти відмивання грошей, закони проти тероризму, закони про експортний контроль, обмеження для кінцевих користувачів, закони про конфіденційність або економічні санкції.
