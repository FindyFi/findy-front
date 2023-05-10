FROM bcgovimages/von-image:node-1.12-6
USER root

# Set the working directory
WORKDIR /home/indy

ENV LOG_LEVEL ${LOG_LEVEL:-info}
ENV RUST_LOG ${RUST_LOG:-warning}

EXPOSE 80

COPY . /home/indy

# COPY server/static /app/static

# VOLUME /app/static

# Here we need to upgrade pip in order to intsall IndyVDR binary
# However, this causes issue with 'plenum' package (for example: https://github.com/bcgov/von-network/issues/238)
# So we need to downgrade to pip 9.0.3 after requirements install
RUN pip3 install -U pip && \
    pip install --no-cache-dir -r server/requirements.txt && \
    pip install psycopg2-binary && \
    pip install PyJWT && \       
    python -m pip install pip==9.0.3

ADD --chown=indy:indy . $HOME

ENTRYPOINT ["/bin/bash", "-c", "python -m server.server"]
