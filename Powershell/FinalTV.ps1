#Monitoramento e exibição de telas Grafana. 
#Versão 1.0
#Criador: Kelvyn.prete
#Finalidade: Monitoramento
#Time Responsável: COMS

#Esse script tem como finalidade atualizar as telas de monitoramento da sala do Datacenter, manejadas pelo time de COMS.
#Ele irá executar em tarefa agendada no Windows, sem a necessidade de interação, atualizando-se a cada 10min 

# Definição de URL e usuário padrão
$pathToChrome = '"C:\Program Files\Google\Chrome\Application\chrome.exe"'
$tempFolder1 = '--user-data-dir=C:\Temp\Screen1'
$tempFolder2 = '--user-data-dir=C:\Temp\Screen2'
$tempFolder3 = '--user-data-dir=C:\Temp\Screen3'
$tempFolder4 = '--user-data-dir=C:\Temp\Screen4'
$startPage1 = 'http://172.18.190.77:3000/d/DyTLMN67k/tesp1-tradicional-monitor-recursos?orgId=1'
$startPage2 = 'http://172.18.190.77:3000/d/RHhw8XX7z/tesp1-intera-monitor-recursos?orgId=1&refresh=30s'
$startPage3 = 'http://172.18.190.77:3000/d/EOvVA3Xnk/tesp2-monitor-recursos?orgId=1&refresh=30s'
$startPage4 = 'http://172.18.190.121/check_mk_central/check_mk/index.py?start_url=%2Fcheck_mk_central%2Fnagvis%2Ffrontend%2Fnagvis-js%2Findex.php%3Fmod%3DMap%26act%3Dview%26show%3DGlobal-TOTVS'

# Loop executar o código a cada 5 minutos
while($true) {
    # Mede o tempo de execução do código
    $startTime = Get-Date
    
    # Abre o chrome em páginas separadas, uma pagina por monitor
    Start-Process -FilePath $pathToChrome -ArgumentList '--new-window', $tempFolder1, '--window-position=8,1080', '--window-size=1920,1080', $startPage1 -ErrorVariable Test1
    Start-Process -FilePath $pathToChrome -ArgumentList '--new-window', $tempFolder2, '--window-position=1928,1104', '--window-size=1920,1080', $startPage2 -ErrorVariable Test2
    Start-Process -FilePath $pathToChrome -ArgumentList '--new-window', $tempFolder3, '--window-position=1920,-8', '--window-size=1920,1080', $startPage3 -ErrorVariable Test3
    Start-Process -FilePath $pathToChrome -ArgumentList '--new-window', $tempFolder4, '--window-position=0,0', '--window-size=1920,1080', $startPage4 -ErrorVariable Test4

    # Sleep de 10 minutos para reabrir as páginas
    Start-Sleep -Seconds 600

    # Fechar todas as janelas do Chrome
    Stop-Process -Name chrome -Force
    
    # Tempo de execução do código
    $endTime = Get-Date
    $executionTime = New-TimeSpan $startTime $endTime
    Write-Output "Tempo de execução: $($executionTime.TotalSeconds) segundos."
}
