#!/bin/bash

CLONE_URL=https://github.com/peterwu/copr-rendezvous.git
COMMITTISH=main
TIMEOUT=58000
COPR_REPO=peterwu/rendezvous

# iosevka-fusion
FONT_NAME=iosevka-fusion
FONT_SUBDIR=${FONT_NAME}-fonts
FONT_SPEC=${FONT_NAME}-fonts.spec

copr-cli buildscm               \
         --clone-url $CLONE_URL \
         --commit $COMMITTISH   \
         --subdir $FONT_SUBDIR  \
         --spec $FONT_SPEC      \
         --timeout $TIMEOUT     \
         --enable-net on        \
         --background           \
         --nowait               \
         $COPR_REPO
