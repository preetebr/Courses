#Monitoramento e exibição de telas Grafana. 
#Versão 1.0
#Local: C:\Users\user\Documents\WindowsPowerShell\Scripts
#Criador: Kelvyn
#Finalidade: Monitoramento
#Time Responsável: ## 

#Esse script tem como finalidade atualizar as telas de monitoramento da sala do Datacenter, manejadas pelo time de COMS.
#Ele irá executar em tarefa agendada no Windows, sem a necessidade de interação, atualizando-se a cada 10min 

# Definição de URL e usuário padrão
$pathToEdge = "msedge.exe"
$tempFolder1 = '--user-data-dir=C:\Temp\Screen1'
$tempFolder2 = '--user-data-dir=C:\Temp\Screen2'
$tempFolder3 = '--user-data-dir=C:\Temp\Screen3'
$tempFolder4 = '--user-data-dir=C:\Temp\Screen4'
$startPage1 = 'NomeHTTPS'
$startPage2 = 'NomeHTTPS'
$startPage3 = 'NomeHTTPS'
$startPage4 = 'NomeHTTPS'

# Loop para executar o código a cada 5 minutos
while ($true) {
    # Mede o tempo de execução do código
    $startTime = Get-Date

    # Abre o Microsoft Edge em páginas separadas, uma página por monitor
    Start-Process -FilePath $pathToEdge -ArgumentList '--new-window', '--profile-directory="$profilePath"', $tempFolder1, '--start-fullscreen', $startPage1 -ErrorVariable Test1
    Start-Process -FilePath $pathToEdge -ArgumentList '--new-window', '--profile-directory="$profilePath"', $tempFolder2, '--start-fullscreen', $startPage2 -ErrorVariable Test2
    Start-Process -FilePath $pathToEdge -ArgumentList '--new-window', '--profile-directory="$profilePath"', $tempFolder3, '--start-fullscreen', $startPage3 -ErrorVariable Test3
    Start-Process -FilePath $pathToEdge -ArgumentList '--new-window', '--profile-directory="$profilePath"', $tempFolder4, '--start-fullscreen', $startPage4 -ErrorVariable Test4

    # Aguarda 10 minutos para reabrir as páginas
    Start-Sleep -Seconds 600

    # Obtém os processos do Microsoft Edge pelo nome do arquivo executável
    $edgeProcesses = Get-Process -Name msedge -ErrorAction SilentlyContinue

    # Fecha apenas as janelas do Microsoft Edge sem encerrar o processo
    foreach ($process in $edgeProcesses) {
        $process.CloseMainWindow()
    }

    # Tempo de execução do código
    $endTime = Get-Date
    $executionTime = New-TimeSpan $startTime $endTime
    Write-Output "Tempo de execução: $($executionTime.TotalSeconds) segundos."
}
