#!/bin/sh


gpg --quiet --batch --yes --decrypt --passphrase="$LARGE_SECRET_PASSPHRASE" \
--output ./src/persistence/app-str-team-6577bb093acd.json ./src/persistence/app-str-team-6577bb093acd.json.gpg

gpg --quiet --batch --yes --decrypt --passphrase="$LARGE_SECRET_PASSPHRASE" \
--output ./src/persistence/firebase_config.json ./src/persistence/firebase_config.json.gpg

