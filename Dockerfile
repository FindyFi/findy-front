FROM bcgovimages/von-image:node-1.12-6
USER root

ENV LOG_LEVEL ${LOG_LEVEL:-info}
ENV RUST_LOG ${RUST_LOG:-warning}

EXPOSE 80

COPY . /home/indy

COPY ./server/static /app/static

# Here we need to upgrade pip in order to intsall IndyVDR binary
# However, this causes issue with 'plenum' package (for example: https://github.com/bcgov/von-network/issues/238)
# So we need to downgrade to pip 9.0.3 after requirements install
RUN pip3 install -U pip && \
    pip install --no-cache-dir -r server/requirements.txt && \
    pip install psycopg2-binary && \
    pip install PyJWT && \       
    python -m pip install pip==9.0.3

ADD --chown=indy:indy . $HOME

# Set the working directory
WORKDIR /home/indy

RUN [ -f $HOME/.env ] || touch $HOME/.env

ENTRYPOINT ["/bin/bash", "-c", "source $HOME/.env && GENESIS_FILE=$PWD/pool_transactions_genesis \
    LEDGER_SEED=$TRUSTEE_SEED \
    PORT=80 \
    LOG_LEVEL=info \
    RUST_LOG=warning \
    REGISTER_NEW_DIDS=True \
    AML_CONFIG_FILE=$PWD/config/sample_aml.json \
    TAA_CONFIG=$PWD/config/sample_taa.json \
    python -m server.server"]

# ENTRYPOINT ["/bin/bash", "-c", "python -m server.server"]
