
# Oracle Webhook Bot (Fly.io + GitHub Deploy Ready)

## 🚀 Deploy preko GitHub-a na Fly.io

1. Napravi novi GitHub repozitorijum (npr. `oracle-bot`)
2. Raspakuj ovaj ZIP i pokreni sledeće:

```
git init
git remote add origin https://github.com/USERNAME/oracle-bot.git
git add .
git commit -m "Initial commit"
git push -u origin master
```

3. Na Fly.io:
- Idi na "Create New App"
- Izaberi "Deploy from GitHub"
- Izaberi repo
- Deployuj

4. Dodaj `.env` varijable u Fly dashboard:
```
TELEGRAM_TOKEN=
TELEGRAM_CHAT_ID=
BINANCE_API_KEY=
BINANCE_SECRET=
```

5. Kad deploy završi, koristi Fly URL kao WEBHOOK za Telegram.
