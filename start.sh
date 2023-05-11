#!/bin/sh

GENESIS_FILE=$PWD/pool_transactions_genesis \
LEDGER_SEED=$1 \
JWT_SECRET=$2 \
PORT=9000 \
LOG_LEVEL=info \
RUST_LOG=warning \
REGISTER_NEW_DIDS=True \
python -m server.server