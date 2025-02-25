# article generator

## requirements

cerebras api key  
serper api key https://serper.dev/api-key

## How to run

1. add api keys to env file (backend/.env.sample)
2. install python packages

```shell
cd backend
pip install -r requirements.txt
```

3. install node packages

```shell
cd frontend
pnpm install
```

4. run frontend and backend

```shell
cd frontend
pnpm run dev
```

```shell
cd backend
uvicorn server:app --reload
```
