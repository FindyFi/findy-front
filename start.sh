#!/bin/sh

GENESIS_FILE=$PWD/pool_transactions_genesis \
LEDGER_SEED=$1 \
PORT=9000 \
LOG_LEVEL=info \
RUST_LOG=warning \
REGISTER_NEW_DIDS=True \
AML_CONFIG_FILE=$PWD/config/sample_aml.json \
TAA_CONFIG=$PWD/config/sample_taa.json \
python -m server.server