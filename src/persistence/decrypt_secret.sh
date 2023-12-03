#!/bin/sh


gpg --quiet --batch --yes --decrypt --passphrase="$LARGE_SECRET_PASSPHRASE" \
--output ./app-str-team-6577bb093acd.json app-str-team-6577bb093acd.json.gpg

gpg --quiet --batch --yes --decrypt --passphrase="$LARGE_SECRET_PASSPHRASE" \
--output ./firebase_config.json firebase_config.json.gpg

