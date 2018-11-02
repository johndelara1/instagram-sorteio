@echo on
:while1
    python instagram.py %*
    msg/time:120 /w * "Intervalo de 2 minutos. Aguarde..." 
    goto :while1