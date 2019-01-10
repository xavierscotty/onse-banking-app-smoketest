#!/bin/bash

git submodule add git@bitbucket.org-armakuni:armakuni/onse-transaction-service.git onse-transaction-service
git submodule add git@bitbucket.org-armakuni:armakuni/onse-account-service.git onse-account-service
git submodule add git@bitbucket.org-armakuni:armakuni/onse-customer-service.git onse-customer-service
git submodule add git@bitbucket.org-armakuni:armakuni/onse-customer-service.git onse-customer-service
git submodule add git@bitbucket.org-armakuni:armakuni/onse-cashier-service.git onse-cashier-service
git submodule add git@bitbucket.org-armakuni:armakuni/onse-balance-service.git onse-balance-service

git submodule init
git submodule update --remote --merge
