$executionTime = Measure-Command {

  # Definir variáveis para as páginas e pastas temporárias
$pathToChrome = '"C:\Program Files\Google\Chrome\Application\chrome.exe"'
$tempFolder1 = '--user-data-dir=C:\Temp\Screen1'
$tempFolder2 = '--user-data-dir=C:\Temp\Screen2'
$tempFolder3 = '--user-data-dir=C:\Temp\Screen3'
$tempFolder4 = '--user-data-dir=C:\Temp\Screen4'
$startPage1 = 'https://www.domain1.com'
$startPage2 = 'https://www.domain2.com'
$startPage3 = 'https://www.domain3.com'
$startPage4 = 'https://www.domain4.com'

# Loop while infinito para executar a cada 5 minutos
while($true) {

  # Fechar todas as janelas do Chrome abertas
  Stop-Process -Name chrome -Force

  # Aguardar 5 minutos antes de abrir as páginas novamente
  Start-Sleep -Seconds (5 * 20)

  # Abrir o Chrome com as páginas desejadas
  Start-Process -FilePath $pathToChrome -ArgumentList '--new-window', $tempFolder1, '--window-position=1536,872', '--window-size=1920,1080', $startPage1 -ErrorVariable Test1
  Start-Process -FilePath $pathToChrome -ArgumentList '--new-window', $tempFolder2,  '--window-position=0,864', '--window-size=1920,1080', $startPage2 -ErrorVariable Test2
  Start-Process -FilePath $pathToChrome -ArgumentList '--new-window', $tempFolder3, '--window-position=1536,8', '--window-size=1920,1080', $startPage3 -ErrorVariable Test3
  Start-Process -FilePath $pathToChrome -ArgumentList '--new-window', $tempFolder4,  '--window-position=0,0', '--window-size=1920,1080', $startPage4 -ErrorVariable Test4

  }
}

# Exibir o tempo de execução
Write-Output "Tempo de execução: $($executionTime.TotalSeconds) segundos."