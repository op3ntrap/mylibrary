#!/usr/bin/env bash

rm -R TransactionManager/migrations/000*
rm -R BookManager/migrations/000*
rm -R UserManager/migrations/000*
rm -R testapp/migrations/000*
echo "The Migrations have been cleared"