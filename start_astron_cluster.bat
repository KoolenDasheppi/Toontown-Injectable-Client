@echo off
cd astron
:main
astrond --loglevel info config/cluster.yml
goto main