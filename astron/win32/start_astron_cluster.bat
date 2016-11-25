@echo off
cd ..
:main
astrond --loglevel info config/cluster.yml
goto main