#!/bin/sh

redis-server

redis-cli XGROUP CREATE mystream groupname $ MKSTREAM

