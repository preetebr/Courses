#Monitoramento e exibição de telas Grafana. 
#Versão 1.0
#Criador: @preete
#Finalidade: Monitoramento


#Esse script tem como finalidade atualizar as telas de monitoramento.
#Ele irá executar em tarefa agendada no Windows, sem a necessidade de interação, atualizando-se a cada 10min 

# Definição de URL e usuário padrão
$pathToChrome = '"C:\Program Files\Google\Chrome\Application\chrome.exe"'
$tempFolder1 = '--user-data-dir=C:\Temp\Screen1'
$tempFolder2 = '--user-data-dir=C:\Temp\Screen2'
$tempFolder3 = '--user-data-dir=C:\Temp\Screen3'
$tempFolder4 = '--user-data-dir=C:\Temp\Screen4'
$startPage1 = 'NomeHTTPS'
$startPage2 = 'NomeHTTPS'
$startPage3 = 'NomeHTTPS'
$startPage4 = 'NomeHTTPS'

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
