#!/bin/bash

alembic stamp head
alembic upgrade head

cd ../
