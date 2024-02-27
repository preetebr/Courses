#Esse script tem como função rodar nas TV's de monitoramento de COMS, fazendo com a visualização seja sempre a mesma, bastando executar o script(Ou coloca-lo como processo de iniciar sozinho pelo windows assim que a máquina for reiniciada)

Start-Process "chrome.exe" -ArgumentList "--start-maximized"
Start-Process "chrome.exe" -ArgumentList "--start-maximized"



Get-Process "chrome" | Foreach-Object { Set-WindowPosition $_.MainWindowHandle 0 0; Start-Sleep -Milliseconds 500; }
Get-Process "chrome" | Foreach-Object { Set-WindowPosition $_.MainWindowHandle 1920 0; Start-Sleep -Milliseconds 500; }

